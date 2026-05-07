import time
import uuid
import allure

@allure.epic("UI Automation")
@allure.feature("Create Notes")
@allure.story("Create Note Successfully")
@allure.title("Validate User Can Create Note")
def test_create_note(notes_page):
    unique_title = f"Automation-{uuid.uuid4()}"
    description = "This is automation testing"
    with allure.step("Create note from UI"):
        notes_page.create_note(
            unique_title,
            description,
            "Home"
        )
    with allure.step("Validate note visible in UI"):
        assert notes_page.note_exists(unique_title)


def test_note_visible_immediately(notes_page):
    unique_title = f"Instant-{uuid.uuid4()}"
    notes_page.create_note(
        unique_title,
        "DOM validation",
        "Work"
    )
    assert notes_page.note_exists(unique_title)