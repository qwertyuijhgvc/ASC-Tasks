import math
import random
class Animal:
    #private age
    #private vertebrae
    
    #public procedure sound
    
    def __init__(self, vertebrae) -> None:
        self.age = 0                #private
        self.vertebrae = vertebrae  #private
    #end public constructor
    
    
    def sound():
        pass
    #end public procedure
#end class

class Mammal(Animal):
    def __init__(self,legs) -> None:
        super().__init__(True)
        self.legs = legs
    #end constructor
#end class

class Dogs(Mammal):
    def sound():
        print("woof")
    #end public procedure
#end class

class Cats(Mammal):
    def sound():
        print("meow")
    #end public procedure
#end class

pets = []
seedlist = [1,0,0,1,0,0,1,0,1]
for _ in seedlist:
    if _ == 1:
        _ = Dogs
        pets.append(_)
    else:
        _ = Cats
        pets.append(_)
    #end if
#next _
for x in range(len(pets)):
    pets[x].sound()
#next x
