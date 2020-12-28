from mathcplx import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.status == '200 OK'
    assert response.data == b'Hello, world!'
