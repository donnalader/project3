from commands.context import Context
from .base import BaseCommand

class NoopCmd(BaseCommand):
    """A command that simply returns a context with a given screen."""

    def __init__(self, screen, **kwargs):
        self.screen = screen
        self.kwargs = kwargs

    def execute(self, app=None, **kwargs):
        # Merge kwargs passed at creation with kwargs passed at execution
        merged = {}
        merged.update(self.kwargs)
        merged.update(kwargs)
        return Context(self.screen, kwargs=merged)

