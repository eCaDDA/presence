from presence.faculties import propose_engram
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