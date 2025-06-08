import hashlib
import inspect
import logging
import os

import allure
import allure_commons
import pytest
from _pytest.config import UsageError
from slugify import slugify

from clients.mail_client import MailClient


@pytest.fixture(scope="function")
def mail_client():
    return MailClient()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,  # default = headed
        help="Run browser in headless mode (default: False)",
    )
    parser.getgroup("logging").addoption(
        "--allure-step-log-level",
        dest="allure_step_log_level",
        default="debug",
        metavar="ALLURE_STEP_LEVEL",
        help="Level of allure.step log messages. 'DEBUG' by default."
    )


@pytest.fixture(scope="session")
def browser_type_launch_args(pytestconfig, browser_type_launch_args):
    headless = pytestconfig.getoption("--headless")

    options = {
        "headless": headless,
        'args': [
            '--ignore-certificate-errors',
            '--disable-extensions',
            '--disable-infobars',
            '--disable-notifications',
            '--disable-popup-blocking',
            '--no-default-browser-check',
            '--deny-permission-prompts',
            '--start-maximized'
        ]
    }
    return {**browser_type_launch_args, **options}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, request: pytest.FixtureRequest):
    is_headless = request.config.getoption("--headless")
    return {
        **browser_context_args,
        "base_url": request.config.getini("base_url"),
        "no_viewport": not is_headless,
        "viewport": {"width": 1920, "height": 1080} if is_headless else None
    }


@pytest.fixture(scope='function', autouse=True)
def add_artifacts_to_allure_teardown(request):
    """
    Make after step fixture for attach screenshot, video and trace.\n
    Use flags: --screenshot=only-on-failure --video=retain-on-failure --tracing=retain-on-failure --full-page-screenshot
    :param request:
    :return:
    """
    yield

    output_dir = request.config.getoption("--output")
    output_path = os.path.join(output_dir, truncate_file_name(slugify(request.node.nodeid)))

    ext = ("png", "webm", "zip")
    if not os.path.exists(output_path):
        return
    for file in os.listdir(output_path):
        if file.endswith(ext):
            allure.attach(
                open(os.path.join(output_path, file), 'rb').read(),
                name=f"{file}",
                extension=file.split('.')[-1]
            )


def truncate_file_name(file_name: str) -> str:
    if len(file_name) < 256:
        return file_name
    return f"{file_name[:100]}-{hashlib.sha256(file_name.encode()).hexdigest()[:7]}-{file_name[-100:]}"


class AllureStepLogger:
    def __init__(self, config):
        # Create a logger
        self.logger = logging.getLogger(self.__class__.__name__)

        # Get --allure-step-log-level value
        self.level = config.option.allure_step_log_level
        if isinstance(self.level, str):
            self.level = self.level.upper()
        # Get a level number by a level name
        try:
            self.level = int(getattr(logging, self.level, self.level))
        except ValueError as e:
            # Python logging does not recognise this as a logging level
            raise UsageError(
                "'{}' is not recognized as a logging level name for "
                "'{}'. Please consider passing the "
                "logging level num instead.".format(self.level, self.__class__.__name__)
            ) from e

    @allure_commons.hookimpl
    def start_step(self, uuid, title, params):
        """Add a hook implementation to log every step"""
        # get test_* function name from stack
        test_name = next((frame[3] for frame in inspect.stack() if frame[3].startswith("test_")), "Unknown test")
        # log a message using defined logger and log level
        self.logger.log(self.level, f"{test_name}: {title}")


def pytest_configure(config):
    """Register `allure_step_logger` plugin if `allure_pytest` plugin is registered."""
    if config.pluginmanager.getplugin('allure_pytest'):
        allure_commons.plugin_manager.register(AllureStepLogger(config), "allure_step_logger")

    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    if worker_id is not None:
        logging.basicConfig(
            format=config.getini("log_cli_format"),
            filename=f"tests_{worker_id}.log",
            level=config.getini("log_cli_level"),
        )
