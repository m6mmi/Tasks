import json

from main import clean_line

headers = ['id', 'name', 'category', 'price', 'currency', 'stock', 'description', 'manufacturer', 'warranty',
           'extra_field']


def test_1_clean_line(data_1):
    assert clean_line(data_1, headers) == {'category': 'Appliances',
                                           'currency': 'USD',
                                           'description': 'Description of product 1',
                                           'extra_field': 'N/A',
                                           'id': '1',
                                           'manufacturer': 'CamTech',
                                           'name': 'Product 1',
                                           'price': 320.46,
                                           'stock': 51,
                                           'warranty': '2 years'}


def test_2_clean_line(data_2):
    assert clean_line(data_2, headers) == {'category': 'Wearables',
                                           'currency': 'USD',
                                           'description': 'Description of product 2',
                                           'extra_field': 'Extra value 2',
                                           'id': '2',
                                           'manufacturer': 'BrightLife',
                                           'name': 'Product 2',
                                           'price': 808.81,
                                           'stock': 127,
                                           'warranty': '1 year'}


def test_3_clean_line(data_3):
    assert clean_line(data_3, headers) == {'category': 'Accessories',
                                           'currency': 'USD',
                                           'description': 'N/A',
                                           'extra_field': 'N/A',
                                           'id': '7',
                                           'manufacturer': 'VirtuaWorld',
                                           'name': 'Product 7',
                                           'price': 341.36,
                                           'stock': 13,
                                           'warranty': '1 year'}
