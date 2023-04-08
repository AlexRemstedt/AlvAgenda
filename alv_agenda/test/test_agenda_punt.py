from agenda_punt import AgendaPunt
import unittest


class TestAgendaPunt(unittest.TestCase):

    def test_init(self):
        punt = AgendaPunt('test', 0, 10, '19:03')
        self.assertEqual(punt.title, 'test', "Should be 'title'")
        self.assertEqual(punt.tijdsduur, 10, "Should be 10")
        self.assertEqual(punt.id, -1, "Should be -1")
        self.assertEqual(punt.begintijd, '19:03:00', "Should be 19:03:00")
        self.assertEqual(punt.eindtijd, '19:13:00', "should be 19:13:00")
        self.assertEqual(punt.fname, 'test.txt', "Should be test.txt")
        self.assertEqual(punt.path, 'alv_agenda\/snippets\/test.txt',
                         "Should be 'alv_agenda/snippets/test.txt")


if __name__ == "__main__":
    unittest.main()
