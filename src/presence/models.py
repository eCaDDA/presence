from dataclasses import dataclass
from enum import Enum


class Faculty(Enum):
    WIT = "wit"
    ENGRAM = "engram"
    ORIENT = "orient"
    SERENDIPITY = "serendipity"


class Activity(Enum):
    CONVERSATION = "conversation"
    STUDYING = "studying"
    WALKING = "walking"


@dataclass
class ContextFrame:
    activity: Activity


@dataclass
class CandidateIntervention:
    relevance: float
    expired: bool
    cue_text: str
    faculty: Faculty
    attention_cost: float
    urgent: bool = False

    def __post_init__(self):
        if not 0.0 <= self.relevance <= 1.0:
            raise ValueError("relevance must be between 0.0 and 1.0")

        if not 0.0 <= self.attention_cost <= 1.0:
            raise ValueError("attention_cost must be between 0.0 and 1.0")
