
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
        
        
class Dog(Pets):
    def __init__(self,Name, age, hunger, playful, breed, myFavoriteToy):
        Pets.__init__(self,Name, age, hunger, playful)
        self.breed = breed
        self.FavoriteToy = myFavoriteToy
    
    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with "+self.FavoriteToy)
        else:
            return ("Dog does not want to play")
        
huskyDog = Dog("Snowboy", 5, False, True,"Husky", "Stick")

play = huskyDog.wantsToPlay()
print(play)

huskyDog.playful = False

play = huskyDog.wantsToPlay()

print(play)