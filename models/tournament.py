from dataclasses import dataclass, field
from typing import List
from .round import Round
from .player import Player


@dataclass
class Tournament:
    name: str
    venue: str
    start_date: str
    end_date: str
    total_rounds: int
    current_round: int = 0   # IMPORTANT: start at 0
    players: List[Player] = field(default_factory=list)
    rounds: List[Round] = field(default_factory=list)

    # -----------------------------
    # Player Management
    # -----------------------------
    def add_player(self, player: Player):
        """Register a player for the tournament."""
        if player.chess_id not in [p.chess_id for p in self.players]:
            self.players.append(player)

    # -----------------------------
    # Round Management
    # -----------------------------
    def add_round(self, round_obj: Round):
        """Add a round to the tournament."""
        self.rounds.append(round_obj)

    def advance_round(self):
        """Move to the next round if possible."""
        if self.current_round < self.total_rounds:
            self.current_round += 1
        else:
            print("Tournament has already completed all rounds.")

    # -----------------------------
    # Reset Tournament
    # -----------------------------
    def reset(self):
        """
        Reset the tournament:
        - Clear all rounds
        - Reset current round to 0
        - Reset all player points
        """
        self.rounds = []
        self.current_round = 0

        for p in self.players:
            p.points = 0

    # -----------------------------
    # Serialization
    # -----------------------------
    def to_dict(self) -> dict:
        """Convert the Tournament into a dictionary for JSON saving."""
        return {
            "name": self.name,
            "venue": self.venue,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "total_rounds": self.total_rounds,
            "current_round": self.current_round,
            "players": [p.to_dict() for p in self.players],
            "rounds": [r.to_dict() for r in self.rounds]
        }

    @staticmethod
    def from_dict(data: dict):
        """Create a Tournament object from a dictionary loaded from JSON."""
        from .round import Round  # avoid circular import

        # Create tournament object
        tournament = Tournament(
            name=data["name"],
            venue=data["venue"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            total_rounds=data["total_rounds"],
            current_round=data.get("current_round", 0)
        )

        # Load players FIRST (real objects)
        tournament.players = [
            Player.from_dict(p)
            for p in data.get("players", [])
        ]

        # Load rounds using REAL players
        tournament.rounds = [
            Round.from_dict(r, tournament.players)
            for r in data.get("rounds", [])
        ]

        return tournament

    def __str__(self):
        return f"Tournament: {self.name} ({self.start_date} → {self.end_date})"
