class NoopCmd:
    """
    A simple command that switches screens without performing any action.
    Now supports clearing context to avoid passing unwanted kwargs
    (such as 'tournament') to screens that don't accept them.
    """

    def __init__(self, screen_name, clear_context=False, **kwargs):
        self.screen_name = screen_name

        # If clear_context=True, wipe all kwargs so screens like MainMenu don't crash
        if clear_context:
            self.kwargs = {}
        else:
            self.kwargs = kwargs

    def execute(self, app):
        """
        The app will call this to switch screens.
        """
        app.set_screen(self.screen_name, **self.kwargs)



