from player import Player
from bucket import Bucket

class Game :
    
    def __init__(self, turns: int, dices: int, players_names : list) :
        
        self.players = [Player(name) for name in players_names]
        self.dices = dices
        self.turns = turns

            
    def launch(self) :
        
        for turn in range(self.turns) :
            for player in self.players :
                bucket = Bucket(self.dices)
                player.play(bucket)
                print(f"{player.name} a joué {bucket.bucket_value} points. Score : {player.score}")
        
        classement = self.getClassement()
       
        
    def sortByPoints(self, arr) :
        return arr[0]
    
    def getClassement(self):
        classement = [[player.score, player.name] for player in self.players]
        classement.sort(key=self.sortByPoints, reverse=True)
        return classement


        


partie = Game(300, 2, ["Tommy", "Francois", "Zoubida", "Xavier", "Isabelle", "Nagi", "Richard", "Randy", "Romy", "Boualem"])

partie.launch()

vainqueur = partie.getClassement()[0]

print(f"{vainqueur[1]} a gagné la partie avec {vainqueur[0]} points")