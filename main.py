"""Main document."""


from docx import Document
from datetime import date, time


class AgendaPunt:
    """AgendaPunt"""

    def __init__(self, title, nummer, tijdsduur, begintijd):
        self.title = title
        self.tijdsduur = tijdsduur
        self.nummer = nummer - 1
        [h, m] = [int(n) for n in begintijd.split(":")]
        self.begintijd = time(h, m)
        self.eindtijd = self.begintijd.minute + tijdsduur


class Agenda:
    """Agenda class."""
    title = "Algemene Leden Vergadering van het \"S. G. William Froude\""

    def __init__(self, agenda_punten, location):
        self.agenda_punten = agenda_punten
        self.date = date.today().strftime("%d-%m-%Y")
        self.doc = Document()
        self.location = location

        # Agenda creations
        self.init_agenda()

    def add_agenda_punt(self, title, nummer, tijdsduur, begintijd):
        agenda_punt = AgendaPunt(title, nummer, tijdsduur, begintijd)
        self.agenda_punten.insert(agenda_punt.nummer, agenda_punt)

    def save_agenda(self):
        """Save the agenda."""
        self.doc.save('Agenda.docx')
        return True

    def init_agenda(self):
        """Initiate agenda."""
        # Create header
        with open('snippets/header.txt') as h:
            header = h.read()
            compiled_header = compile(header, '<header>', 'eval')
            evaluated_header = eval(compiled_header)
        self.doc.add_paragraph(evaluated_header)

    def create_agenda(self):
        for agenda_punt in self.agenda_punten:
            self.doc.add_paragraph(agenda_punt.title, style='List Number')
        return "Agenda updated"


# Create Document
def main():
    alv_agenda = Agenda([], 'Hier')
    alv_agenda.add_agenda_punt("MMD", 2, 10, "19:03")
    alv_agenda.add_agenda_punt("DWT", 1, 10, "19:03")
    alv_agenda.create_agenda()
    alv_agenda.save_agenda()


if __name__ == "__main__":
    main()


# document = Document()

# document.add_paragraph('')

# p = document.add_paragraph('A plain paragraph having some ')
# p.add_run('bold').bold = True


# title = input("title: ")
# nummer = input("nummer: ")
# tijdsduur = input("tijdsduur: ")
# begintijd = input("begintijd: ")
# eindtijd = input("eindtijd: ")

# document.save('demo.docx')
