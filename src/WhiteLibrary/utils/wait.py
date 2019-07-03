import time
from robot.utils import timestr_to_secs


class Wait:
    @staticmethod
    def until_true(condition, timeout, error_msg):
        """Helper to wait until given condition is met."""
        timeout = timestr_to_secs(timeout)
        max_wait = time.time() + timeout
        while True:
            if condition():
                break
            if time.time() > max_wait:
                raise AssertionError(error_msg)
            time.sleep(0.1)
