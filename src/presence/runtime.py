from presence.acuity import contextualize_candidate
from presence.decision import choose_intervention
from presence.faculties import propose_engram, propose_orient
from presence.models import CandidateIntervention, ContextFrame


def collect_candidates(
    state: dict[str, str],
    context: ContextFrame,
) -> list[CandidateIntervention]:
    candidates = []

    engram_candidate = propose_engram(state, context)

    if engram_candidate is not None:
        candidates.append(engram_candidate)

    orient_candidate = propose_orient(state, context)

    if orient_candidate is not None:
        candidates.append(orient_candidate)

    return candidates


def run_decision_cycle(
    state: dict[str, str],
    context: ContextFrame,
) -> CandidateIntervention | None:
    candidates = collect_candidates(state, context)

    contextualized_candidates = []

    for candidate in candidates:
        contextualized_candidate = contextualize_candidate(candidate, context)
        contextualized_candidates.append(contextualized_candidate)

    return choose_intervention(contextualized_candidates)
