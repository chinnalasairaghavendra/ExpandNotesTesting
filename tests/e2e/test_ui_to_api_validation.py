import uuid
import json
import allure

from utils.logger import get_logger


logger = get_logger(__name__)


@allure.epic("Hybrid E2E")
@allure.feature("UI to API Validation")
@allure.story("Create Note in UI and Validate in API")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Validate UI Created Note Exists in API")
@allure.description(
    """
    This test validates that a note created through the UI
    is immediately available in the GET /notes API response.
    """
)
@allure.tag("E2E", "UI", "API", "Regression")
def test_ui_created_note_exists_in_api(
        notes_page,
        notes_api
):
    logger.info(
        "STARTING E2E TEST: UI -> API"
    )
    unique_title = f"E2E-{uuid.uuid4()}"
    description = "Hybrid UI API Validation"
    allure.dynamic.parameter(
        "Note Title",
        unique_title
    )
    allure.dynamic.parameter(
        "Category",
        "Home"
    )
    with allure.step("Create note via UI"):
        logger.info(
            f"Creating note from UI | Title: {unique_title}"
        )
        notes_page.create_note(
            unique_title,
            description,
            "Home"
        )
        logger.info(
            "Note creation completed"
        )

    with allure.step("Validate note visible immediately in UI"):
        assert notes_page.note_exists(unique_title)
        logger.info(
            "Note visible in UI successfully"
        )

    with allure.step("Call GET /notes API"):
        logger.info(
            "Calling GET /notes API"
        )
        response = notes_api.get_notes()
        logger.info(
            f"API Response Status: {response.status_code}"
        )
        assert response.status_code == 200

    with allure.step("Attach API response to report"):
        allure.attach(
            json.dumps(response.json(), indent=4),
            name="GET Notes API Response",
            attachment_type=allure.attachment_type.JSON
        )

    # with allure.step("Validate API response time < 2 seconds"):
    #     response_time = response.elapsed.total_seconds()
    #     logger.info(
    #         f"API Response Time: {response_time}"
    #     )
    #     allure.attach(
    #         str(response_time),
    #         name="API Response Time",
    #         attachment_type=allure.attachment_type.TEXT
    #     )
    #     assert response_time < 2
    with allure.step("Validate created note exists in API response"):
        notes = response.json()["data"]
        logger.info(
            f"Total Notes Returned: {len(notes)}"
        )
        matched_note = None
        for note in notes:
            if (
                note["title"] == unique_title and
                note["description"] == description
            ):
                matched_note = note
                break
        logger.info(
            f"Matched Note: {matched_note}"
        )
        allure.attach(
            json.dumps(matched_note, indent=4),
            name="Matched Note",
            attachment_type=allure.attachment_type.JSON
        )
        assert matched_note is not None
    logger.info(
        "E2E UI -> API validation PASSED"
    )