from classes.game import Person, bcolors

# Name of Magics Spells
# Magic
magic = [{"name" : "Fire", "cost" : 10, "dmg" : 60},
         { "name" : "Thunder", "cost" : 12, "dmg" : 80},
         {"name": "Blizzard", "cost" : 10, "dmg" : 60}]

# Generate the player and enemy character
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

# Initialise the running variable
running  = True
i = 0 

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!"+ bcolors.ENDC)

# Creating the Gaming Loop

while running:
    print("========================")
    # Damage done by player to Enemy
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, " points of damage. Enemy HP:", enemy.get_hp())
    
    # Damage done by enemy to player
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg, " Player HP:", player.get_hp())



