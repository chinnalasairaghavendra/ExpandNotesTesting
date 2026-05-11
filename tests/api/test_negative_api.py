from api.notes_api import NotesAPI
from config.environment import env
import pytest 
API_URL=env.get("api_url")

@pytest.mark.api
def test_get_notes_invalid_token():
    api = NotesAPI(
        API_URL
    )
    api.token = "invalid_token"
    response = api.get_notes()
    assert response.status_code == 401

@pytest.mark.api
def test_delete_invalid_note(notes_api):
    response = notes_api.delete_note(
        "123456789"
    )
    assert response.status_code in [400, 404]

@pytest.mark.api
def test_create_note_missing_title(notes_api):
    response = notes_api.create_note(
        "",
        "Description",
        "Home"
    )
    assert response.status_code in [400, 422]

@pytest.mark.api
def test_create_note_missing_description(notes_api):
    response = notes_api.create_note(
        "Title",
        "",
        "Home"
    )
    assert response.status_code in [400, 422]