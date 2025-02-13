from collections import defaultdict
from typing import Any, Callable

from baukasten.logger import get_logger

logger = get_logger('event_bus')


class Event:
    def __init__(self, source: str, type: str, data: Any):
        self.source = source
        self.type = type
        self.data = data


class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def publish(self, event: Event) -> None:
        logger.debug(f"Publishing event: {event.source} -> {event.type} with data: {event.data}")
        if len(self.subscribers[event.source]) == 0:
            logger.debug(f"No subscribers to notify.")
            return

        for subscriber in self.subscribers[event.source]:
            logger.debug(f"Notifying subscriber for {event.source}")
            subscriber(event)

    def subscribe(self, source: str, callback: Callable[[Event], None]) -> None:
        logger.debug(f"New subscription to {source} events")
        self.subscribers[source].append(callback)