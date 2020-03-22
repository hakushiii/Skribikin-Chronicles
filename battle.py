from random import randint as rdi

def battleON(player,enemy):

    def checkHP():
        if player.hp <= 0:
            print(f"{player.name} has fainted.")

        if enemy.hp <= 0:
            print(f"{enemy.name} has fainted.")

    def enemyAttack():
        moveset = rdi(1,3)
        if moveset == 1:
            pass
        if moveset == 2:
            pass
        if moveset == 3:
            pass

    turn = 1
    while (player.hp > 0) and (enemy.hp > 0):
        
        print(f"\tTURN", turn)
        print(f"{player.name}\t{enemy.name}")
        print(f"(Level: {player.lvl})\t(Level:{enemy.lvl})")
        print(f"HP: {player.hp}/{player.maxHP}     \tHP: {enemy.hp}/{enemy.maxHP}")
        print(f"MP: {player.mp}/{player.maxMP}")
        
        print("\n1. Basic\t2. Skill\tX. Run")
        if player.prof == "kn":
            action = str(input(">"))
            if action == "1":
                pass
            if action == "2":
                player.slash(enemy)
            if action == "X" or "x":
                pass
        if player.prof == "ba":
            action = str(input(">"))
            if action == "1":
                pass
            if action == "2":
                player.heavy(enemy)
            if action == "X" or "x":
                pass
        if player.prof == "ma":
            action = str(input(">"))
            if action == "1":
                pass
            if action == "2":
                player.fireBall(enemy)
            if action == "X" or "x":
                pass
        if player.prof == "ar":
            action = str(input(">"))
            if action == "1":
                pass
            if action == "2":
                player.powerShot(enemy)
            if action == "X" or "x":
                pass

        checkHP()
        if (player.hp <= 0) or (enemy.hp <= 0):
            break

        enemyAttack()
        checkHP()
        if (player.hp <= 0) or (enemy.hp <= 0):
            break

        turn += 1
