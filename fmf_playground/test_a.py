import pytest

@pytest.fixture(scope='session', autouse=True)
def fixture_session():
    print(">fixture session")
    yield
    print("<fixture session")

@pytest.fixture(scope='module', autouse=True)
def fixture_module():
    print(">fixture module")
    yield
    print("<fixture module")

@pytest.fixture(scope='function', autouse=True)
def fixture_function():
    print(">fixture function")
    yield
    print("<fixture function")

@pytest.fixture(autouse=True)
def fixture_autouse():
    print(">fixture autouse")
    yield
    print("<fixture autouse")

def setup_module(module):
    print(">setup_module")

def teardown_module(module):
    print(">teardown_module")

@pytest.fixture
def setup_a():
    print(">setup_a")
    yield
    print("<teardown_a")

def setup_function(function):
    print(">setup_function")
    assert True

def teardown_function(function):
    print("<teardown_function")
    assert True

@pytest.fixture
def setup_finalizer(request):
    print(">setup_finalizer")

    def finalizer_a():
        print("<finalizer_a")

    def finalizer_b():
        print("<finalizer_b")

    request.addfinalizer(finalizer_a)
    request.addfinalizer(finalizer_b)

def test_a(setup_a, setup_finalizer):
    print(">test_a")
    assert True


def test_b():
    print(">test_b")
    assert True