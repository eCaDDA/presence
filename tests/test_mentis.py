from presence.mentis import recall_fact, remember_fact


def test_remember_and_recall_fact():
    state = {}

    remember_fact(
        state,
        "wearer.current_task",
        "conversation",
    )

    result = recall_fact(state, "wearer.current_task")

    assert result == "conversation"


def test_recall_missing_fact_returns_none():
    state = {}

    result = recall_fact(state, "wearer.favourite_planet")

    assert result is None


def test_remember_fact_can_update_existing_fact():
    state = {}

    remember_fact(state, "wearer.current_task", "conversation")
    remember_fact(state, "wearer.current_task", "walking")

    result = recall_fact(state, "wearer.current_task")

    assert result == "walking"
