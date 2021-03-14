
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
    def __init__(self, PlayerName, PlayerPoint, TeamName, TeamOrigin):
        Team.__init__(self, TeamName, TeamOrigin)
        self.PlayerName = "Kelian MBape"
        self.PlayerPoint = 3
    
    def ScoredPoint(self):
        self.PlayerPoint += 1
    
    def setName(self, Name):
        self.TeamName = Name
    def __str__(self):
        return "Player has socored: "+ str(self.PlayerPoint)+ " Points"
Player1 = Player("Mohamed Sallah", 4, "Barca", "Pala")
print(Player1.PlayerName)
print(Player1.PlayerPoint)

print(Player1.TeamName)
print(Player1.TeamOrigin)

Player1.setName("Leonel Messi")

Player1.ScoredPoint()
print(Player1.PlayerPoint)

print(Player1)
