from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6,4)

    def test_init_status(self):
       assert self.game.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)

    def test_init_play(self):
        assert self.game.play(1) == "Player 2 plays next"
        assert self.game.play(1) == "Player 1 plays next"
        self.assertRaises(ValueError, self.game.play, -2)
        self.assertRaises(ValueError, self.game.play, 7)
        self.assertRaises(ValueError, self.game.play, self.game.holes)

    def test_init_done(self):
        assert self.game.game_over == False

    def test_init_score(self):
        assert self.game.score() == (0,0)

    # def test_simple_nove(self):
    #     self.game.play(2)
    #     assert self.game.status() == (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0)

if __name__ == '__main__':
    unittest.main()