from datetime import time


class AgendaPunt:
    """AgendaPunt"""

    def __init__(self, title, id, tijdsduur, begintijd, **kwargs):
        self.title = title
        self.tijdsduur = tijdsduur
        self.id = int(id) - 1
        [h, m] = [int(n) for n in begintijd.split(":")]
        self.begintijd = time(h, m)
        self.eindtijd = self.begintijd.minute + int(tijdsduur)
        self.path = kwargs['text_location']
