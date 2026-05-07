from api.api_client import APIClient


class AuthAPI(APIClient):

    def login(self, email, password):

        payload = {
            "email": email,
            "password": password
        }

        response = self.post(
            "/users/login",
            payload
        )

        if response.status_code == 200:

            self.token = response.json()["data"]["token"]

        return response