from presence.models import ExperienceOutcome, Faculty
from presence.remembrance import propose_remembrance_delta


def test_remembrance_proposes_delta_when_assistance_has_not_transferred():
    outcome = ExperienceOutcome(
        faculty=Faculty.WIT,
        assisted_success=True,
        unaided_success=False,
    )

    result = propose_remembrance_delta(outcome)

    assert result is not None
    assert result.confidence == 0.8
    assert result.value == "wit"
    assert result.key == "wearer.support_need"
    assert result.source == "remembrance"


def test_remembrance_proposes_nothing_after_unaided_success():
    outcome = ExperienceOutcome(
        faculty=Faculty.WIT,
        assisted_success=True,
        unaided_success=True,
    )

    result = propose_remembrance_delta(outcome)

    assert result is None
