import pytest

@pytest.fixture
def in_ring_message() -> str:
    return "Точка находится в кольце."

@pytest.fixture
def out_of_ring_message() -> str:
    return "Точка вне кольца."
