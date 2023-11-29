import datetime


class Timestamp:
    """Timestamp model."""

    def __init__(self, timestamp: str = ""):
        """Initialize."""
        self._ct = datetime.datetime.now()
        self._ts = self._ct.timestamp()

    @property
    def get_timestamp(self) -> float:
        """Return timestamp."""
        return self._ts

    @property
    def get_current_time(self) -> datetime.datetime:
        """Return current time."""
        return self._ct

    def generate_timestamp(self, days=0, hours=0, minutes=0, seconds=0):
        """Generate timestamp."""
        print("current time:-", self._ct)
        new_ct = self._ct + datetime.timedelta(
            days=days, hours=hours, minutes=minutes, seconds=seconds
        )
        print("new time:-", new_ct)
        return new_ct.timestamp()

    def return_timestamp(self, timestamp: float) -> datetime.datetime:
        """Return timestamp."""
        return datetime.datetime.fromtimestamp(timestamp)
