"""
Round Model
-----------
Represents a round in a tournament, containing multiple matches.
"""

from dataclasses import dataclass, field
from typing import List
from .match import Match


@dataclass
class Round:
    round_number: int
    matches: List[Match] = field(default_factory=list)

    def add_match(self, match: Match):
        """Add a match to the round."""
        self.matches.append(match)

    def to_dict(self):
        return {
            "round_number": self.round_number,
            "matches": [m.to_dict() for m in self.matches]
        }

    @staticmethod
    def from_dict(data):
        from .match import Match
        return Round(
            round_number=data["round_number"],
            matches=[Match.from_dict(m) for m in data.get("matches", [])]
        )

    def __str__(self):
        return f"Round {self.round_number} — {len(self.matches)} matches"
