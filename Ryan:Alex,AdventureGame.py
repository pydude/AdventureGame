import random

player = 150
knight = 50
knightgroup = 150
royalguard = 100
bigboss = 350
smallboss = 275
tenbossgroup = 400

def checkPlayerHealth():
    if player < 1:
        print("You died.")
        exit()

def hardAttack():
    global enemy
    attack = random.randint(1, 17)
    print("Player attacks!")
    print("Attack = ", attack, "Points")
    enemy = enemy - attack
    print("Enemy Health:", enemy)

def conserveAttack():
    global enemy
    attack = random.randint(7, 9)
    print("Player attacks!")
    print("Attack = ", attack, "Points")
    enemy = enemy - attack
    print("Enemy Health:", enemy)
    
def bigbossAttack():
    global player
    attack = random.randint(9, 21)
    print("BigBoss attacks!")
    print("Attack = ", attack, "Points")
    player = player - attack
    print("Player Health:", player)

def smallbossAttack():
    global player
    attack = random.randint(8, 19)
    print("SmallBoss attacks!")
    print("Attack = ", attack, "Points")
    player = player - attack
    print("Player Health:", player)

def tenbossgroupAttack():
    global player
    attack = random.randint(5, 19)
    print("10BossGroup attacks!")
    print("Attack = ", attack, "Points")
    player = player - attack
    print("Player Health:", player)

print("You wake up in a room with a single door. Do you go through or fall back asleep?")

print("You open the door and are in front of a castle. The guards appear mad at you. Fight or run?")


print()
bigbossAttack()
smallbossAttack()
tenbossgroupAttack()
print()
