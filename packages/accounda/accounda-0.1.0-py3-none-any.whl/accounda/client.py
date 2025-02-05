import requests


class AccoundaClient:
    """
    A client for interacting with the Accounda API.
    """

    def __init__(self, client_id, client_secret, url="https://api.accounda.com/v1/"):
        """
        Initialize the Accounda client.

        Args:
            client_id (str): Your Accounda client ID.
            client_secret (str): Your Accounda client secret.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.url = url
        self.access_token = None
        self.refresh_token = None

    def get_access_token(self):
        """
        Requests an access token from the Accounda API.

        Returns:
            str: The access token.

        Raises:
            Exception: If the request fails.
        """
        url = f"{self.url}token/"
        data = {'client_id': self.client_id, 'client_secret': self.client_secret}
        response = requests.post(url, data=data)
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens['access_token']
        self.refresh_token = tokens.get('refresh_token')
        return self.access_token

    def refresh_access_token(self):
        """
        Refresh the access token using the refresh endpoint.
        """
        if not self.refresh_token:
            raise Exception("Refresh token not available. Please obtain a new access token.")

        url = f"{self.url}token/refresh/"
        headers = {
            'Authorization': f'Bearer {self.refresh_token}',
            'Content-Type': 'application/json',
            'Client-ID': self.client_id
        }
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens['access_token']

    def validate_user(self, auth_id, token, extra_params=None):
        """
        Validate the user using the Accounda API.

        Args:
            auth_id (str): The user's authorization ID.
            token (str): The user's auth token.
            extra_params (dict, optional): Additional GET parameters.

        Returns:
            dict: User data if valid.

        Automatically refreshes the access token if it expires.
        """
        # Ensure an access token is available
        if not self.access_token:
            self.get_access_token()

        # Build the validation URL with optional parameters
        url = f'{self.url}user/validate/?auth_id={auth_id}'
        if extra_params:
            query_params = '&'.join(f'{key}={value}' for key, value in extra_params.items())
            url = f"{url}&{query_params}"

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'Client-ID': self.client_id,
            'Auth-Token': token
        }

        # Make the request and handle token expiration
        response = requests.get(url, headers=headers)
        if response.status_code == 401:  # Unauthorized, likely due to token expiration
            self.refresh_access_token()  # Refresh the token
            headers['Authorization'] = f'Bearer {self.access_token}'  # Update the header
            response = requests.get(url, headers=headers)  # Retry the request

        response.raise_for_status()
        return (response.status_code == 200), response.json()

    def get_user_information(self, auth_id, extra_params=None):
        """
        Retrieve the user information from the Accounda API.

        Args:
            auth_id (str): The user's authorization ID.

        Returns:
            dict: The user information if the request is successful.

        Raises:
            Exception: If the request to retrieve user information fails.
            :param auth_id:
            :param extra_params:
        """
        # Ensure an access token is available
        if not self.access_token:
            self.get_access_token()

        url = f'{self.url}user/information/?auth_id={auth_id}'
        if extra_params:
            query_params = '&'.join(f'{key}={value}' for key, value in extra_params.items())
            url = f"{url}&{query_params}"

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'Client-ID': self.client_id
        }

        # Make the request and handle token expiration
        response = requests.get(url, headers=headers)
        if response.status_code == 401:  # Unauthorized, likely due to token expiration
            self.refresh_access_token()  # Refresh the token
            headers['Authorization'] = f'Bearer {self.access_token}'  # Update the header
            response = requests.get(url, headers=headers)  # Retry the request

        response.raise_for_status()
        return response.json()
