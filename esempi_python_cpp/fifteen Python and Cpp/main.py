import cppyy
cppyy.include("fifteen.cpp")
from cppyy.gbl import Fifteen

from boardgame_g2d import BoardGameGui

game = Fifteen(3, 3)
gui = BoardGameGui(game)
gui.main_loop()
