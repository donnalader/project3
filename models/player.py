class Player:
    def __init__(self, name, email, chess_id, birthday):
        self.name = name
        self.email = email
        self.chess_id = chess_id
        self.birthday = birthday

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "chess_id": self.chess_id,
            "birthday": self.birthday
        }

    @staticmethod
    def from_dict(data):
        return Player(
            name=data.get("name"),
            email=data.get("email"),
            chess_id=data.get("chess_id"),
            birthday=data.get("birthday")
        )
