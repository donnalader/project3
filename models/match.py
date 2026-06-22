"""
Match Model
-----------
Represents a single match between two players in a round.
"""

from dataclasses import dataclass
from typing import Optional
from .player_model import Player


@dataclass
class Match:
    player1: Player
    player2: Player
    result: Optional[str] = None
    # result values:
    #   "1"   -> player1 wins
    #   "2"   -> player2 wins
    #   "T"   -> tie

    def set_result(self, result: str):
        """Set the match result."""
        if result not in ("1", "2", "T"):
            raise ValueError("Invalid result. Use '1', '2', or 'T'.")
        self.result = result

    def get_points(self):
        """Return a tuple of (player1_points, player2_points)."""
        if self.result == "1":
            return 1.0, 0.0
        if self.result == "2":
            return 0.0, 1.0
        if self.result == "T":
            return 0.5, 0.5
        return 0.0, 0.0  # no result yet

    def to_dict(self):
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "result": self.result
        }

    @staticmethod
    def from_dict(data):
        from .player_model import Player
        return Match(
            player1=Player.from_dict(data["player1"]),
            player2=Player.from_dict(data["player2"]),
            result=data.get("result")
        )

    def __str__(self):
        if self.result is None:
            return f"{self.player1} vs {self.player2} (pending)"
        return f"{self.player1} vs {self.player2} — Result: {self.result}"
