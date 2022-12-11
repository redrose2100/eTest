import pytest
import logging
from .env import Env

@pytest.fixture(scope="session")
def env():
    return Env

@pytest.fixture(scope="session",autouse=True)
def session_setup_teardown():
    logging.info("开始执行session级别的setup ...")
    # session级的setup，可在下面继续编写session级别的setup操作

    yield
    logging.info("开始执行session级别的teardown ...")
    # session级别的teardown，可在下面继续编写session级别的teardown的操作
