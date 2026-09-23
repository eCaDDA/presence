from presence.acuity import score_contextual_relevance
from presence.models import (
    Activity,
    CandidateIntervention,
    ContextFrame,
    Faculty,
)


def test_engram_relevance_drops_during_conversation():
    candidate = CandidateIntervention(
        relevance=0.9,
        expired=False,
        cue_text="Review gradient descent",
        faculty=Faculty.ENGRAM,
        attention_cost=0.2,
    )

    context = ContextFrame(
        activity=Activity.CONVERSATION,
    )

    result = score_contextual_relevance(candidate, context)

    assert result == 0.5


def test_engram_relevance_stays_same_while_studying():
    candidate = CandidateIntervention(
        relevance=0.9,
        expired=False,
        cue_text="Review gradient descent",
        faculty=Faculty.ENGRAM,
        attention_cost=0.2,
    )

    context = ContextFrame(
        activity=Activity.STUDYING
    )

    result = score_contextual_relevance(candidate, context)

    assert result == 0.9