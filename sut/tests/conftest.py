import pytest
from sut.Sut import Sut


@pytest.fixture(scope="module")
def sut():
    sut = Sut()
    return sut


@pytest.fixture(scope="module")
def user():
    return "guest"


@pytest.fixture(scope="module")
def sut_auth_enabled(sut):
    sut.enable_authorization()
    return sut


@pytest.fixture(scope="module")
def sut_auth_enabled_user_existing(sut_auth_enabled, user):
    sut_auth_enabled.add_user(user)
    return sut_auth_enabled


@pytest.fixture(scope="module")
def sut_auth_disabled_user_existing(sut, user):
    sut.add_user(user)
    return sut
