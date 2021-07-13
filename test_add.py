from add import adding


def test_always_passes():
    assert True


def test_adding():
    assert (5 == adding(2, 3))
    assert (10 == adding(2, 8))
    assert (0 == adding(0, 0))
