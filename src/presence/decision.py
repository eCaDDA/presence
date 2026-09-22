from presence.models import CandidateIntervention


def should_surface(candidate: CandidateIntervention) -> bool:
    if candidate.expired:
        return False

    return candidate.relevance >= 0.8 or candidate.urgent
