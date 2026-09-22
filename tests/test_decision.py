import pytest

from presence.decision import should_surface
from presence.models import CandidateIntervention, Faculty


def test_high_relevance_surfaces():
    result = should_surface(
        candidate=CandidateIntervention(
            relevance=0.9,
            expired=False,
            urgent=False,
            cue_text="Interview — Tuesday",
            faculty=Faculty.WIT,
            attention_cost=0.2,
        )
    )

    assert result is True


def test_low_relevance_does_not_surface():
    result = should_surface(
        candidate=CandidateIntervention(
            relevance=0.6,
            expired=False,
            urgent=False,
            cue_text="Interview — Tuesday",
            faculty=Faculty.WIT,
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
            faculty=Faculty.WIT,
            attention_cost=0.2,
        )
    )

    assert result is True


def test_expired_does_not_surface():
    result = should_surface(
        candidate=CandidateIntervention(
            relevance=0.95,
            expired=True,
            urgent=True,
            cue_text="Interview — Tuesday",
            faculty=Faculty.WIT,
            attention_cost=0.2,
        )
    )

    assert result is False


def test_invalid_relevance_is_rejected():
    with pytest.raises(ValueError):
        CandidateIntervention(
            relevance=5.0,
            expired=False,
            cue_text="Interview",
            faculty=Faculty.WIT,
            attention_cost=0.2,
        )


def test_invalid_attention_cost_is_rejected():
    with pytest.raises(ValueError):
        CandidateIntervention(
            relevance=1.0,
            expired=False,
            cue_text="Interview",
            faculty=Faculty.WIT,
            attention_cost=-1.0,
        )
