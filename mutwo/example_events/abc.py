import abc

# Add an empty line between buildin modules and mutwo modules

# Always use the "from mutwo import ..." style of imports
from mutwo import core_constants
from mutwo import core_events

# Specify __all__ to have clean wildcard imports
__all__ = ("AbstractExampleEvent",)


class AbstractExampleEvent(core_events.SimpleEvent):
    def __init__(self):
        super().__init__(self.constant_duration)

    @abc.abstractclassmethod
    @property
    def constant_duration(cls) -> core_constants.DurationType:
        raise NotImplementedError
