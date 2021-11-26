from dice import Dice

class Bucket :
    
    '''
        Bucket (Gobelet)
        Classe qui gère autant d'instances de la Classe Dice (Dé)
        que renseignée dans le constructeur via le paramèrtre nb_dices
    '''
    
    def __init__(self, nb_dices : int):
        self.dices = []
        self.bucket_value = 0
        self.nb_dices = nb_dices

    @property
    def nb_dices(self):
        return self._nb_dices
    
    @nb_dices.setter
    def nb_dices(self, value: int):
        self._nb_dices = value
          
    def getValues(self):
        '''
            Méthode qui retourne la liste des instances de la Classe
            Dice contenues dans l'attribut "dices"
        '''  
        return self.dices
    
    
    def pitch(self):
        '''
            Méthode qui abonde l'attribut "dices" (liste) d'instances de la Classe
            Dice puis met à jour la valeur du gobelet (Total des valeurs de chaque Dice)
        '''          
        self.dices.clear()
        for i in range(self.nb_dices):
            dice = Dice()
            self.dices.append(dice)
            self.bucket_value += dice.value
            
    def showScore(self):
        '''Afficher en console le score du dernier lancer'''
        print(f"Score du lancer: {self.bucket_value} ")
        

# b = Bucket(5)
# b.pitch()
# b.showScore()