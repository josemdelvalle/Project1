import unittest
from flask import render_template
from pip._vendor import requests
from services.employee_service_impl import EmployeeServiceImpl
from models.employee_credentials import EmployeeCredentials


class TestEmployeeControllerImpl(unittest.TestCase):
    # def test_hello():
    #     response = requests.get('http://localhost:5000/hello')
    #     assert response.text == 'hello'

    def test_login(self):
        valid_login = {"userName": 'Jose', "password": 'Del Valle'}
        bad_login = {"userName": '', "password": ''}
        response = requests.post('http://localhost:5000/login', json=valid_login)
        body = response.json()
        print(body)
        assert body == ["Logged in!",1]
        response = requests.post('http://localhost:5000/login', json=bad_login)
        body = response.json()
        assert body == ["Invalid user name or password", 0]


if __name__ == '__main__':
    unittest.main()
