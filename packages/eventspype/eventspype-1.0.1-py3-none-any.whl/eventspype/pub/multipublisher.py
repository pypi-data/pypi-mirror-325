from typing import Any

from eventspype.pub.publication import EventPublication
from eventspype.pub.publisher import EventPublisher
from eventspype.sub.functional import FunctionalEventSubscriber
from eventspype.sub.subscriber import EventSubscriber


class MultiPublisher:
    """
    A publisher that can handle multiple event types through different publications.
    Each publication is handled by its own EventPublisher instance.
    """

    def __init__(self) -> None:
        # Map of publications to their dedicated publishers
        self._publishers: dict[EventPublication, EventPublisher] = {}
        # Keep references to functional subscribers to prevent garbage collection
        self._functional_subscribers: dict[Any, FunctionalEventSubscriber] = {}

    # === Class Methods ===

    @classmethod
    def get_event_definitions(cls) -> dict[str, EventPublication]:
        """Get all event publications defined in the class."""
        result = {}
        for name, value in cls.__dict__.items():
            if isinstance(value, EventPublication):
                result[name] = value
        return result

    @classmethod
    def is_publication_valid(
        cls, publication: EventPublication, raise_error: bool = True
    ) -> bool:
        """Check if a publication is valid."""
        if publication not in cls.get_event_definitions().values():
            if raise_error:
                raise ValueError(f"Invalid publication: {publication}")
            return False
        return True

    # === Subscriptions ===

    def _get_or_create_publisher(self, publication: EventPublication) -> EventPublisher:
        """Get or create a dedicated publisher for a publication."""
        if publication not in self._publishers:
            self._publishers[publication] = EventPublisher(publication)
        return self._publishers[publication]

    def add_subscriber(
        self, publication: EventPublication, subscriber: EventSubscriber
    ) -> None:
        """Add a subscriber for a specific publication."""
        self.is_publication_valid(publication, raise_error=True)

        publisher = self._get_or_create_publisher(publication)
        publisher.add_subscriber(subscriber)

    def remove_subscriber(
        self, publication: EventPublication, subscriber: EventSubscriber
    ) -> None:
        """Remove a subscriber for a specific publication."""
        self.is_publication_valid(publication, raise_error=True)

        if publication not in self._publishers:
            return

        publisher = self._publishers[publication]
        publisher.remove_subscriber(subscriber)

        # Clean up empty publishers
        if not publisher.get_subscribers():
            del self._publishers[publication]

    def add_subscriber_with_callback(
        self, publication: EventPublication, callback: Any
    ) -> None:
        """Add a callback function as a subscriber for a specific publication."""
        self.is_publication_valid(publication, raise_error=True)

        subscriber = FunctionalEventSubscriber(callback)

        # Keep a reference to the subscriber
        self._functional_subscribers[callback] = subscriber
        self.add_subscriber(publication, subscriber)

    def remove_subscriber_with_callback(
        self, publication: EventPublication, callback: Any
    ) -> None:
        """Remove a callback function subscriber for a specific publication."""
        self.is_publication_valid(publication, raise_error=True)

        if publication not in self._publishers:
            return

        # Get the subscriber from our references
        if callback in self._functional_subscribers:
            subscriber = self._functional_subscribers[callback]
            self.remove_subscriber(publication, subscriber)
            del self._functional_subscribers[callback]

    # === Events ===

    def publish(self, publication: EventPublication, event: Any) -> None:
        """Trigger an event for a specific publication."""
        self.is_publication_valid(publication, raise_error=True)

        if publication not in self._publishers:
            return

        # Use the dedicated publisher to trigger the event
        self._publishers[publication].publish(event)
