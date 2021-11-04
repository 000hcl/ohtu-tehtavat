import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_returns_none_if_player_is_not_found(self):
        result = self.statistics.search("A")
        self.assertIsNone(result)
    
    def test_search_does_not_return_none_if_player_is_found(self):
        result = self.statistics.search("Semenko")
        self.assertIsNotNone(result)
    
    def test_team_returns_list_of_correct_length(self):
        edm = self.statistics.team("EDM")
        self.assertAlmostEqual(3, len(edm))
    
    def test_top_scorers_returns_list_of_correct_length(self):
        top = self.statistics.top_scorers(4)
        self.assertAlmostEqual(5, len(top))