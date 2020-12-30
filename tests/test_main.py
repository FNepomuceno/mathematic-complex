from mathcplx import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client, captured_templates):
    response = client.get('/')

    assert response.status == '200 OK'
    assert len(captured_templates) == 1

    template, context = captured_templates[0]
    assert template.name == 'main/index.html'
