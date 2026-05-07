import os
from datetime import datetime


def capture_screenshot(driver, test_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(file_path)
    return file_path