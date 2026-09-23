from presence.models import Activity, CandidateIntervention, ContextFrame, Faculty


def propose_engram(
    state: dict[str, str],
    context: ContextFrame,
) -> CandidateIntervention | None:
    if context.activity is not Activity.STUDYING:
        return None

    topic = state.get("wearer.study_topic")

    if topic is None:
        return None

    return CandidateIntervention(
        relevance=0.9,
        expired=False,
        cue_text=f"Review {topic}",
        faculty=Faculty.ENGRAM,
        attention_cost=0.2,
    )