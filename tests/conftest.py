import pytest

@pytest.fixture
def in_ring_message() -> str:
    return "Точка находится в области."

@pytest.fixture
def out_of_ring_message() -> str:
    return "Точка вне области."
