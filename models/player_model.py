"""
Player Model for Tournament System
----------------------------------
This class represents a Player object used inside the tournament system.
It is intentionally separate from the player structure used in clubs.py
to avoid conflicts with the starter code.
"""

from dataclasses import dataclass


@dataclass
class Player:
    """
    Represents a chess player participating in a tournament.
    """
    name: str
    email: str
    chess_id: str
    birthdate: str

    def to_dict(self) -> dict:
        """
        Convert the Player object into a dictionary for JSON serialization.
        """
        return {
            "name": self.name,
            "email": self.email,
            "chess_id": self.chess_id,
            "birthdate": self.birthdate
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Create a Player object from a dictionary loaded from JSON.
        """
        return Player(
            name=data.get("name", ""),
            email=data.get("email", ""),
            chess_id=data.get("chess_id", ""),
            birthdate=data.get("birthdate", "")
        )

    def __str__(self):
        """
        Human-readable representation of the player.
        """
        return f"{self.name} ({self.chess_id})"
