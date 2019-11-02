import unittest
from lightsout_console import LightsOut
from random import randrange

class LightsOutTest(unittest.TestCase):

	def test_play_at_00(self):		# test 0,0
		game = LightsOut(side = 6, level = 0)		# 6x6 all False
		game.play_at(0,0)
		for dx, dy in ((0, 0), (1, 0), (0, 1)):
			self.assertTrue(game.value_at(dx,dy) == "@")
		game.play_at(0,0)
		for dx, dy in ((0, 0), (1, 0), (0, 1)):
			self.assertTrue(game.value_at(dx,dy) == "-")
		#self.assertTrue(game.value_at(3,3) == "@")

	def test_playat_rnd(self):		# test random
		side = randrange(10)
		game = LightsOut(side, level = 0)		# sidexside all False
		x = randrange(side)
		y = randrange(side)
		game.play_at(x,y)
		for dx, dy in ((0, 0), (0, -1), (1, 0),(0, 1), (-1, 0)):
			if 0 <= x+dx < side and 0 <= y +dy < side:
				self.assertTrue(game.value_at(x+dx,y+dy) == "@")
		game.play_at(x,y)
		for dx, dy in ((0, 0), (0, -1), (1, 0),(0, 1), (-1, 0)):
			if 0 <= x+dx < side and 0 <= y +dy < side:
				self.assertTrue(game.value_at(x+dx,y+dy) == "-")

if __name__ == '__main__':
	unittest.main()
