import pytest


@pytest.fixture()
def set_up():
    print("\n--Start test--")
    yield
    print("\n--Finish test--")

@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")