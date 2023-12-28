import requests
import pytest
import logging
import allure
import os
from faker import Faker
from time import sleep
from unittest import TestCase

current_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join('../logs', 'app.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO)
logger = logging.getLogger(__name__)
fake = Faker()

sleep(2)

class BasePytest(TestCase):
    host_url = "http://localhost:3000"

    headers = {'Content-Type': 'application/json'}

    def send_request(self, method, url, data=None):
        with allure.step(f"{method} : {url}"):
            match (method):
                case "POST":
                    response = requests.post(f"{self.host_url}/{url}", json=data, headers=self.headers)
                case "GET":
                    response = requests.get(f"{self.host_url}/{url}", headers=self.headers)
                case "PUT":
                    response = requests.put(f"{self.host_url}/{url}", json=data, headers=self.headers)
                case "DELETE":
                    response = requests.delete(f"{self.host_url}/{url}", headers=self.headers)
                case _:
                    logger.error(f"Unsupported: {method}")
                    raise ValueError(f"Unsupported: {method}")  
                
            logger.info(f"{method} Response: {response.text}")
            return response

class APITests(BasePytest):

    @allure.feature("Users block")
    @allure.title("Create User")
    def test_01_create_user(self):
        user_data = {"name": fake.name()}
        with allure.step(f"Sending a POST request to create a user with data: {user_data}"):
            response = self.send_request('POST', 'users', user_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 201)

    @allure.feature("Users block")
    @allure.title("Read User")
    def test_02_read_user(self):
        with allure.step("Sending a GET request to read a user"):
            response = self.send_request('GET', 'users/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Users block")
    @allure.title("Update User")
    def test_03_update_user(self):
        user_data = {"name": fake.name()}
        with allure.step(f"Sending a PUT request to update a user with data: {user_data}"):
            response = self.send_request('PUT', 'users/1', user_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Users block")
    @allure.title("Delete User")
    def test_04_delete_user(self):
        with allure.step("Sending a DELETE request to delete a user"):
            response = self.send_request('DELETE', 'users/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Posts block")
    @allure.title("Create Post")
    def test_05_create_post(self):
        post_data = {"text": fake.text(), "date": fake.iso8601()}
        with allure.step(f"Sending a POST request to create a post with data: {post_data}"):
            response = self.send_request('POST', 'posts', post_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 201)

    @allure.feature("Posts block")
    @allure.title("Read Post")
    def test_06_read_post(self):
        with allure.step("Sending a GET request to read a post"):
            response = self.send_request('GET', 'posts/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Posts block")
    @allure.title("Update Post")
    def test_07_update_post(self):
        post_data = {"text": fake.text(), "date": fake.iso8601()}
        with allure.step(f"Sending a PUT request to update a post with data: {post_data}"):
            response = self.send_request('PUT', 'posts/1', post_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Posts block")
    @allure.title("Delete Post")
    def test_08_delete_post(self):
        with allure.step("Sending a DELETE request to delete a post"):
            response = self.send_request('DELETE', 'posts/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Orders block")
    @allure.title("Create Order")
    def test_09_create_order(self):
        order_data = {"amount": fake.random_number(4), "positions": fake.random_number(2)}
        with allure.step(f"Sending a POST request to create an order with data: {order_data}"):
            response = self.send_request('POST', 'orders', order_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 201)

    @allure.feature("Orders block")
    @allure.title("Read Order")
    def test_10_read_order(self):
        with allure.step("Sending a GET request to read an order"):
            response = self.send_request('GET', 'orders/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Orders block")
    @allure.title("Update Order")
    def test_11_update_order(self):
        order_data = {"amount": fake.random_number(4), "positions": fake.random_number(2)}
        with allure.step(f"Sending a PUT request to update an order with data: {order_data}"):
            response = self.send_request('PUT', 'orders/1', order_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Orders block")
    @allure.title("Delete Order")
    def test_12_delete_order(self):
        with allure.step("Sending a DELETE request to delete an order"):
            response = self.send_request('DELETE', 'orders/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Vehicle block")
    @allure.title("Create Vehicle")
    def test_13_create_vehicle(self):
        vehicle_data = {"name": fake.company(), "price": fake.random_number(5)}
        with allure.step(f"Sending a POST request to create a vehicle with data: {vehicle_data}"):
            response = self.send_request('POST', 'vehicle', vehicle_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 201)

    @allure.feature("Vehicle block")
    @allure.title("Read Vehicle")
    def test_14_read_vehicle(self):
        with allure.step("Sending a GET request to read a vehicle"):
            response = self.send_request('GET', 'vehicle/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Vehicle block")
    @allure.title("Update Vehicle")
    def test_15_update_vehicle(self):
        vehicle_data = {"name": fake.company(), "price": fake.random_number(5)}
        with allure.step(f"Sending a PUT request to update a vehicle with data: {vehicle_data}"):
            response = self.send_request('PUT', 'vehicle/1', vehicle_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Vehicle block")
    @allure.title("Delete Vehicle")
    def test_16_delete_vehicle(self):
        with allure.step("Sending a DELETE request to delete a vehicle"):
            response = self.send_request('DELETE', 'vehicle/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Colors block")
    @allure.title("Create Color")
    def test_17_create_color(self):
        color_data = {"color": fake.hex_color()}
        with allure.step(f"Sending a POST request to create a color with data: {color_data}"):
            response = self.send_request('POST', 'colors', color_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 201)

    @allure.feature("Colors block")
    @allure.title("Read Color")
    def test_18_read_color(self):
        with allure.step("Sending a GET request to read a color"):
            response = self.send_request('GET', 'colors/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Colors block")
    @allure.title("Update Color")
    def test_19_update_color(self):
        color_data = {"color": fake.hex_color()}
        with allure.step(f"Sending a PUT request to update a color with data: {color_data}"):
            response = self.send_request('PUT', 'colors/1', color_data)
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)

    @allure.feature("Colors block")
    @allure.title("Delete Color")
    def test_20_delete_color(self):
        with allure.step("Sending a DELETE request to delete a color"):
            response = self.send_request('DELETE', 'colors/1')
        allure.attach(str(response.json()), name="Response")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    pytest.main(args=["-s", __file__])