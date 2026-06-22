from models.tournament import Tournament

def main():
    t = Tournament(
        name="Spring Open",
        venue="Richmond",
        start_date="2024-04-01",
        end_date="2024-04-03",
        total_rounds=4
    )

    print("Tournament name:", t.name)
    print("Venue:", t.venue)
    print("Dates:", t.start_date, "to", t.end_date)
    print("Total rounds:", t.total_rounds)
    print("Current round:", t.current_round)

if __name__ == "__main__":
    main()
