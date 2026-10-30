from presence.models import CandidateIntervention


def should_surface(
    candidate: CandidateIntervention,
) -> bool:
    if candidate.expired:
        return False

    return candidate.relevance >= 0.8 or candidate.urgent


def get_eligible_candidates(
    candidates: list[CandidateIntervention],
) -> list[CandidateIntervention]:
    eligible = []

    for candidate in candidates:
        if should_surface(candidate):
            eligible.append(candidate)

    return eligible


def choose_intervention(
    candidates: list[CandidateIntervention],
) -> CandidateIntervention | None:
    winner = None

    for candidate in get_eligible_candidates(candidates):
        if winner is None or candidate.relevance > winner.relevance:
            winner = candidate

    return winner
