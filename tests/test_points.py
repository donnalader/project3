from models.player_model import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament

def main():
    # Create players
    p1 = Player("Alice", "alice@example.com", "AB12345", "1990-05-12")
    p2 = Player("Bob", "bob@example.com", "CD67890", "1988-03-22")
    p3 = Player("Carol", "carol@example.com", "EF54321", "1992-11-10")

    # Create matches
    m1 = Match(p1, p2, "1")   # Alice wins
    m2 = Match(p1, p3, "T")   # Tie
    m3 = Match(p2, p3, "2")   # Carol wins

    # Create rounds
    r1 = Round(1, [m1])
    r2 = Round(2, [m2, m3])

    # Create tournament
    t = Tournament(
        name="Test Tournament",
        venue="Test Venue",
        start_date="2024-01-01",
        end_date="2024-01-02",
        total_rounds=2,
        players=[p1, p2, p3],
        rounds=[r1, r2]
    )

    # Calculate points
    scores = {p.chess_id: 0 for p in t.players}

    for rnd in t.rounds:
        for match in rnd.matches:
            p1_pts, p2_pts = match.get_points()
            scores[match.player1.chess_id] += p1_pts
            scores[match.player2.chess_id] += p2_pts

    print("Final Scores:")
    for p in t.players:
        print(p.name, ":", scores[p.chess_id])

if __name__ == "__main__":
    main()
