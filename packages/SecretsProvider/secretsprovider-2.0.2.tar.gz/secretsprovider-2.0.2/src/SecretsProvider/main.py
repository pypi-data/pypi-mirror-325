import dotenv
import getpass


class SecretsProvider:
    def __init__(self, input_func=getpass.getpass, env_path=".env"):
        """Saves and retrieves secrets

        Args:
            input_func: Controls how input from the user is asked when creating a new secret.
            By default, the user is asked for input.
            env_path: The path of the file where the secrets are stored.
        """
        self.get_input = input_func
        self.env_path = env_path

    def set_secret(self, secret_name: str):
        """Saves a secret.
        If there is already a secret with the name given. Entering a new value will overwrite the existing secret.
        """
        current_secret_value: str = dotenv.get_key(self.env_path, secret_name)
        if current_secret_value:
            print(f"\nThere is already a secret named {secret_name} stored as {secret_name}."
                  f"Entering a new value will overwrite the existing secret.")
        new_secret_value = self._request_secret_value()
        self._store_secret(secret_name, new_secret_value)

    def get_secret(self, secret_name: str) -> str:
        """Retrieves secret
        If this secret does not exist, it prompts the user to enter a secret and stores that.
        """
        secret_value = dotenv.get_key(self.env_path, secret_name)
        if not secret_value:
            print(f"\nA secret with name {secret_name} is not yet stored in {self.env_path}.")
            secret_value = self._request_secret_value()
            self._store_secret(secret_name, secret_value)
        return secret_value

    def remove_secret(self, secret_name: str) -> None:
        """Remove a secret"""
        dotenv.unset_key(self.env_path, secret_name)

    def print_secrets(self) -> None:
        """Prints all secrets stored in the file in the env_path location."""
        stored_secrets = dotenv.dotenv_values(self.env_path)
        if stored_secrets:
            print(f"\nThere are {len(stored_secrets)} secret(s) stored: {stored_secrets}")
        else:
            print(f"\nNothing is stored in the file {self.env_path}")

    def _request_secret_value(self) -> str:
        return self.get_input("Enter your Secret: ")

    def _store_secret(self, secret_name: str, secret_value: str) -> None:
        if secret_value.strip():
            dotenv.set_key(self.env_path, secret_name, secret_value)
            print(f"\nSecret has been stored: {secret_name}.")
        else:
            print("\nNo value entered for the secret. Not storing.")
