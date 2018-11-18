import cppyy
cppyy.include("lightsout.cpp")
from cppyy.gbl import LightsOut

from boardgame_g2d import BoardGameGui

game = LightsOut(4, 5, 5)
gui = BoardGameGui(game)
gui.main_loop()
