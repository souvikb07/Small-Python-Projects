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
        """ Create a Profile of Individual Players
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

    # Function to generate damage points
    def generate_damage(self):
        """ Create Damage Points of an attack
        Parameters
        ----------

        Returns
        ----------
         Range of attack damage : num
        """
        return random.randrange(self.atkl, self.atkh)

    # Function to generate spell damage points
    def generate_spell_damage(self, i):
        """ Create spell damage points of an attack
        Parameters
        ----------
        i : num
            Index of the magic list
        Returns
        ----------
         Range of magic damage : num
        """
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)
    
    # Function to generate Players take damage points
    def take_damage(self, dmg):
        """ Create the damage that is taken by the player
        Parameters
        ----------
        dmg : num
            Damage Points
        Returns
        ----------
         Health Point after damage : num
        """
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    # Function for hp
    def get_hp(self):
        return self.hp

    # Function for max hp
    def max_hp(self):
        return self.maxhp
    
    # Function for reduce MP
    def reduce_mp(self, cost):
        self.mp -= cost

    # Funtion which gives spell name
    def spell_name(self, i):
        return self.magic[i]["name"]

    # Function to get the spell mp cost
    def get_spell_mp_cost(self,i):
        return self.magic[i]["cost"]
    
    # Function to choose action
    def choose_action(self):
        i = 1
        print("Action")
        for item in self.action:
            print(str(i) + ":" + item)
            i += 1
    
    # Function to choose Magic
    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":" + spell["name"] + "(cost:" , str(spell["cost"]) + ")")
            i += 1