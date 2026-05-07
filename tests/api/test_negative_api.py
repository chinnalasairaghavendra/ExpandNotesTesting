from api.notes_api import NotesAPI
from config.environment import env

API_URL=env.get("api_url")
def test_get_notes_invalid_token():
    api = NotesAPI(
        API_URL
    )
    api.token = "invalid_token"
    response = api.get_notes()
    assert response.status_code == 401


def test_delete_invalid_note(notes_api):
    response = notes_api.delete_note(
        "123456789"
    )
    assert response.status_code in [400, 404]


def test_create_note_missing_title(notes_api):
    response = notes_api.create_note(
        "",
        "Description",
        "Home"
    )
    assert response.status_code in [400, 422]


def test_create_note_missing_description(notes_api):
    response = notes_api.create_note(
        "Title",
        "",
        "Home"
    )
    assert response.status_code in [400, 422]