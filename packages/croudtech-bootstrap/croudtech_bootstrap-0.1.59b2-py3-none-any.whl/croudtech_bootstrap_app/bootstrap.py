from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any

import botocore.exceptions

if TYPE_CHECKING:
    from mypy_boto3_s3 import S3Client
    from mypy_boto3_secretsmanager import SecretsManagerClient
else:
    S3Client = object

import json
import logging
import os
import re
import shutil
import tempfile
import time
import typing
from collections.abc import MutableMapping
from pathlib import Path

import boto3
import botocore
import click
import yaml

from croudtech_bootstrap_app.logging import init as initLogs

from .redis_config import RedisConfig

logger = initLogs()


AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL", None)


class Utils:
    @staticmethod
    def chunk_list(data, chunk_size):
        for i in range(0, len(data), chunk_size):
            yield data[i : i + chunk_size]


class BootstrapParameters:
    def __init__(
        self,
        environment_name,
        app_name,
        bucket_name,
        click=click,
        prefix="/appconfig",
        region="eu-west-2",
        include_common=True,
        use_sns=True,
        endpoint_url=AWS_ENDPOINT_URL,
        parse_redis=True,
        cache_enabled=True,
        cache_directory=os.path.join(str(Path.home()), ".croudtech-bootstrap", "cache"),
    ):
        self.environment_name = environment_name
        self.app_name = app_name
        self.bucket_name = bucket_name
        self.click = click
        self.prefix = prefix
        self.region = region
        self.include_common = include_common
        self.logger = logging.getLogger(self.__class__.__name__)
        self.use_sns = use_sns
        self.endpoint_url = endpoint_url
        self.put_metrics = False
        self.parse_redis = parse_redis
        self.cache_enabled = cache_enabled
        self.cache_directory = cache_directory

    @property
    def bootstrap_manager(self) -> BootstrapManager:
        if not hasattr(self, "_bootstrap_manager"):
            self._bootstrap_manager = BootstrapManager(
                prefix=self.prefix,
                region=self.region,
                click=self.click,
                values_path=None,
                bucket_name=self.bucket_name,
                endpoint_url=self.endpoint_url,
            )
        return self._bootstrap_manager

    @property
    def environment(self) -> BootstrapEnvironment:
        if not hasattr(self, "_environment"):
            self._environment = BootstrapEnvironment(
                name=self.environment_name,
                path=None,
                manager=self.bootstrap_manager,
                cache_enabled=self.cache_enabled,
                cache_directory=self.cache_directory,
            )
        return self._environment

    @property
    def app(self) -> BootstrapApp:
        if not hasattr(self, "_app"):
            self._app = BootstrapApp(
                name=self.app_name,
                path=None,
                environment=self.environment,
                cache_enabled=self.cache_enabled,
                cache_directory=self.cache_directory,
            )
        return self._app

    @property
    def common_app(self) -> BootstrapApp:
        if not hasattr(self, "_common_app"):
            self._common_app = BootstrapApp(
                name="common",
                path=None,
                environment=self.environment,
                cache_enabled=self.cache_enabled,
                cache_directory=self.cache_directory,
            )
        return self._common_app

    def get_redis_db(self):
        parameters = self.get_params()
        redis_db, redis_host, redis_port = self.find_redis_config(parameters)
        return redis_db, redis_host, redis_port

    def find_redis_config(self, parameters, allocate=False):
        if "REDIS_DB" not in parameters or parameters["REDIS_DB"] == "auto":
            redis_host = (
                parameters["REDIS_HOST"] if "REDIS_HOST" in parameters else False
            )
            redis_port = (
                parameters["REDIS_PORT"] if "REDIS_PORT" in parameters else 6379
            )

            if redis_host is not None:
                redis_config_instance = RedisConfig(
                    redis_host=redis_host,
                    redis_port=redis_port,
                    app_name=self.app_name,
                    environment=self.environment_name,
                    put_metrics=self.put_metrics,
                )
                redis_db = redis_config_instance.get_redis_database(allocate)
                return redis_db, redis_host, redis_port
        return None, None, None

    def parse_params(self, parameters):
        if self.parse_redis:
            redis_db, redis_host, redis_port = self.find_redis_config(
                parameters, allocate=True
            )
            if redis_db or redis_db == 0:
                parameters["REDIS_DB"] = redis_db
                parameters["REDIS_URL"] = "redis://%s:%s/%s" % (
                    redis_host,
                    redis_port,
                    redis_db,
                )
            else:
                raise Exception("Couldn't allocate Redis Database")
        return parameters

    def get_params(self):
        app_params = self.app.get_remote_params()

        if self.include_common:
            common_params = self.common_app.get_remote_params()
            app_params = {**common_params, **app_params}
        return self.parse_params(app_params)

    def get_raw_params(self):
        app_params = self.app.get_remote_params(flatten=False)

        if self.include_common:
            common_params = self.common_app.get_remote_params(flatten=False)
            app_params = {**common_params, **app_params}
        return self.parse_params(app_params)

    def params_to_env(self, export=False):
        strings = []
        for parameter, value in self.get_params().items():
            os.environ[parameter] = str(value)
            prefix = "export " if export else ""
            strings.append(
                '%s%s="%s"'
                % (
                    prefix,
                    parameter,
                    str(value).replace("\n", "\\n").replace('"', '\\"'),
                )
            )
            logger.debug("Imported %s from SSM to env var %s" % (parameter, parameter))

        return "\n".join(strings)


class BootstrapApp:
    environment: BootstrapEnvironment

    def __init__(
        self,
        name,
        path,
        environment: BootstrapEnvironment,
        cache_enabled=True,
        cache_directory=os.path.join(str(Path.home()), ".croudtech-bootstrap", "cache"),
    ):
        self.name = name
        self.path = path
        self.environment = environment
        self.cache_enabled = cache_enabled
        self.cache_directory = cache_directory

    @property
    def s3_client(self) -> S3Client:
        return self.environment.manager.s3_client

    @property
    def ssm_client(self):
        return self.environment.manager.ssm_client

    @property
    def secrets_client(self) -> SecretsManagerClient:
        return self.environment.manager.secrets_client

    @property
    def secret_path(self):
        return os.path.join(self.environment.path, f"{self.name}.secret.yaml")

    def upload_to_s3(self):
        source = self.path
        bucket = self.environment.manager.bucket_name
        dest = os.path.join("", self.environment.name, os.path.basename(self.path))

        self.environment.manager.click.secho(
            f"Uploading {source} to s3 {bucket}/{dest}"
        )

        self.s3_client.upload_file(source, bucket, dest)

        self.environment.manager.click.secho(f"Uploaded {source} to s3 {bucket}/{dest}")

    @property
    def s3_key(self):
        return os.path.join("", self.environment.name, ".".join([self.name, "yaml"]))

    def fetch_from_s3(self, raw=False) -> typing.Dict[str, Any]:
        if not hasattr(self, "_s3_data"):
            response = self.s3_client.get_object(
                Bucket=self.environment.manager.bucket_name, Key=self.s3_key
            )
            self._s3_data = yaml.load(response["Body"], Loader=yaml.SafeLoader)
            if raw:
                return self._s3_data
            for key, value in self._s3_data.items():
                self._s3_data[key] = self.parse_value(value)

        return self._s3_data

    def parse_value(self, value):
        try:
            parsed_value = json.dumps(json.loads(value))
        except json.decoder.JSONDecodeError:
            parsed_value = value
        except TypeError:
            parsed_value = value
        return str(parsed_value).strip()

    def cleanup_ssm_parameters(self):
        local_value_keys = set(self.convert_flatten(self.local_values).keys() or [])
        self.raw = True
        remote_value_keys = set(self.remote_values or [])
        self.raw = None

        orphaned_ssm_parameters = remote_value_keys - local_value_keys

        for parameter in orphaned_ssm_parameters:
            parameter_id = self.get_parameter_id(parameter)
            try:
                self.ssm_client.delete_parameter(Name=self.get_parameter_id(parameter))
                logger.info(f"Deleted orphaned ssm parameter {parameter}")
            except Exception:
                logger.info(f"Parameter: {parameter_id} could not be deleted")

    def cleanup_secrets(self):
        local_secret_keys = self.convert_flatten(self.local_secrets).keys()
        remote_secret_keys = self.remote_secret_records.keys()

        orphaned_secrets = [
            item
            for item in remote_secret_keys
            if re.sub(r"(-[a-zA-Z]{6})$", "", item) not in local_secret_keys
        ]

        for secret in orphaned_secrets:
            secret_record = self.remote_secrets[secret]
            self.secrets_client.delete_secret(
                SecretId=secret_record["ARN"], ForceDeleteWithoutRecovery=True
            )
            logger.info(f"Deleted orphaned secret {secret_record['ARN']}")

    @property
    def local_secrets(self) -> typing.Dict[str, Any]:
        if not hasattr(self, "_secrets"):
            self._secrets = {}
            if os.path.exists(self.secret_path):
                with open(self.secret_path) as file:
                    secrets = yaml.safe_load(file)
                if secrets:
                    self._secrets = secrets

        return self._secrets

    @property
    def local_values(self) -> typing.Dict[str, Any]:
        if not hasattr(self, "_values"):
            self._values = {}
            if os.path.exists(self.path):
                with open(self.path) as file:
                    values = yaml.safe_load(file)
                if values:
                    self._values = values

        return self._values

    @property
    def remote_secrets(self) -> typing.Dict[str, Any]:
        if not hasattr(self, "_remote_secrets"):
            self._remote_secrets = self.get_remote_secrets()

        return self._remote_secrets

    @property
    def remote_secret_records(self) -> typing.Dict[str, Any]:
        if not hasattr(self, "_remote_secrets"):
            self._remote_secrets = self.get_remote_secret_records()

        return self._remote_secrets

    @property
    def remote_ssm_parameters(self) -> typing.Dict[str, Any]:
        if not hasattr(self, "_remote_parameters"):
            self._remote_parameters = self.get_remote_ssm_parameters()

        return self._remote_parameters

    @property
    def remote_values(self) -> typing.Dict[str, Any]:
        if not hasattr(self, "_remote_values"):
            try:
                self._remote_values = self.fetch_from_s3(self.raw)
            except botocore.exceptions.ClientError as err:
                self.environment.manager.click.secho(err)
                self._remote_values = {}

        return self._remote_values

    def get_local_params(self):
        app_values = self.convert_flatten(self.local_values)
        app_secrets = self.convert_flatten(self.local_secrets)
        return {**app_values, **app_secrets}

    @property
    def cache_file_name(self):
        return os.path.join(self.cache_app_directory, f"{self.name}.yaml")

    @property
    def cache_app_directory(self):
        return os.path.join(self.cache_directory, self.environment.name)

    def get_cached_parameters(self, flatten=True):
        if self.cache_enabled is False:
            return None
        if not os.path.exists(self.cache_file_name):
            return None
        with open(self.cache_file_name) as cache_file_pointer:
            return json.load(cache_file_pointer)

    def get_remote_params(self, flatten=True):
        if not (parameters := self.get_cached_parameters(flatten)):
            if flatten:
                self.raw = False
                app_values = self.convert_flatten(self.remote_values)
                app_secrets = self.convert_flatten(self.remote_secrets)
            else:
                self.raw = True
                app_values = self.remote_values
                app_secrets = self.remote_secrets
            parameters = {**app_values, **app_secrets}
            if self.cache_enabled:
                self.save_to_cache(parameters)
        return parameters

    def save_to_cache(self, parameters):
        if not os.path.exists(self.cache_app_directory):
            os.makedirs(self.cache_app_directory)
        with open(self.cache_file_name, "w") as cache_file_pointer:
            json.dump(parameters, cache_file_pointer)
        return True

    def get_flattened_parameters(self) -> typing.Dict[str, Any]:
        return self.convert_flatten(self.local_values)

    def get_flattened_secrets(self) -> typing.Dict[str, Any]:
        return self.convert_flatten(self.local_secrets)

    def get_parameter_id(self, parameter):
        return f"/{self.get_secret_id(parameter)}"

    def get_secret_id(self, secret):
        return os.path.join("", self.environment.name, self.name, secret)

    def put_parameter(
        self, parameter_id, parameter_value, tags=None, type="String", overwrite=True
    ):
        print(f"Creating Parameter {parameter_id}")
        self.ssm_client.put_parameter(
            Name=parameter_id,
            Value=parameter_value,
            Type=type,
            Overwrite=overwrite,
        )
        if tags:
            self.ssm_client.add_tags_to_resource(
                ResourceType="Parameter", ResourceId=parameter_id, Tags=tags
            )

    def create_secret(self, Name, SecretString, Tags, ForceOverwriteReplicaSecret):
        print(f"Creating Secret {Name}")
        try:
            self.secrets_client.create_secret(
                Name=Name,
                SecretString=SecretString,
                Tags=[
                    {"Key": "Environment", "Value": self.environment.name},
                    {"Key": "App", "Value": self.name},
                ],
                ForceOverwriteReplicaSecret=True,
            )
        except self.secrets_client.exceptions.ResourceExistsException:
            self.secrets_client.update_secret(
                SecretId=Name,
                SecretString=SecretString,
            )

    def backoff_with_custom_exception(
        self,
        func,
        exception,
        message_prefix="",
        max_attempts=5,
        base_delay=1,
        max_delay=10,
        factor=2,
        *args,
        **kwargs,
    ):
        attempts = 0
        delay = base_delay

        while attempts < max_attempts:
            try:
                result = func(*args, **kwargs)
                return result  # Return result if successful
            except exception as e:
                print(f"{message_prefix} Attempt {attempts + 1} failed: {e}")
                attempts += 1
                if attempts == max_attempts:
                    raise  # If all attempts fail, raise the last exception

                # Backoff logic
                delay = min(delay * factor, max_delay)
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)

    def push_parameters(self):
        for parameter, value in self.get_flattened_parameters().items():
            parameter_value = str(value)
            if (
                value_size := sys.getsizeof(parameter_value)
            ) > 4096 or not parameter_value:
                self.environment.manager.click.secho(
                    f"Parameter: {parameter} value is too large to store ({value_size})"
                )
                continue
            parameter_id = self.get_parameter_id(parameter)
            self.backoff_with_custom_exception(
                self.put_parameter,
                exception=botocore.exceptions.ClientError,
                message_prefix=f"Creating/Updating parameter {parameter_id}",
                max_attempts=5,
                base_delay=1,
                max_delay=10,
                factor=2,
                parameter_id=parameter_id,
                parameter_value=parameter_value,
                tags=[
                    {"Key": "Environment", "Value": self.environment.name},
                    {"Key": "App", "Value": self.name},
                ],
            )

    def push_secrets(self):
        for secret, value in self.get_flattened_secrets().items():
            sec_val = str(value)
            if len(sec_val) == 0:
                sec_val = "__EMPTY__"
            secret_id = self.get_secret_id(secret)
            try:
                self.backoff_with_custom_exception(
                    self.create_secret,
                    exception=botocore.exceptions.ClientError,
                    message_prefix=f"Creating/Updating secret {secret_id}",
                    max_attempts=5,
                    base_delay=1,
                    max_delay=10,
                    factor=2,
                    Name=secret_id,
                    SecretString=sec_val,
                    Tags=[
                        {"Key": "Environment", "Value": self.environment.name},
                        {"Key": "App", "Value": self.name},
                    ],
                    ForceOverwriteReplicaSecret=True,
                )

            except Exception as err:
                logger.error(f"Failed to push secret {secret_id}")
                raise err
            self.environment.manager.click.secho(f"Pushed {secret_id}")

    def fetch_secret_value(self, secret):
        response = self.secrets_client.get_secret_value(SecretId=secret["ARN"])
        sec_val = response["SecretString"]
        if sec_val == "__EMPTY__":
            return ""
        return response["SecretString"]

    @property
    def remote_ssm_parameter_filters(self):
        return [
            {
                "Key": "Name",
                "Option": "Contains",
                "Values": [f"/{self.environment.name}/{self.name}"],
            }
        ]

    @property
    def remote_secret_filters(self):
        return [
            {"Key": "tag-key", "Values": ["Environment"]},
            {"Key": "tag-value", "Values": [self.environment.name]},
            {"Key": "tag-key", "Values": ["App"]},
            {"Key": "tag-value", "Values": [self.name]},
        ]

    def get_remote_ssm_parameters(self):
        paginator = self.ssm_client.get_paginator("describe_parameters")
        parameters = {}
        filters = self.remote_ssm_parameter_filters
        response = paginator.paginate(
            ParameterFilters=filters,
        )
        for page in response:
            for parameter in page["Parameters"]:
                parameter_key = os.path.split(parameter["Name"])[-1]
                # parameters.append(parameter_key)
                parameters[parameter_key] = parameter
        return parameters

    def get_remote_secrets(self) -> typing.Dict[str, str]:
        paginator = self.secrets_client.get_paginator("list_secrets")
        secrets = {}
        response = paginator.paginate(
            Filters=self.remote_secret_filters,
        )
        for page in response:
            for secret in page["SecretList"]:
                secret_key = os.path.split(secret["Name"])[-1]
                secrets[secret_key] = self.fetch_secret_value(secret)

        return secrets

    def get_remote_secret_records(self):
        paginator = self.secrets_client.get_paginator("list_secrets")
        secrets = {}
        response = paginator.paginate(
            Filters=self.remote_secret_filters,
        )
        for page in response:
            for secret in page["SecretList"]:
                secret_key = os.path.split(secret["Name"])[-1]
                secrets[secret_key] = secret

        return secrets

    def convert_flatten(self, d, parent_key="", sep="_"):
        items = []
        if isinstance(d, dict):
            for k, v in d.items():
                new_key = parent_key + sep + k if parent_key else k

                if isinstance(v, MutableMapping):
                    items.extend(self.convert_flatten(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
        return dict(items)


class BootstrapEnvironment:
    manager: BootstrapManager

    def __init__(
        self,
        name,
        path,
        manager: BootstrapManager,
        cache_enabled=True,
        cache_directory=os.path.join(str(Path.home()), ".croudtech-bootstrap", "cache"),
    ):
        self.name = name
        self.path = path
        self.manager = manager
        if self.path:
            self.copy_to_temp()
        self.cache_enabled = cache_enabled
        self.cache_directory = cache_directory

    @property
    def temp_dir(self):
        if not hasattr(self, "_temp_dir"):
            self._temp_dir = os.path.join(self.manager.temp_dir, self.name)
            os.mkdir(self._temp_dir)
        return self._temp_dir

    @property
    def apps(self) -> typing.Dict[str, BootstrapApp]:
        if not hasattr(self, "_apps"):
            self._apps = {}
            for file in os.listdir(self.path):
                absolute_path = os.path.join(self.path, file)
                app_name, file_extension = os.path.splitext(file)
                app_name, is_secret = os.path.splitext(app_name)

                if (
                    os.path.isfile(absolute_path)
                    and file_extension in [".yaml", ".yml"]
                    and not is_secret
                ):
                    self._apps[app_name] = BootstrapApp(
                        app_name,
                        absolute_path,
                        environment=self,
                        cache_enabled=self.cache_enabled,
                        cache_directory=self.cache_directory,
                    )
        return self._apps

    def copy_to_temp(self):
        for _app_name, app in self.apps.items():
            shutil.copy(app.path, self.temp_dir)


class BootstrapManager:
    _environments: dict[str, BootstrapEnvironment]

    def __init__(
        self,
        prefix,
        region,
        click,
        values_path,
        bucket_name,
        endpoint_url=AWS_ENDPOINT_URL,
    ):
        self.prefix = prefix
        self.region = region
        self.click = click
        self.values_path = values_path
        self.endpoint_url = endpoint_url
        self.bucket_name = bucket_name

    @property
    def s3_client(self) -> S3Client:
        if not hasattr(self, "_s3_client"):
            self._s3_client = boto3.client(
                "s3", region_name=self.region, endpoint_url=self.endpoint_url
            )
        return self._s3_client

    @property
    def ssm_client(self):
        if not hasattr(self, "_ssm_client"):
            self._ssm_client = boto3.client(
                "ssm", region_name=self.region, endpoint_url=self.endpoint_url
            )
        return self._ssm_client

    @property
    def secrets_client(self) -> SecretsManagerClient:
        if not hasattr(self, "_secrets_client"):
            self._secrets_client = boto3.client(
                "secretsmanager",
                region_name=self.region,
                endpoint_url=self.endpoint_url,
            )
        return self._secrets_client

    @property
    def values_path_real(self):
        return os.path.realpath(self.values_path)

    @property
    def temp_dir(self):
        if not hasattr(self, "_temp_dir"):
            self._temp_dir = tempfile.TemporaryDirectory("app-bootstrap")
        return self._temp_dir.name

    def initBootstrap(self):
        try:
            self.s3_client.create_bucket(
                ACL="private",
                Bucket=f"{self.bucket_name}",
                CreateBucketConfiguration={"LocationConstraint": self.region},
            )
        except self.s3_client.exceptions.BucketAlreadyOwnedByYou:
            self.click.secho(
                f"Already initialised with bucket {self.bucket_name}",
                bg="red",
                fg="white",
            )
        except self.s3_client.exceptions.BucketAlreadyExists:
            self.click.secho(
                f"Bucket {self.bucket_name} already exists but is not owned by you.",
                bg="red",
                fg="white",
            )
        except Exception as err:
            self.click.secho(f"S3 Client Error {err}", bg="red", fg="white")

    def put_config(self, delete_first):
        self.cleanup_ssm_parameters()
        self.cleanup_secrets()
        for _environment_name, environment in self.environments.items():
            for _app_name, app in environment.apps.items():
                # pass
                app.upload_to_s3()
                app.push_parameters()
                app.push_secrets()

    def cleanup_ssm_parameters(self):
        for _environment_name, environment in self.environments.items():
            for _app_name, app in environment.apps.items():
                app.cleanup_ssm_parameters()

    def cleanup_secrets(self):
        for _environment_name, environment in self.environments.items():
            for _app_name, app in environment.apps.items():
                app.cleanup_secrets()

    @property
    def environments(self) -> typing.Dict[str, BootstrapEnvironment]:
        if not hasattr(self, "_environments"):
            self._environments = {}
            for item in os.listdir(self.values_path_real):
                if os.path.isdir(os.path.join(self.values_path_real, item)):
                    if item not in self._environments:
                        self._environments[item] = BootstrapEnvironment(
                            item,
                            os.path.join(self.values_path_real, item),
                            manager=self,
                            cache_enabled=False,
                        )

        return self._environments

    def list_apps(self):
        paginator = self.s3_client.get_paginator("list_objects")
        response_iterator = paginator.paginate(
            Bucket=self.bucket_name,
        )
        items = {}
        for page in response_iterator:
            for item in page["Contents"]:
                envname, filename = item["Key"].split("/")
                if envname not in items:
                    items[envname] = []
                items[envname].append(os.path.splitext(filename)[0])
        return items
