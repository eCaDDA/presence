from presence.faculties import propose_engram, propose_orient
from presence.models import Activity, ContextFrame, Faculty


def test_engram_proposes_study_topic_while_studying():
    state = {
        "wearer.study_topic": "gradient descent",
    }

    context = ContextFrame(
        activity=Activity.STUDYING,
    )

    result = propose_engram(state, context)

    assert result is not None
    assert result.faculty is Faculty.ENGRAM
    assert result.cue_text == "Review gradient descent"


def test_engram_does_not_propose_during_conversation():

    state = {
        "wearer.study_topic": "english literature",
    }

    context = ContextFrame(
        activity=Activity.CONVERSATION,
    )

    result = propose_engram(state, context)

    assert result is None


def test_orient_proposes_intention_while_walking():
    state = {
        "wearer.current_intention": "Buy milk",
    }

    context = ContextFrame(
        activity=Activity.WALKING,
    )

    result = propose_orient(state, context)

    assert result is not None
    assert result.faculty is Faculty.ORIENT
    assert result.cue_text == "Remember: Buy milk"


def test_orient_does_not_propose_without_intention():
    state = {}

    context = ContextFrame(
        activity=Activity.WALKING,
    )

    result = propose_orient(state, context)

    assert result is None
