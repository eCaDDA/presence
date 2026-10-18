from presence.acuity import contextualize_candidate
from presence.decision import choose_intervention
from presence.faculties import propose_engram, propose_orient
from presence.mentis import commit_state_delta
from presence.models import (
    CandidateIntervention,
    ContextFrame,
    ExperienceOutcome,
    StateDelta,
)
from presence.remembrance import propose_remembrance_delta


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


def process_experience_outcome(
    state: dict[str, str],
    outcome: ExperienceOutcome,
) -> StateDelta | None:
    delta = propose_remembrance_delta(outcome)

    if delta is None:
        return None

    commit_state_delta(state, delta)

    return delta
