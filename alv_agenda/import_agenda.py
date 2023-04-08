"""Import an agenda from an .xlsx file."""


from agenda_punten import AgendaPunt
import pandas as pd


class AgendaData:
    """Import agenda data from an excel."""

    def __init__(self, workbook_location_string: str):
        self.dataframe = pd.read_excel(workbook_location_string)

    def import_from_excel(self):
        """Import data from excel and paste in list."""
        listed_agenda_data = []
        for index, row in self.dataframe.iterrows():
            listed_agenda_data.append([index, row])
        return listed_agenda_data


def main():
    agenda_data = AgendaData('./alv_agenda/agenda_punten.xlsx')
    agenda_data.import_from_excel()


if __name__ == "__main__":
    main()

