from __future__ import annotations

import pytest
import uvicorn

from src.server.runner import run
from src.app.basic_math import BasicMath


@pytest.fixture(scope="session")
def run_server():
    return run()

@pytest.fixture(scope="session")
def math_unit():
    return BasicMath()