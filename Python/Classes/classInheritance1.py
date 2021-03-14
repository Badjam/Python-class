
class Team:
    def __init__(self, Name = "Ouragan", Origin = "Tempete"):
        self.TeamName = Name
        self.TeamOrigin = Origin
        
    def DefineTeamName(self, Name):
        self.TeamName = Name
        
    def DefineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin
# The class Player inherites the properties of base class Team
class Player(Team):
    def __init__(self):
        Team.__init__(self)
        self.PlayerName = "Sadjo Mane"
        self.PlayerPoint = 5
        
    def ScoredPoint(self):
        self.PlayerPoint += 1
        
    def setName(self, Name):
        self.TeamName = Name
        
Player1 = Player()
print(Player1.PlayerName)
print(Player1.PlayerPoint)
Player1.TeamOrigin = "Liver Pool"
Player1.DefineTeamOrigin("Gaboke")
print(Player1.TeamName)
print(Player1.TeamOrigin)

