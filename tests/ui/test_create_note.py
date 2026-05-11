import uuid
import allure
import pytest
from ai.test_data_generator import (
    TestDataGenerator
)


@allure.epic("UI Automation")
@allure.feature("Create Notes")
@allure.story("Create Note Successfully")
@allure.title("Validate User Can Create Note")
@pytest.mark.ui
def test_create_note(notes_page):

    # AI-generated test data
    data = (
        TestDataGenerator.generate_note()
    )

    unique_title = (
        f"{data['title']}-{uuid.uuid4()}"
    )

    description = (
        data["description"]
    )

    category = (
        data["category"]
    )

    print("\n===== AI GENERATED TEST DATA =====\n")

    print(data)

    with allure.step(
        "Create note from UI using AI-generated data"
    ):

        notes_page.create_note(
            unique_title,
            description,
            category
        )

    with allure.step(
        "Validate note visible in UI"
    ):

        assert notes_page.note_exists(
            unique_title
        )


@allure.epic("UI Automation")
@allure.feature("DOM Validation")
@allure.story("Immediate UI Update")
@allure.title(
    "Validate Note Appears Immediately"
)
@pytest.mark.ui
def test_note_visible_immediately(notes_page):

    # Static data for stability
    unique_title = (
        f"Instant-{uuid.uuid4()}"
    )

    description = (
        "DOM validation"
    )

    category = (
        "Work"
    )

    with allure.step(
        "Create note using static test data"
    ):

        notes_page.create_note(
            unique_title,
            description,
            category
        )

    with allure.step(
        "Validate note visible immediately"
    ):

        assert notes_page.note_exists(
            unique_title
        )