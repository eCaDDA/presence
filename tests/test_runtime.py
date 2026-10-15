from presence.models import Activity, ContextFrame, Faculty
from presence.runtime import collect_candidates, run_decision_cycle


def test_collect_candidates_while_studying():
    state = {
        "wearer.study_topic": "gradient descent",
        "wearer.current_intention": "Buy milk",
    }

    context = ContextFrame(
        activity=Activity.STUDYING,
    )

    result = collect_candidates(state, context)

    assert len(result) == 1
    assert result[0].faculty is Faculty.ENGRAM


def test_collect_candidates_while_walking():
    state = {
        "wearer.study_topic": "gradient descent:",
        "wearer.current_intention": "Buy milk",
    }

    context = ContextFrame(
        activity=Activity.WALKING,
    )

    result = collect_candidates(state, context)

    assert len(result) == 1
    assert result[0].faculty is Faculty.ORIENT


def test_decision_cycle_selects_engram_while_studying():
    state = {
        "wearer.study_topic": "gradient descent:",
        "wearer.current_intention": "Buy milk",
    }

    context = ContextFrame(
        activity=Activity.STUDYING,
    )

    result = run_decision_cycle(state, context)

    assert result.faculty is Faculty.ENGRAM


def test_decision_cycle_selects_orient_while_walking():
    state = {
        "wearer.study_topic": "gradient descent:",
        "wearer.current_intention": "Buy milk",
    }

    context = ContextFrame(
        activity=Activity.WALKING,
    )

    result = run_decision_cycle(state, context)

    assert result.faculty is Faculty.ORIENT


def test_decision_cycle_chooses_silence_during_conversation():
    state = {
        "wearer.study_topic": "gradient descent",
        "wearer.current_intention": "Buy milk",
    }

    context = ContextFrame(
        activity=Activity.CONVERSATION,
    )

    result = run_decision_cycle(state, context)

    assert result is None
