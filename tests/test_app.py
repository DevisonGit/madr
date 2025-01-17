from http import HTTPStatus

from fastapi.testclient import TestClient

from madr.app import app


def test_root_deve_retonar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola Mundo!'}
