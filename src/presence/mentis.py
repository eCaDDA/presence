from presence.models import StateDelta


def remember_fact(
    state: dict[str, str],
    key: str,
    value: str,
) -> None:
    state[key] = value


def recall_fact(
    state: dict[str, str],
    key: str,
) -> str | None:
    return state.get(key)


def commit_state_delta(
    state: dict[str, str],
    delta: StateDelta,
) -> None:
    state[delta.key] = delta.value
