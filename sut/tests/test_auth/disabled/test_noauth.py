def test_no_user(sut):

    result = sut.get()
    assert result == (200, "Data!")


def test_user(sut, user):

    result = sut.get(user)
    assert result == (400, "Error: Bad Request")
