from __future__ import annotations

import pytest
import uvicorn

from src.server.echo_server import app
from src.app.basic_math import BasicMath


@pytest.fixture(scope="session")
def math_unit():
    return BasicMath()


@pytest.fixture(scope="session", autouse=True)
def collect_result():
    return []


@pytest.fixture(scope="session", autouse=True)
def publish_results():
    return []
