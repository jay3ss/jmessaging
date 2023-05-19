import pytest

import jmessaging as jm


@pytest.fixture
def messenger():
    return jm.Messenger()