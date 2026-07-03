from dataclasses import dataclass
from typing import Optional
from models.player import Player

@dataclass
class Match:
    player1: Player
    player2: Player
    result: Optional[str] = None  # "1", "2", "T" (tie)

    def set_result(self, result: str):
        """
        Set the result of the match.
        result = "1" → player1 wins
        result = "2" → player2 wins
        result = "T" → tie
        """
        self.result = result

        if result == "1":
            self.player1.points += 1
        elif result == "2":
            self.player2.points += 1
        elif result == "T":
            self.player1.points += 0.5
            self.player2.points += 0.5

    def to_dict(self):
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "result": self.result
        }

    @staticmethod
    def from_dict(data):
        p1 = Player.from_dict(data["player1"])
        p2 = Player.from_dict(data["player2"])
        match = Match(player1=p1, player2=p2, result=data.get("result"))
        return match

