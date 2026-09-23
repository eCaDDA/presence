import pytest

from presence.decision import (
    choose_intervention,
    get_eligible_candidates,
    should_surface,
)
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


def test_get_eligible_candidates_filters_candidates():
    candidates = [
        CandidateIntervention(
            relevance=0.9,
            expired=False,
            cue_text="Ask about her new job",
            faculty=Faculty.WIT,
            attention_cost=0.2,
        ),
        CandidateIntervention(
            relevance=0.6,
            expired=False,
            cue_text="Review gradient descent",
            faculty=Faculty.ENGRAM,
            attention_cost=0.4,
        ),
        CandidateIntervention(
            relevance=0.95,
            expired=True,
            cue_text="Ask Sam about the project",
            faculty=Faculty.ORIENT,
            attention_cost=0.1,
        ),
    ]

    result = get_eligible_candidates(candidates)

    assert len(result) == 1
    assert result[0].cue_text == "Ask about her new job"


def test_choose_intervention_returns_highest_relevance_candidate():
    candidates = [
        CandidateIntervention(
            relevance=0.82,
            expired=False,
            cue_text="Ask about her new job",
            faculty=Faculty.WIT,
            attention_cost=0.2,
        ),
        CandidateIntervention(
            relevance=0.95,
            expired=False,
            cue_text="Review gradient descent",
            faculty=Faculty.ENGRAM,
            attention_cost=0.4,
        ),
        CandidateIntervention(
            relevance=0.88,
            expired=True,
            cue_text="Ask Sam about the project",
            faculty=Faculty.ORIENT,
            attention_cost=0.1,
        ),
    ]

    winner = choose_intervention(candidates)

    assert winner.cue_text == "Review gradient descent"


def test_choose_intervention_returns_none_when_nothing_is_eligible():
    candidates = [
        CandidateIntervention(
            relevance=0.3,
            expired=False,
            cue_text="Ask about her new job",
            faculty=Faculty.WIT,
            attention_cost=0.2,
        ),
        CandidateIntervention(
            relevance=0.6,
            expired=False,
            cue_text="Review gradient descent",
            faculty=Faculty.ENGRAM,
            attention_cost=0.4,
        ),
        CandidateIntervention(
            relevance=0.79,
            expired=True,
            cue_text="Ask Sam about the project",
            faculty=Faculty.ORIENT,
            attention_cost=0.1,
        ),
    ]

    winner = choose_intervention(candidates)

    assert winner == None
