from commands.context import Context
from .base import BaseCommand

class NoopCmd(BaseCommand):
    """A command that simply returns a context with a given screen."""

    def __init__(self, screen, **kwargs):
        self.screen = screen
        self.kwargs = kwargs

    def execute(self, app=None, **kwargs):
        # Always merge constructor kwargs with execution kwargs
        merged = dict(self.kwargs)   # start with kwargs passed at creation
        merged.update(kwargs)        # add kwargs passed at execution (if any)

        # Ensure app.context exists before updating
        if app is not None and hasattr(app, "context"):
            # If app.context.kwargs is missing, create it
            if not hasattr(app.context, "kwargs"):
                app.context.kwargs = {}

            # Update app context with merged kwargs
            app.context.kwargs.update(merged)

        # Return a Context pointing to the next screen
        return Context(self.screen, kwargs=merged)



