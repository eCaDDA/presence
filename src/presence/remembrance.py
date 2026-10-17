from presence.models import ExperienceOutcome, StateDelta


def propose_remembrance_delta(
    outcome: ExperienceOutcome,
) -> StateDelta | None:
    
    if outcome.assisted_success and not outcome.unaided_success:
        delta = StateDelta(key="wearer.support_need", 
                           value=outcome.faculty.value,
                           source="remembrance",
                           confidence = 0.8,
                           )

        return delta
    else:
        return None