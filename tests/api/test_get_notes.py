from utils.logger import get_logger

logger = get_logger(__name__)

def test_get_all_notes(notes_api):
    logger.info(
        "Starting test_get_all_notes"
    )
    response = notes_api.get_notes()
    logger.info(
        f"Response received: {response.status_code}"
    )
    assert response.status_code == 200
    data = response.json()["data"]
    assert isinstance(data, list)
    logger.info(
        "test_get_all_notes PASSED"
    )


def test_notes_response_time(notes_api):
    response = notes_api.get_notes()
    response_time = response.elapsed.total_seconds()
    assert response_time < 2