import uuid
import pytest

@pytest.mark.api
def test_create_note_api(notes_api):
    unique_title = f"API-{uuid.uuid4()}"
    response = notes_api.create_note(
        unique_title,
        "API Automation Description",
        "Home"
    )
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["title"] == unique_title