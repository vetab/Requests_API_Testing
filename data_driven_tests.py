import requests
import pytest
import csv

test_data_zip_code = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze")
]

def read_testing_data_from_csv():
    test_data = []
    with open('data/test_data_for_test_driven_tests.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter= ',')
        next(data)
        for row in data:
            test_data.append(row)
    return test_data


#Test which uses data from test_data_zip_code within the main test file
@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_code )

def test_data_driven_using_data_object_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name

#Same test which uses csv placed outside of the main test file
@pytest.mark.parametrize("country_code, zip_code, expected_place_name", read_testing_data_from_csv())

def test_data_driven_using_csv_to_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name