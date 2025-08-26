from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class TimeInterval:
    """
    Represents an immutable time interval in hours, minutes, and seconds.
    """

    # Conversion factors
    SECONDS_IN_MINUTE: ClassVar[int] = 60
    SECONDS_IN_HOUR: ClassVar[int] = 3600
    MINUTES_IN_HOUR: ClassVar[int] = 60

    # State
    hours: int = 0
    minutes: int = 0
    seconds: int = 0

    def __post_init__(self):
        """
        Post-initialization hook to normalize the time interval.

        Args:
          None

        Returns:
          None
        """
        # Normalize as seconds to support TimeInterval(seconds=90) for example
        total_seconds = self.hours * TimeInterval.SECONDS_IN_HOUR + \
          self.minutes * TimeInterval.SECONDS_IN_MINUTE + self.seconds
        
        hours, remainder = divmod(total_seconds, TimeInterval.SECONDS_IN_HOUR)
        minutes, seconds = divmod(remainder, TimeInterval.SECONDS_IN_MINUTE)

        # Update attributes using __setattr__ because the dataclass is frozen
        object.__setattr__(self, "hours", hours)
        object.__setattr__(self, "minutes", minutes)
        object.__setattr__(self, "seconds", seconds)

    def to_seconds(self) -> int:
        """
        Converts the time interval to seconds.

        Args:
          None

        Returns:
          int: The total number of seconds in the time interval.
        """
        return self.hours * TimeInterval.SECONDS_IN_HOUR + \
          self.minutes * TimeInterval.SECONDS_IN_MINUTE + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds: int) -> "TimeInterval":
        """
        Creates a TimeInterval object from a total number of seconds.

        This is implemented as a class method so that subclasses return instances of themselves
        (i.e., cls), not TimeInterval.

        Args:
          total_seconds (int): The total number of seconds.

        Returns:
          TimeInterval: A new TimeInterval object representing the given number of seconds.
        """
        hours, remainder = divmod(total_seconds, TimeInterval.SECONDS_IN_HOUR)
        minutes, seconds = divmod(remainder, TimeInterval.SECONDS_IN_MINUTE)
        return cls(hours, minutes, seconds)

    def __add__(self, other: "TimeInterval") -> "TimeInterval":
        """
        Adds two time intervals together.

        Args:
          other (TimeInterval): The time interval to add.

        Returns:
          TimeInterval: A new TimeInterval object representing the sum of the two intervals.
        """
        return TimeInterval.from_seconds(self.to_seconds() + other.to_seconds())

    def __mul__(self, factor: int) -> "TimeInterval":
        """
        Multiplies the time interval by an integer factor.

        Args:
          factor (int): The integer factor to multiply the time interval by.

        Returns:
          TimeInterval: A new TimeInterval object representing the result of the multiplication.

        Raises:
          TypeError: If the factor is not an integer.
        """
        if not isinstance(factor, int):
            raise TypeError("Factor must be an integer.")
        return TimeInterval.from_seconds(self.to_seconds() * factor)

    # To allow : factor * interval
    __rmul__ = __mul__

    def __str__(self) -> str:
        """
        Returns a string representation of the time interval in the HH:MM:SS format.

        Args:
          None

        Returns:
          str: A string representing the time interval.
        """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


# Runner code      
interval_1 = TimeInterval(hours=12, minutes=30, seconds=25)
interval_2 = TimeInterval(hours=12, minutes=30, seconds=40)

interval_sum = interval_1 + interval_2
interval_prod = interval_1 * 3

print(f"{interval_1} + {interval_2} = {interval_sum}")
print(f"{interval_1} * 3 = {interval_prod}")
