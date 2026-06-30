class Context:
    """
    Represents a 'context' for the application.
    """

    def __init__(self, screen=None, run=True, kwargs=None, **extra):
        # screen name
        self.screen = screen

        # whether the app should keep running
        self.run = run

        # kwargs for the next screen
        # merge kwargs and extra keyword arguments
        self.kwargs = kwargs or {}
        self.kwargs.update(extra)

    def set_args(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return f"<Context: {self.screen} | {self.kwargs}>"

