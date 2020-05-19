import requests

def test__check_status_code_equals_200_for_code_ch_1000():
    response = requests.get("http://api.zippopotam.us/ch/1000")
    assert response.status_code == 200

def test_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/ch/1000")
    assert response.headers["Content-Type"] == "application/json"

def test_country_equals_switzerland_for_post_code_1000():
    response = requests.get("http://api.zippopotam.us/ch/1000")
    response_body = response.json()
    assert response_body["country"] == "Switzerland"

def test_first_place_name_is_Lausanne_26():
    response = requests.get("http://api.zippopotam.us/ch/1000")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == 'Lausanne 26'
    assert response_body["places"][1]["longitude"] == "6.6987"