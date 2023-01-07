from sensor.exception import SensorException
from sensor.logger import logging
import sys,os

def test_logger_and_exception():
    try:
        logging.info("start")
        result = 3/0
        print(result)
    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        pass
    except Exception as e:
        print(e)