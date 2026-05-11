import uuid
import pytest

@pytest.mark.ui
def test_create_note_without_title(notes_page):
    notes_page.click_add_note()
    notes_page.enter_description("Missing title")
    notes_page.select_category("Home")
    notes_page.click_save()
    errors = notes_page.get_validation_errors()
    assert "title is required" in errors

@pytest.mark.ui
def test_create_note_without_description(notes_page):
    title = f"Negative-{uuid.uuid4()}"
    notes_page.click_add_note()
    notes_page.enter_title(title)
    notes_page.select_category("Work")
    notes_page.click_save()
    errors = notes_page.get_validation_errors()
    assert "description is required" in errors
