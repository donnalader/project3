class Player:
    def __init__(self, name, email, chess_id, birthday):
        self.name = name
        self.email = email
        self.chess_id = chess_id
        self.birthday = birthday

        # Required for tournaments
        self.points = 0

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "chess_id": self.chess_id,
            "birthday": self.birthday,
            "points": self.points
        }

    @staticmethod
    def from_dict(data):
        player = Player(
            name=data.get("name"),
            email=data.get("email"),
            chess_id=data.get("chess_id"),
            birthday=data.get("birthday")
        )
        player.points = data.get("points", 0)
        return player

    def __repr__(self):
        return (
            f"Player(name={self.name}, email={self.email}, "
            f"chess_id={self.chess_id}, birthday={self.birthday}, "
            f"points={self.points})"
        )
