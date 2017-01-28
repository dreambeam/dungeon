from dungeon_game import get_moves
import unittest

class test_dungeon_game(unittest.TestCase):
	def test_get_moves(self):
		self.assertTrue(get_moves(1))

if __name__ == '__main__':
	unittest.main(exit=False)