import json
import random
from commands.base import BaseCommand
from commands import NoopCmd
from models.round import Round
from models.match import Match


class TournamentGenerateRoundsCmd(BaseCommand):
    name = "tournament-generate-rounds"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):

        tournament = self.tournament
        index = self.tournament_index or kwargs.get("tournament_index")

        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd("tournament-actions")

        players = tournament.players

        if len(players) < 2:
            print("Not enough players to generate a round.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        # Determine round number
        round_number = len(tournament.rounds) + 1

        # Prevent generating past total rounds
        if round_number > tournament.total_rounds:
            print("All rounds have already been generated.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        # Prevent generating the same round twice
        if tournament.current_round >= round_number:
            print(f"Round {round_number} has already been generated.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        print(f"\nGenerating Round {round_number}...")

        # ---------------------------------------------------------
        # ROUND 1 → RANDOM PAIRINGS
        # ---------------------------------------------------------
        if round_number == 1:
            shuffled = players[:]  # shuffle a copy
            random.shuffle(shuffled)
            pairings = []

            for i in range(0, len(shuffled), 2):
                if i + 1 < len(shuffled):
                    pairings.append((shuffled[i], shuffled[i+1]))
                else:
                    # Odd number → bye
                    print(f"{shuffled[i].name} receives a bye (+1 point)")
                    shuffled[i].points += 1

        # ---------------------------------------------------------
        # ROUND 2+ → SORT BY POINTS
        # ---------------------------------------------------------
        else:
            sorted_players = sorted(players, key=lambda p: p.points, reverse=True)
            pairings = []
            used = set()

            for i in range(len(sorted_players)):
                if sorted_players[i] in used:
                    continue

                # Find next available opponent
                for j in range(i + 1, len(sorted_players)):
                    if sorted_players[j] not in used:
                        pairings.append((sorted_players[i], sorted_players[j]))
                        used.add(sorted_players[i])
                        used.add(sorted_players[j])
                        break

            # Handle odd number of players
            remaining = [p for p in sorted_players if p not in used]
            if remaining:
                print(f"{remaining[0].name} receives a bye (+1 point)")
                remaining[0].points += 1

        # ---------------------------------------------------------
        # CREATE ROUND OBJECT
        # ---------------------------------------------------------
        new_round = Round(round_number=round_number)

        for p1, p2 in pairings:
            match = Match(player1=p1, player2=p2)
            new_round.add_match(match)

        tournament.rounds.append(new_round)
        tournament.current_round = round_number

        # ---------------------------------------------------------
        # DISPLAY PAIRINGS
        # ---------------------------------------------------------
        print("\nPairings:")
        for p1, p2 in pairings:
            print(f"  {p1.name} vs {p2.name}")

        print(f"\nRound {round_number} generated successfully!")

        # ---------------------------------------------------------
        # SAVE TO JSON
        # ---------------------------------------------------------
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

        return NoopCmd("tournament-actions",
                       tournament=tournament,
                       tournament_index=index)

