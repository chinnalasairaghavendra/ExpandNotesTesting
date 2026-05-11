import uuid
import pytest

@pytest.mark.api
def test_delete_note(notes_api):
    unique_title = f"DELETE-{uuid.uuid4()}"
    create_response = notes_api.create_note(
        unique_title,
        "Delete Description",
        "Work"
    )
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]
    delete_response = notes_api.delete_note(note_id)
    assert delete_response.status_code == 200
    get_response = notes_api.get_notes()
    notes = get_response.json()["data"]
    deleted_note = [
        note for note in notes
        if note["id"] == note_id
    ]
    assert len(deleted_note) == 0