import json
import unittest
import requests
from requests import ReadTimeout


class TestApi(unittest.TestCase):
    base_url = "https://reqres.in/api"
    timeout = 3  # 3 seconds timeout for performance test

    def test_list_users(self):
        # setup
        url = f"{self.base_url}/users"
        # action
        response = requests.get(url)
        response_json = response.json()  # Parse JSON response
        formatted_json = json.dumps(response_json, indent=4)  # Pretty-print JSON
        print(formatted_json)  # Print formatted JSON
        # result
        assert response.status_code == 200

    def test_get_single_user(self):
        # setup
        url = f"{self.base_url}/users/2"
        # action
        response = requests.get(url)
        # result
        assert response.status_code == 200

    def test_get_single_user_details(self):
        # setup
        url = f"{self.base_url}/users/2"
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
        url = f"{self.base_url}/users/28"
        # action
        response = requests.get(url)
        # result
        assert response.status_code == 404

    def test_create_user(self):
        # setup
        post_url = f"{self.base_url}/users"
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
        url = f"{self.base_url}/users/2"
        data = {
            "name": "John",
            "job": "Developer"
        }
        # action
        response = requests.put(url, json=data)
        print(response.json())
        # result
        assert response.status_code == 200

    def test_delete_user(self):
        # setup
        url = f"{self.base_url}/users/2"
        # action
        response = requests.delete(url)
        # result
        assert response.status_code == 204

    def test_register_successful(self):
        # setup
        url = f"{self.base_url}/register"
        data = {
            "email": "newEmail@test.com",
            "password": "newPassword"
        }
        # action
        response = requests.post(url, json=data)
        # result
        assert response.status_code == 400

    def test_register_unsuccessful(self):
        # setup
        url = f"{self.base_url}/register"
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
        url = f"{self.base_url}/users?delay=3"
        # action
        try:
            response = requests.get(url, timeout=self.timeout)
            assert response.status_code == 200
        except ReadTimeout:
            # Handle the timeout gracefully
            self.fail("Request timed out. The response took longer than expected.")


if __name__ == '__main__':
    unittest.main()
