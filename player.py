from bucket import Bucket


class Player :
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def getName(self) :
        ''' Méthode qui retourne le nom du joueur '''
        return self.name
    
    def getScore(self) :
        ''' Méthode qui retourne le score du joueur '''
        return self.score
    
    def play(self, Bucket : Bucket) :
        ''' 
            Lancer du Gobelet
            Récupère le gobelet du joueur (Bucket en paramètre)
            Et le lance. (Pitch).
            Puis incrémente le score du joueur (Total de tous ses lancers)
        
        '''
        Bucket.pitch()    
        for Dice in Bucket.dices :
            self.score += Dice.getValue()
            
    def showScore(self):
        ''' Méthode qui affiche le score du joueur en console '''
        print(f"{self.name} - Score : {self.score}")
    
    
    
# p = Player("Tommy")

# p.play(Bucket(2))

# p.showScore()