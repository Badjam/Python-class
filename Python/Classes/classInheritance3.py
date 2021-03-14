
class Pets:
    def __init__(self, n, a, h, p):
        self.Name = n
        self.age = a
        self.hunger = h
        self.playful = p
        
    def getName(self):
        return self.Name
    
    def getAge(self):
        return self.age
    
    def getHunger(self):
        return self.hunger
    
    def getPlayful(self):
        return self.playful
    
    def setName(self, myName):
        self.Name = myName
        
    def setAge(self, theAge):
        self.age = theAge
        
        
    def setHunger(self, hung):
        self.hunger = hung
        
    def setPlayful(self, play):
        self.playful = play
        
        
Pets1 = Pets("Baramu", 5, False, True)

print(Pets1.getName())
print(Pets1.getAge())
Pets1.setName("Chernobil")
print(Pets1.Name)

Pets1.Name = "Kawazaky"

print(Pets1.Name)




