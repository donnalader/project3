from dataclasses import dataclass, field
from typing import List
from models.match import Match

@dataclass
class Round:
    round_number: int
    matches: List[Match] = field(default_factory=list)

    def add_match(self, match: Match):
        self.matches.append(match)

    def to_dict(self):
        return {
            "round_number": self.round_number,
            "matches": [m.to_dict() for m in self.matches]
        }

    @staticmethod
    def from_dict(data):
        matches = [Match.from_dict(m) for m in data.get("matches", [])]
        return Round(
            round_number=data["round_number"],
            matches=matches
        )

