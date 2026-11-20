import unittest
from core_engine import compute_buchholz

class TestChess(unittest.TestCase):
    def test_buchholz(self):
        players = {"p1": {"points": 3}, "p2": {"points": 2}, "p3": {"points": 1}}
        rounds = {"p1": [{"opponent_id": "p2"}, {"opponent_id": "p3"}]}
        b = compute_buchholz("p1", rounds, players)
        self.assertEqual(b, 3)

if __name__ == "__main__":
    unittest.main()
