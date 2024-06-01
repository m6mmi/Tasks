import pytest


@pytest.fixture
def data_1():
    return {
            "id": "1",
            "name": "Product 1",
            "category": "Appliances",
            "price": 320.46,
            "currency": "USD",
            "stock": 51,
            "description": "Description of product 1",
            "manufacturer": "CamTech",
            "warranty": "2 years",
            "extra_field": None
        }


@pytest.fixture
def data_2():
    return {
            "id": "2",
            "name": "Product 2",
            "category": "Wearables",
            "price": 808.81,
            "currency": "USD",
            "stock": 127,
            "description": "Description of product 2",
            "manufacturer": "BrightLife",
            "warranty": "1 year",
            "extra_field": "Extra value 2"
        }


@pytest.fixture
def data_3():
    return {
            "id": "7",
            "name": "Product 7",
            "category": "Accessories",
            "price": 341.36,
            "currency": "USD",
            "stock": 13,
            "manufacturer": "VirtuaWorld",
            "warranty": "1 year",
            "extra_field": None
        }
