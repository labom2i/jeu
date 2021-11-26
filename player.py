from bucket import Bucket


class Player :
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value

    
    def play(self, Bucket : Bucket) :
        ''' 
            Lancer du Gobelet
            Récupère le gobelet du joueur (Bucket en paramètre)
            Et le lance. (Pitch).
            Puis incrémente le score du joueur (Total de tous ses lancers)
        '''
        Bucket.pitch()    
        for Dice in Bucket.dices :
            self.score += Dice.value
            
    def showScore(self):
        ''' Méthode qui affiche le score du joueur en console '''
        print(f"{self.name} - Score : {self.score}")
    
    
    
# p = Player("Tommy")

# p.play(Bucket(2))

# p.showScore()