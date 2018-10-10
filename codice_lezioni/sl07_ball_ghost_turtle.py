'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Ball Ghost Turtle - implementano l'interfaccia Actor
'''

from random import choice, randrange
from sl07_actor import Actor, Arena

class Ball(Actor):
    '''
    Pallina che si muove in diagonale e rimbalza 
    se incontra i limiti dell'arena
    e se si scontra con altri personaggi
    '''
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._speed = 5
        self._dx, self._dy = self._speed, self._speed
        self._arena = arena
        arena.add(self)

    def move(self):
        ''' Rimbalza sui bordi dell'arena '''
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x + self._dx <= arena_w - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= arena_h - self._h):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def collide(self, other):
        if not isinstance(other, Ghost):
            x, y, w, h = other.position()
            if x < self._x:
                self._dx = self._speed	# rimbalzo a ds
            else:
                self._dx = -self._speed	# rimbalzo a sn
            if y < self._y:
                self._dy = self._speed	# rimbalzo in basso
            else:
                self._dy = -self._speed	# rimbalzo in alto
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        ''' sprite coordinate 0,0 20,20 '''
        return 0, 0, self._w, self._h


class Ghost(Actor):
    ''' Fantasma si muove con spostamento casuale
        se esce da un bordo rientra dalla parte opposta
        può diventare invisibile poi riapparire
    '''    
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._arena = arena
        arena.add(self)
        self._visible = True

    def move(self):
        dx = choice([-5, 0, 5])
        dy = choice([-5, 0, 5])
        arena_w, arena_h = self._arena.size()
        self._x = (self._x + dx) % arena_w
        self._y = (self._y + dy) % arena_h

        if randrange(100) == 0:
            self._visible = not self._visible

    def collide(self, other):
        pass
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._visible:
            return 20, 0, self._w, self._h	# immagine visibile
        return 20, 20, self._w, self._h		# immagine se invisibile


class Turtle(Actor):
    ''' Tartaruga: movimento guidato dai tasti freccia
        non supera i bordi dell'arena
    '''
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._speed = 2
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def go_left(self):
        self._dx, self._dy = -self._speed, 0
        
    def go_right(self):
        self._dx, self._dy = +self._speed, 0

    def go_up(self):
        self._dx, self._dy = 0, -self._speed
        
    def go_down(self):
        self._dx, self._dy = 0, +self._speed

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        pass
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 20, self._w, self._h
