from models.match import Match

class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.matches = []

    def add_match(self, match):
        """Add a match to this round."""
        self.matches.append(match)

    def to_dict(self):
        return {
            "round_number": self.round_number,
            "matches": [m.to_dict() for m in self.matches]
        }

    @staticmethod
    def from_dict(data, players):
        round_obj = Round(data["round_number"])
        round_obj.matches = [
            Match.from_dict(m, players)
            for m in data.get("matches", [])
        ]
        return round_obj



