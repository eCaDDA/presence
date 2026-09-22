from dataclasses import dataclass


@dataclass
class CandidateIntervention:
    relevance: float
    expired: bool
    urgent: bool
    cue_text: str
    faculty: str
    attention_cost: float
