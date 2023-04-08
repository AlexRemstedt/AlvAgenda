from datetime import datetime


class AgendaPunt:
    """Base AgendaPunt object"""

    def __init__(self, id: str, type: str, title: str, duration_minutes: str,
                 speaker: str, subject: str):
        self.id = id
        self.type = type
        self.title = title
        zero_padded_duration = duration_minutes.zfill(2)
        self.duration_minutes = datetime.strptime(zero_padded_duration, "%M")
        self.speaker = speaker
        self.subject = subject

    def numbered_title(self):
        return f"{self.id}. {self.title}"

    def start(self):
        """This is the start of a point."""
        pass

    def mid(self):
        """This is the mid of a point."""
        pass

    def end(self, next_point):
        """This is the end of a point."""
        pass
