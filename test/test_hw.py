from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_registration():
    email = "eve.holt@reqres.in"
    password = "qwerty"
    res = api.registrate_user(email, password)

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())


def test_not_correct_registration():
    email = "eve.holt@reqres.in"
    res = api.not_correct_registrate_user(email)
    res_body = res.json()
    example = {
        "error": "Missing password"
    }
    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res_body)
    assert example == res_body
