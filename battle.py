from random import randint as rdi

def battleON(player,enemy):
    turn = 1
    while (player.hp > 0) and (enemy.hp > 0):
        
        print(f"TURN", turn)
        print(f"{player.name}\t{enemy.name}")
        print(f"(Level: {player.lvl})\t(Level:{enemy.lvl})")
        print(f"HP: {player.hp}/{player.maxHP}     \tHP: {enemy.hp}/{enemy.maxHP}")
        print(f"MP: {player.mp}/{player.maxMP}")
        
        

        if player.prof == "kn":
            print("you a knight")
            break
        if player.prof == "ba":
            pass
        if player.prof == "ma":
            pass
        if player.prof == "ar":
            pass

        checkHP()  

        enemyAttack()
        checkHP()
        
        turn += 1

def checkHP():
    if player.hp <= 0:
        print('me ded')
        pass
    if enemy.hp <= 0:
        print('you ded')
        pass

def enemyAttack():
    moveset = rdi(1,3)
    if moveset == 1:
        pass
    if moveset == 2:
        pass
    if moveset == 3:
        pass