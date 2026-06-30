from abc import ABCMeta, abstractmethod
from commands.context import Context


class BaseCommand(metaclass=ABCMeta):
    """Base class for all commands."""

    @abstractmethod
    def execute(self, app=None, **kwargs):
        """Child classes must implement this."""
        pass

    def __call__(self, app=None, **kwargs):
        """
        Calling a command runs execute(), but we must ensure
        the result is ALWAYS a Context object.
        """
        result = self.execute(app=app, **kwargs)

        # If execute returned another command, run it
        if hasattr(result, "__call__"):
            return result()

        # If execute returned a screen name (string), wrap it
        if isinstance(result, str):
            return Context(screen=result)

        # If execute returned a Context already, return it
        if isinstance(result, Context):
            return result

        # If execute returned nothing, stay on current screen
        if result is None:
            return Context(screen="main-menu")

        # Fallback: wrap anything unexpected
        return Context(screen=str(result))

