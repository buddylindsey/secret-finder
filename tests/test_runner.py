import pytest
from secretfinder import SecertsEnv, providers
from unittest.mock import patch


@patch('secretfinder.providers.EnvironmentVariable.get')
def test_single_provider(mock_provider_get):
    mock_provider_get.return_value = 'blob'

    env = SecertsEnv(providers=providers.EnvironmentVariable)

    assert env.get('TEST_ENV_VAR') == 'blob'
