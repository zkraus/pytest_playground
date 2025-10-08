import pytest

from fixture_params.main import Sut

@pytest.fixture(params=['a', 'b'])
def sut(request):
    sut = Sut(request.param)
    return sut


def test_a(sut):
    result = sut.get()
    assert result == sut.a

@pytest.mark.parametrize('prefix', ['X', 'Y'])
def test_prefix(prefix, sut):
    result = sut.get_prefix(prefix)
    assert result == f'{prefix}{sut.a}'