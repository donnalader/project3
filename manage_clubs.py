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
        if screen_name not in screen_registry:
            print(f"Unknown screen '{screen_name}'. Returning to main menu.")
            self.current_screen = MainMenu
            self.context = {"clubs": self.load_clubs()}
            return

        self.current_screen = screen_registry[screen_name]

        # Always keep clubs in context
        new_context = {"clubs": self.context.get("clubs", [])}

        # Add any additional kwargs (except None)
        for key, value in kwargs.items():
            if value is not None:
                new_context[key] = value

        self.context = new_context

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
