from sut.Sut import Sut
import pytest


@pytest.fixture(scope="module")
def sut(user):
    sut = Sut()
    sut.enable_authorization()
    sut.add_user(user)
    return sut


@pytest.fixture(scope="module")
def user():
    return "guest"


def test_no_user(sut):

    result = sut.get()
    assert result == (401, "Error: Unauthorized")


def test_user(sut, user):

    result = sut.get(user)
    assert result == (200, "Data!")
