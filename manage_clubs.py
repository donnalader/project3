from screens import MainMenu
from commands.noop import NoopCmd


class App:
    """
    Main application controller.
    Handles screen switching and command execution.
    """

    def __init__(self):
        # Initial context passed to screens
        self.context = {}

        # Start at main menu
        self.current_screen = MainMenu

    def set_screen(self, screen_name, **kwargs):
        """
        Switch to a new screen by name.
        """
        from screens import screen_registry

        if screen_name not in screen_registry:
            print(f"Unknown screen '{screen_name}'. Returning to main menu.")
            self.current_screen = MainMenu
            self.context = {}
            return

        self.current_screen = screen_registry[screen_name]
        self.context = kwargs

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
                print("Invalid command object returned. Returning to main menu.")
                self.set_screen("main-menu")


if __name__ == "__main__":
    app = App()
    app.run()
