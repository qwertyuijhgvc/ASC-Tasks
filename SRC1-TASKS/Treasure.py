class Treasure:
    def __init__(self, value:int, level:str): 
        self.__value = value
        self.__level = level
    #end procedure
    def getValue(self):
        return self.__value
    #end function
    def getLevel(self):
        return self.__level
    #end function
    def setValue(self, value:int):
        self.__value = value
    #end proedure
    def setLevel(self, level:str):
        self.__level = level
    #end procedure
#end class
gold = Treasure(1000,"high")

print()
