from random import randint

class Dice :
    
    '''
        Initialise un dé avec une valeur égale à Zéro (Tel que demandé dans l'énoncé)
        Puis l'affecte une valeur aléatoire comprise entre
        1 et 6
    '''
    
    def __init__(self):
        self.value = 0
        self.pitch()
    
    def getValue(self):
        '''Retourne la valeur du dé'''
        return self.value
    
    def pitch(self):
        ''' Génère une valeur aléatoire comprise entre 1 et 6 et la définit entant que
            valeur du dé
        '''
        self.value = randint(1,6)

    
# d = Dice()
# print(d.getValue())