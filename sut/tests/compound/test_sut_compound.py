def test_authorization(sut):

    user = 'guest'

    result = sut.get()
    assert result == (200, "Data!")

    result = sut.get(user)
    assert result == (400, "Error: Bad Request")

    sut.enable_authorization()

    result = sut.get(user)
    assert result == (401, "Error: Unauthorized")

    sut.add_user(user)

    result = sut.get(user)
    assert result == (200, "Data!")

    result = sut.get()
    assert result == (401, "Error: Unauthorized")
