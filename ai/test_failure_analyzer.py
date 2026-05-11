from failure_analyzer import (
    FailureAnalyzer
)
error = """
selenium.common.exceptions.TimeoutException:
Message:
"""
analysis = (
    FailureAnalyzer.analyze(error)
)
print(analysis)