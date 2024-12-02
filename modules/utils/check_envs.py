import os

def check_env_vars(required_vars: list):
    for var in required_vars:
        if var not in os.environ:
            raise EnvironmentError(f"Missing required environment variable: {var}")
