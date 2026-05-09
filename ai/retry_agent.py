import time

from selenium.common.exceptions import (

    StaleElementReferenceException,

    ElementClickInterceptedException,

    TimeoutException
)


class RetryAgent:

    RETRY_EXCEPTIONS = (

        StaleElementReferenceException,

        ElementClickInterceptedException,

        TimeoutException
    )

    @staticmethod
    def execute(

        action,

        retries=3,

        delay=2
    ):

        for attempt in range(retries):

            try:

                return action()

            except RetryAgent.RETRY_EXCEPTIONS as e:

                print(
                    f"\nRetry {attempt + 1} "
                    f"due to: {type(e).__name__}"
                )

                time.sleep(delay)

        raise Exception(
            "Retry attempts exhausted"
        )