from presence.models import Activity, CandidateIntervention, ContextFrame, Faculty


def score_contextual_relevance(
    candidate: CandidateIntervention,
    context: ContextFrame,
) -> float:
    relevance = candidate.relevance

    if (
        candidate.faculty is Faculty.ENGRAM
        and context.activity is Activity.CONVERSATION
    ):
        relevance -= 0.4

    return max(0.0, relevance)
