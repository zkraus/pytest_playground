from sut.Sut import Sut
import pytest


@pytest.fixture(scope="module")
def sut():
    sut = Sut()
    sut.enable_authorization()
    return sut

@pytest.fixture(scope="module")
def user():
    return 'guest'


def test_no_user(sut):

    result = sut.get()
    assert result == (401, "Error: Unauthorized")

def test_user(sut,user):

    result = sut.get(user)
    assert result == (401, "Error: Unauthorized")
