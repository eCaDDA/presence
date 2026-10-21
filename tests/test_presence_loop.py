from presence.mentis import recall_fact, remember_fact
from presence.models import Activity, ContextFrame, ExperienceOutcome, Faculty
from presence.runtime import process_experience_outcome, run_decision_cycle


def test_presence_loop_surfaces_help_and_records_remaining_support_need():
    state = {}

    remember_fact(
        state,
        key="wearer.study_topic",
        value="gradient descent",
    )

    context = ContextFrame(activity=Activity.STUDYING)

    result = run_decision_cycle(state, context)

    assert result is not None
    assert result.faculty is Faculty.ENGRAM
    assert result.cue_text == "Review gradient descent"

    outcome = ExperienceOutcome(
        faculty=Faculty.ENGRAM,
        assisted_success=True,
        unaided_success=False,
    )

    delta = process_experience_outcome(state, outcome)

    assert delta is not None
    assert delta.value == Faculty.ENGRAM.value
    assert delta.value == "engram"
    assert recall_fact(state, key="wearer.support_need") == Faculty.ENGRAM.value
    assert recall_fact(state, key="wearer.support_need") == "engram"
