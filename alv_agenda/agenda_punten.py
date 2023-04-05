from datetime import datetime


class AgendaPunt:
    """AgendaPunt"""

    def __init__(self, title: str, duration_minutes: str, start_time: str,
                 spreker: str):
        self.title = title

        zero_padded_duration = duration_minutes.zfill(2)
        self.duration_minutes = datetime.strptime(zero_padded_duration, "%M")

        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.index = self.get_index()

    def get_index(self):
        """Get the index of this agenda point."""
        pass

    def doorslaan(self, document, next_punt):
        """Het stukje tekst aan het einde van een puntje.

        Het stukje waarbij doorgeslagen wordt naar het volgende punt.
        """
        document.doc.add_paragraph(f"Als er verder geen vragen zijn wil ik "
                                   f"{self.spreker} graag bedanken en gaan we "
                                   f"met de volgende hamerslag door naar punt "
                                   f"{next_punt.index}; {next_punt.title}."
                                   f"HAMERSLAG")


class Mededeling(AgendaPunt):
    """Mededelingen base"""

    def make_title(self, document):
        """Make the title of a mededeling."""
        document.doc.add_paragraph(self.title, style="List Number")


class MededelingenAlgemeen(Mededeling):
    """Algemene mededelingen van de voorzitter."""

    def __init__(self, duration_minutes, start_time):
        super().__init__(self, "Mededelingen", duration_minutes, start_time, "voorzitter")

    def tekst(self, document):
        document.doc.add_paragraph("Allereerst wil ik de TaBakCie bedanken "
                                   "voor hun heerlijke taarten \n")
        document.doc.add_paragraph(document.veranderende_agenda_punten())
        document.doc.add_paragraph(document.regels())
        document.doc.add_paragraph(self.doorslaan())

#########################################
    def compile_par(self):
        with open(self.path) as p:
            paragraph = p.read()
            compiled_paragraph = compile(paragraph, f'<{paragraph}>', 'eval')
        return compiled_paragraph
