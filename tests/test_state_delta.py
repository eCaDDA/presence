import pytest

from presence.mentis import commit_state_delta, recall_fact, remember_fact
from presence.models import StateDelta


def test_state_delta_accepts_valid_confidence():
    state_delta = StateDelta(
        key="world.Tau.profession",
        value="robotics engineer",
        source="wearer",
        confidence=0.9,
    )

    assert state_delta.value == "robotics engineer"


def test_state_delta_rejects_invalid_confidence():
    with pytest.raises(ValueError):
        StateDelta(
            key="world.Tau.profession",
            value="robotics engineer",
            source="wearer",
            confidence=4.0,
        )


def test_state_delta_does_not_change_state_until_committed():
    state = {}

    remember_fact(
        state,
        "Tau.profession",
        "psychologist",
    )

    delta = StateDelta(
        key="Tau.profession",
        value="robotics engineer",
        source="wearer",
        confidence=1.0,
    )

    pre_state_delta = recall_fact(state, "Tau.profession")

    commit_state_delta(state, delta)

    post_state_delta = recall_fact(state, "Tau.profession")

    assert pre_state_delta == "psychologist"
    assert post_state_delta == "robotics engineer"
