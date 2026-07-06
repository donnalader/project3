from dataclasses import dataclass
from typing import Optional
from models.player import Player

@dataclass
class Match:
    player1: Player
    player2: Player
    result: Optional[str] = None  # "1", "2", "T" (tie)

    def set_result(self, result: str):
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
            "player1_id": self.player1.chess_id,
            "player2_id": self.player2.chess_id,
            "result": self.result
        }

    @staticmethod
    def from_dict(data, players):
        """
        players = the REAL list of Player objects from the tournament.
        We find the correct Player objects by chess_id.
        """

        p1 = next(p for p in players if p.chess_id == data["player1_id"])
        p2 = next(p for p in players if p.chess_id == data["player2_id"])

        match = Match(player1=p1, player2=p2, result=data.get("result"))
        return match

