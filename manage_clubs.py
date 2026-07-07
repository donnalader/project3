import json
from screens import screen_registry, MainMenu


class App:
    """
    Main application controller.
    Handles screen switching and command execution.
    """

    def __init__(self):
        # Load clubs at startup
        self.context = {"clubs": self.load_clubs()}

        # Start at main menu
        self.current_screen = MainMenu

    def load_clubs(self):
        """Load clubs from JSON file."""
        try:
            with open("data/clubs.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def set_screen(self, screen_name, **kwargs):
        """
        Switch to a new screen by name.
        """

        # Validate screen name
        if screen_name not in screen_registry:
            print(f"Unknown screen '{screen_name}'. Returning to main menu.")
            self.current_screen = MainMenu
            self.context = {"clubs": self.load_clubs()}
            return

        # Set the new screen class
        self.current_screen = screen_registry[screen_name]

        # ⭐ FIX: DO NOT wipe context unless explicitly told
        # Merge new kwargs into existing context
        for key, value in kwargs.items():
            if value is not None:
                self.context[key] = value

        # ⭐ Always keep clubs in context
        if "clubs" not in self.context:
            self.context["clubs"] = self.load_clubs()

    def run(self):
        """
        Main loop: display screen → get command → execute command.
        """
        while True:
            screen = self.current_screen(**self.context)
            command = screen.run()

            # All commands must have an execute() method
            if hasattr(command, "execute"):
                command.execute(self)
            else:
                print("Invalid command returned. Returning to main menu.")
                self.set_screen("main-menu")


if __name__ == "__main__":
    app = App()
    app.run()
