from presence.decision import should_surface


def test_high_relevance_surfaces():
    result = should_surface(0.9, False, False)

    assert result is True

def test_low_relevance_surfaces():
    result = should_surface(0.6, False, False)

    assert result is False

def test_urgent_surfaces():
    result = should_surface(0.6, False, True)

    assert result is True

def test_expired_surfaces():
    result = should_surface(0.95, True, True)

    assert result is False