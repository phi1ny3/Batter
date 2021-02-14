import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to
    detect player keypresses and translate them into a point representing a
    direction (or velocity).

    Stereotype:
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-2, 0) # a
        self._keys[0x01] = Point(-2, 0) # <-
        self._keys[100] = Point(2, 0) # d
        self._keys[0x02] = Point(2, 0)  # ->
        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction