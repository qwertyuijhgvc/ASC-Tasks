class Treasure:
    def __init__(self, value:int, level:str): 
        self.value = value
        self.level = level
    
    def getValue(self):
        return self.value
    
    def getLevel(self):
        return self.level
    
gold = Treasure(1000,"high")

print(gold.getValue())
