from presence.decision import should_surface
from presence.models import CandidateIntervention


def test_high_relevance_surfaces():
    result = should_surface(
        candidate=CandidateIntervention(
            relevance=0.9,
            expired=False,
            urgent=False,
            cue_text="Interview — Tuesday",
            faculty="wit",
            attention_cost=0.2,
        )
    )

    assert result is True


def test_low_relevance_non_surfaces():
    result = should_surface(
        candidate=CandidateIntervention(
            relevance=0.6,
            expired=False,
            urgent=False,
            cue_text="Interview — Tuesday",
            faculty="wit",
            attention_cost=0.2,
        )
    )

    assert result is False


def test_urgent_surfaces():
    result = should_surface(
        candidate=CandidateIntervention(
            relevance=0.6,
            expired=False,
            urgent=True,
            cue_text="Interview — Tuesday",
            faculty="wit",
            attention_cost=0.2,
        )
    )

    assert result is True


def test_expired_surfaces():
    result = should_surface(
        candidate=CandidateIntervention(
            relevance=0.95,
            expired=True,
            urgent=True,
            cue_text="Interview — Tuesday",
            faculty="wit",
            attention_cost=0.2,
        )
    )

    assert result is False
