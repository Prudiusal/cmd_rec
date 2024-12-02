import pytest
# import os
from unittest import mock
from modules.utils.check_envs import check_env_vars  # Assuming check_env_vars is in config.py


def test_env_vars_exist(monkeypatch):
    # Mock environment variables
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    monkeypatch.setenv("WEBSOCKET_HOST", "localhost")
    monkeypatch.setenv("WEBSOCKET_PORT", "8765")
    required_vars = ["OPENAI_API_KEY", "WEBSOCKET_HOST", "WEBSOCKET_PORT"]

    try:
        check_env_vars(required_vars)  # Should not raise any errors
    except Exception as e:
        pytest.fail(f"check_env_vars raised an exception: {e}")

def test_env_vars_missing(monkeypatch):
    # Remove environment variables
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("WEBSOCKET_HOST", raising=False)
    monkeypatch.delenv("WEBSOCKET_PORT", raising=False)

    required_vars = ["OPENAI_API_KEY", "WEBSOCKET_HOST", "WEBSOCKET_PORT"]

    with pytest.raises(EnvironmentError, match="Missing required environment variable"):
        check_env_vars(required_vars)
