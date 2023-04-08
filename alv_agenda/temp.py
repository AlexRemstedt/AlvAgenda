
    def get_index(self):
        """Get the index of this agenda point."""
        pass

    def doorslaan(self, document, next_punt):
        """Het stukje tekst aan het einde van een puntje.

        Het stukje waarbij doorgeslagen wordt naar het volgende punt.
        """
        if not next_punt.schorsing:
            return f"Als er verder geen vragen zijn wil ik {self.spreker} " \
                    "graag bedanken en gaan we met de volgende hamerslag " \
                    f"door naar punt {next_punt.index}; {next_punt.title}. " \
                    "HAMERSLAG"

        return "Als er verder geen vragen zijn wil ik de Algemene Leden " \
               f"Vergadering van {document.datum} met de volgende hamerslag " \
               f"schorsen voor {self.duration_minutes} minuten. Dat " \
               "betekent dat we om ____ door gaan."

    def tekst_builder(self, document):
        document.doc.add_paragraph(self.intro())
        document.doc.add_paragraph(self.mid())
        document.doc.add_paragraph(self.doorslaan())


class Mededeling(AgendaPunt):
    """Mededelingen basis object."""

    def make_title(self, document):
        """Make the title of a mededeling."""
        document.doc.add_paragraph(self.title, style="List Number")


class MededelingenAlgemeen(Mededeling):
    """Algemene mededelingen van de voorzitter."""

    def __init__(self, duration_minutes, start_time):
        super().__init__(self, "Mededelingen",
                         duration_minutes, start_time, "voorzitter")

    def tekst(self, document):
        document.doc.add_paragraph("Allereerst wil ik de TaBakCie bedanken "
                                   "voor hun heerlijke taarten \n")
        document.doc.add_paragraph(document.veranderende_agenda_punten())
        document.doc.add_paragraph(document.regels())
        document.doc.add_paragraph(self.doorslaan())


class MededelingenOnderwijs(Mededeling):
    """Algemene mededelingen van de commissaris onderwijs."""

    def __init__(self, duration_minutes, start_time):
        super().__init__(self, "Mededelingen onderwijs",
                         duration_minutes, start_time, "commissaris onderwijs")

    def intro(self):
        return f"Hiervoor wil ik de {self.spreker} vragen plaats te " \
            "nemen achter de katheder."

    def mid(self):
        return f"{self.spreker.upper()} PRAAT\n Zijn er nog vragen uit de zaal?"

        # Building text
        document.doc.add_paragraph(intro)
        document.doc.add_paragraph(mid)
        document.doc.add_paragraph(self.doorslaan())


class MededelingenFinancieel(Mededeling):
    """Algemene mededelingen van de penningmeester."""

    def __init__(self, duration_minutes, start_time):
        super().__init__(self, "Mededelingen onderwijs",
                         duration_minutes, start_time, "commissaris onderwijs")

    def intro(self):
        return f"Hiervoor wil ik de {self.spreker} vragen plaats te " \
            "nemen achter de katheder."

    def mid(self):
        return f"{self.spreker.upper()} PRAAT\n Zijn er nog vragen uit de zaal?"


class GoedkeuringNotulen(AgendaPunt):
    """Goedkeuring van de notulen van de vorige ALV."""

    def __init__(self, duration_minutes, start_time, vorige_alv):
        self.datum_vorige_notulen = None  # TODO
        super().__init__("Goedkeuring van de notulen "
                         "gehouden op {self.datum_vorige_notulen}",
                         duration_minutes, start_time, "secretaris")

    def intro(self):
        return f"Hiervoor wil ik het woord geven aan de {self.spreker}."

    def mid(self):
        return "Hartelijk dank.\n Dan zijn er nog een aantal punten om terug " \
            "te koppelen.\n -\n -"


class GoedkeuringBegroting(AgendaPunt):

    def intro(self):
        return f"Hiervoor wil ik de {self.spreker} vragen om de begroting " \
            f"van {self.activiteit} te presenteren."

    def mid(self):
        return "Hartelijk dank, zijn er nog vragen vanuit de zaal?"


def main():
    pass


if __name__ == "__main__":
    main()
