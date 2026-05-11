import uuid
import json
import allure
import pytest
from utils.logger import get_logger


logger = get_logger(__name__)


@allure.epic("Hybrid E2E")
@allure.feature("API to UI Validation")
@allure.story("Delete Note via API and Validate in UI")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Validate API Deleted Note Is Removed From UI")
@allure.description(
    """
    This test validates that when a note is deleted
    through the API, the same note disappears
    from the UI after refresh.
    """
)
@allure.tag("E2E", "UI", "API", "Regression")

@pytest.mark.e2e
def test_api_deleted_note_removed_from_ui(
        notes_page,
        notes_api
):
    logger.info(
        "STARTING E2E TEST: API -> UI"
    )
    unique_title = f"DELETE-{uuid.uuid4()}"
    description = "Delete validation"
    allure.dynamic.parameter(
        "Note Title",
        unique_title
    )
    allure.dynamic.parameter(
        "Category",
        "Work"
    )
    with allure.step("Create note via UI"):
        logger.info(
            f"Creating note via UI | Title: {unique_title}"
        )
        notes_page.create_note(
            unique_title,
            description,
            "Work"
        )
        logger.info(
            "Note created successfully"
        )
    with allure.step("Validate note visible in UI"):
        assert notes_page.note_exists(unique_title)
        logger.info(
            "Note created and visible in UI"
        )
    with allure.step("Call GET /notes API"):
        response = notes_api.get_notes()
        logger.info(
            f"GET Notes Status: {response.status_code}"
        )
        assert response.status_code == 200
    with allure.step("Attach GET notes response"):
        allure.attach(
            json.dumps(response.json(), indent=4),
            name="GET Notes Response",
            attachment_type=allure.attachment_type.JSON
        )
    with allure.step("Locate created note ID from API response"):
        notes = response.json()["data"]
        note_id = None
        for note in notes:
            if (
                note["title"] == unique_title and
                note["description"] == description
            ):
                note_id = note["id"]
                break
        logger.info(
            f"Located Note ID: {note_id}"
        )
        allure.attach(
            str(note_id),
            name="Located Note ID",
            attachment_type=allure.attachment_type.TEXT
        )
        assert note_id is not None
    with allure.step("Delete note using DELETE API"):
        logger.info(
            f"Deleting note via API | ID: {note_id}"
        )
        delete_response = notes_api.delete_note(note_id)
        logger.info(
            f"Delete Status: {delete_response.status_code}"
        )
        allure.attach(
            delete_response.text,
            name="Delete API Response",
            attachment_type=allure.attachment_type.TEXT
        )
        assert delete_response.status_code == 200
    with allure.step("Refresh UI page"):
        logger.info(
            "Refreshing UI page"
        )
        notes_page.refresh_page()
    with allure.step("Validate deleted note removed from UI"):
        assert not notes_page.note_exists(unique_title)
        logger.info(
            "Deleted note removed from UI successfully"
        )
    logger.info(
        "E2E API -> UI validation PASSED"
    )