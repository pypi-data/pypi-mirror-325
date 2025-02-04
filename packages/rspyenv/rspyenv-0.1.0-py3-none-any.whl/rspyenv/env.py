import os
import logging


class EnvironmentManager:
    _cached_envs = {}
    _allowed_variables = set()

    @staticmethod
    def load_from_file(file_path: str, override: bool = False, fail_on_missing: bool = True):
        """
        Load environment variables from a file. Each line should be in the format: VAR=VALUE.

        Args:
            file_path (str): Path to the environment file.
            override (bool): Whether to override the existing environment variables.
            fail_on_missing (bool): Whether to throw an exception or log a warning when the file doesn't exist.
        """
        if not os.path.exists(file_path):
            if fail_on_missing:
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            logging.warning(f"Environment file {file_path} not found. Skipping loading.")
            return

        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    if key in EnvironmentManager._allowed_variables:
                        if override or key not in os.environ:
                            os.environ[key] = value
                            EnvironmentManager._cached_envs[key] = value
                    else:
                        logging.warning(f"Skipping unallowed environment variable {key}.")

    @staticmethod
    def register_allowed_variables(variables: list):
        """
        Register the allowed environment variables that can be accessed by the class.

        Args:
            variables (list): List of environment variable names that are allowed.
        """
        EnvironmentManager._allowed_variables.update(variables)

    @staticmethod
    def get_variable(name: str, default_value=None):
        """
        Get an environment variable, case-insensitive. Caches the result for future calls.

        Args:
            name (str): The name of the environment variable.
            default_value: The value to return if the environment variable is not set (default is None).

        Returns:
            The value of the environment variable or the default value.
        """
        # Case-insensitive access
        name = name.upper()  # Normalize to uppercase for case insensitivity.
        if name in EnvironmentManager._cached_envs:
            return EnvironmentManager._cached_envs[name]

        # First time access, try fetching from os.environ
        value = os.environ.get(name, default_value)
        if value is not None:
            EnvironmentManager._cached_envs[name] = value
        return value
