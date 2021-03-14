class Team:
    def __init__(self):
        self.TeamName = "myTeamName"
        self.TeamOrigin = "myTeamOrigin"
        
    
        
    def DefineTeamName(self, myTeamName):
        self.TeamName = myTeamName
        
        
    def DefineTeamOrigin(self, myTeamOrigin):
        self.TeamOrigin= myTeamOrigin
        
        
myTeam = Team()

print(myTeam.TeamName)

myTeam.DefineTeamName("Chimen")
print(myTeam.TeamName)
print(myTeam.TeamOrigin)

myTeam.DefineTeamOrigin("Gondwana")
print(myTeam.TeamOrigin)




