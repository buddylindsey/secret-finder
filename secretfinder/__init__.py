"""
This module is callable via the command line
but importing it does nothing
"""
from collections.abc import Iterable

from .providers import EnvironmentVariable

class SecertsEnv:
    def __init__(self, providers=EnvironmentVariable, raise_exception=False):
        self.raise_exception = raise_exception
        self.providers = providers

    def get(self, name, default=None):
        if not isinstance(self.providers, Iterable):
            return self.providers(raise_exception=self.raise_exception).get(name, default=default)

        for provider in self.providers:
            value = provider(raise_exception=self.raise_exception).get(name, default=default)

            if value == default:
                continue

            return value

        return default


