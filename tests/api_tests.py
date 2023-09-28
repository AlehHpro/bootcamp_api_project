import json
import unittest
import requests
from requests import ReadTimeout


class TestApi(unittest.TestCase):
    _BASE_URL = "https://reqres.in/api"
    _TIMEOUT = 3  # 3 seconds timeout for performance test

    def test_list_users(self):
        # setup
        url = f"{self._BASE_URL}/users"
        # action
        response = requests.get(url)

        # Way to print data in readable .json format
        # response_json = response.json()  # Parse JSON response
        # formatted_json = json.dumps(response_json, indent=4)  # Pretty-print JSON
        # print(formatted_json)  # Print formatted JSON

        # result
        assert response.status_code == 200

    def test_get_single_user(self):
        # setup
        url = f"{self._BASE_URL}/users/2"
        # action
        response = requests.get(url)
        # result
        assert response.status_code == 200

    def test_get_single_user_details(self):
        # setup
        url = f"{self._BASE_URL}/users/2"
        # action
        response = requests.get(url)
        # result
        assert response.status_code == 200
        assert response.json()["data"]["id"] == 2
        assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
        assert response.json()["data"]["first_name"] == "Janet"
        assert response.json()["data"]["last_name"] == "Weaver"

    def test_single_user_not_found(self):
        # setup
        url = f"{self._BASE_URL}/users/28"
        # action
        response = requests.get(url)
        # result
        assert response.status_code == 404

    def test_create_user(self):
        # setup
        post_url = f"{self._BASE_URL}/users"
        post_body = {
            "name": "John",
            "job": "Tester"
        }
        # action
        response = requests.post(url=post_url, json=post_body)
        # result
        assert response.status_code == 201
        assert response.json()["name"] == "John"
        assert response.json()["job"] == "Tester"
        assert int(response.json()["id"]) > 0
        assert response.json()["createdAt"] is not None

    def test_update_user(self):
        # setup
        url = f"{self._BASE_URL}/users/2"
        data = {
            "name": "John",
            "job": "Developer"
        }
        # action
        response = requests.put(url, json=data)
        # print(response.json())

        # result
        assert response.status_code == 200

    def test_delete_user(self):
        # setup
        url = f"{self._BASE_URL}/users/2"
        # action
        response = requests.delete(url)
        # result
        assert response.status_code == 204

    def test_register_successful(self):
        # setup
        url = f"{self._BASE_URL}/register"
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        # action
        response = requests.post(url, json=data)
        # result
        assert response.status_code == 200

    def test_register_unsuccessful(self):
        # setup
        url = f"{self._BASE_URL}/register"
        data = {
            "email": "duplicate@test.com",
            "password": "newPassword"
        }
        # action
        response = requests.post(url, json=data)
        # result
        assert response.status_code == 400

    def test_delayed_response(self):
        # setup
        url = f"{self._BASE_URL}/users?delay=3"
        # action
        response = requests.get(url, timeout=self._TIMEOUT)
        self.assertEqual(response.status_code, 200)

        # Way to handle the timeout gracefully, e.g., print a message
        # try:
        #     response = requests.get(url, timeout=self.timeout)
        #     self.assertEqual(response.status_code, 200)
        # except ReadTimeout:
        #     # Handle the timeout gracefully, e.g., print a message
        #     print("The request timed out but we're handling it gracefully.")


if __name__ == '__main__':
    unittest.main()
