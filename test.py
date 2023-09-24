from app import app


def test_up():
    response = app.test_client().get('/')
    assert response.status_code == 200


# def test_home():
#     response = app.test_client().get('/home')
#     assert response.status_code == 200
#
#
# def test_list():
#     response = app.test_client().get('/list')
#     assert b'To Do App' in response.data
#
#
# def test_edit():
#     response = app.test_client().get('/edit')
#     assert b'Add' in response.data
