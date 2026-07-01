class TournamentManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tournaments = []
        return cls._instance

    def add(self, tournament):
        self.tournaments.append(tournament)
