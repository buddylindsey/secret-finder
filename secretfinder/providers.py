import abc
import json
import logging
import os

import boto3

log = logging.getLogger(__name__)


class Provider():
    def __init__(self, raise_exception=False):
        self.raise_exception = raise_exception

    @abc.abstractmethod
    def get(self, name, default=None):
        pass


class EnvironmentVariable(Provider):
    def get(self, name, default=None):
        value = os.getenv(name, default=default)

        if value == default:
            log.warning("Environment Variable '%s' does not exist" % name)

        return value


class AWSProviderBase(Provider):
    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)
        self.client = boto3.client(service)


class AWSSecretsManager(AWSProviderBase):
    """
    Limited support for other text secrets.
    """
    def __init__(self, **kwargs):
        super().__init__('secretsmanager', **kwargs)

    def get(self, name, default=None):
        try:
            data = self.client.get_secret_value(SecretId=name)['SecretString']
            return json.loads(data)[name]
        except:
            if self.raise_exception:
                raise
            log.warning("Secrets Manager string '%s' does not exist" % name)
            return default           


class AWSSSM(AWSProviderBase):
    def __init__(self, **kwargs):
        super().__init__('ssm', **kwargs)

    def get(self, name, default=None):
        try:
            return self.client.get_parameter(
                Name=name, WithDecryption=True)['Parameter']['Value']
        except self.client.exceptions.ParameterNotFound:
            if self.raise_exception:
                raise
            log.warning("SSM parameter '%s' does not exist" % name)
            return default
