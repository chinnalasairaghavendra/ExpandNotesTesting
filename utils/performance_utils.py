class PerformanceUtils:

    @staticmethod
    def get_page_load_time(driver):

        navigation_start = driver.execute_script(
            "return performance.timing.navigationStart"
        )

        load_event_end = driver.execute_script(
            "return performance.timing.loadEventEnd"
        )

        return (
            load_event_end - navigation_start
        ) / 1000