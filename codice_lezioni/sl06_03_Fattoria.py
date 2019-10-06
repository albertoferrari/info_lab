'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 fattoria parlante
'''

class Animale: 
   def parla(self): 
     raise NotImplementedError("metodo astratto") 

class Cane(Animale):
    def __init__(self, nome):
        self._nome = nome
    def parla(self):
        print("sono", self._nome, ", un cane ... bau")

class Gatto(Animale):
    def __init__(self, nome):
        self._nome = nome
    def parla(self):
        print("sono", self._nome, ", un gatto ... miao")
        
class Maiale(Animale):
    def __init__(self, nome):
        self._nome = nome
    def parla(self):
        print("sono", self._nome, ", un maiale ... oink")
        
# lista di animali
c = Cane("Belva")
g = Gatto("Fufi")
m1 = Maiale("Peppa")
m2 = Maiale("George")

animali = [c, g, m1, m2]

for a in animali:
    a.parla()
