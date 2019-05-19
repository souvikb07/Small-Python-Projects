# All the necessary Imports
import random
# This class is used to build the background color
class bcolors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# create class for player
class Person():
    def __init__(self, hp, mp, atk, df, magic):
            """
            Parameters
            ----------
            hp : num
                Health Point
            mp : num
                Magic Points
            atk : num
                Attack Points
            df : num
                Defence Points
            magic : str
                Magic Type
            
            Returns
            -------
            maxhp : num
                Max Health Point of Player
            hp : num
                Health Point of Player
            maxmp : num
                Max Magic Points of Payer
            mp : num
                Magic Points of Payer
            atkl : num
                Low Attack Points of Player
            atkh : num
                High Attack Points of Player
            df : num
                Defence Points of Player
            magic : str
                Magic Type of Player
            action : str
                Action taken by Player
            """
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.magic = magic
        self.action = ["Attack", "Magic"]
    
    def generate_damage(self):
        """
        Parameters
        ----------

        Returns
        ----------
         Range of attack : num
        """
        return random.randrange(self.atkl, self.atkh)