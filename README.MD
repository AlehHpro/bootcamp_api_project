# API Test Automation README

This repository contains automated API tests for the ReqRes.in API using Python 3, pipenv, unittest, and the requests library.

## Prerequisites

Before you can run the tests, make sure you have the following installed:

- Python 3: You can download it from the [Python website](https://www.python.org/downloads/).
- pipenv: You can install it using pip with the following command:

  ```bash
  pip install pipenv

# Installation
## Clone the repository:
-```git clone git@github.com:AlehHpro/bootcamp_api_project.git```   

  cd */bootcamp_api_project

## Create a virtual environment and install dependencies:
-```pipenv --python 3```  
-```pipenv install```

## Navigate to api_tests.py file and install missing packages ('requests') by
## clicking highlighted rows.

# Running Tests

1. Open your terminal.

2. Navigate to the directory where your Python API tests are located using the `cd` command. For example:

   ```bash
   cd */bootcamp_api_project/tests

3. To run the automated API tests, use the following command:
   ```bash
   python -m unittest api_tests

# Test Cases
## The following API test cases are included:

1. List Users - test_list_users
2. Single User - test_get_single_user
3. Single User - test_get_single_user_details
4. Single User Not Found - test_single_user_not_found
5. Create User - test_create_user
6. Update User - test_update_user
7. Delete User - test_delete_user
8. Register (Successful) - test_register_successful
9. Register (Unsuccessful) - test_register_unsuccessful
10. Delayed Response - test_delayed_response

## Configuration  
You can configure the following options in api_tests.py:

-`base_url:` The base URL of the ReqRes.in API.  
-`timeout:` The timeout in seconds for API requests (default is 3 seconds).
