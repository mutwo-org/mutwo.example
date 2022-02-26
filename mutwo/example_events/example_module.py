# Always use the "from mutwo import ..." style of imports
from mutwo import core_constants
from mutwo import example_events

# Specify __all__ to have clean wildcard imports
__all__ = ("ExampleEvent",)


class ExampleEvent(example_events.AbstractExampleEvent):
    @classmethod
    @property
    def constant_duration(cls) -> core_constants.DurationType:
        return example_events.constants.EXAMPLE_EVENT_DURATION
