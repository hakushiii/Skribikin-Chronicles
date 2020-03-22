from random import randint as rdi

def battleON(player,enemy):

    def checkHP():
        if player.hp <= 0:
            print(f"{player.name} has fainted.")
            player.hp = player.maxHP
            player.mp = player.maxMP
            #goto town

        if enemy.hp <= 0:
            print(f"{enemy.name} has fainted.")
            player.xp += player.xp + (enemy.lvl*2)
            print(f"{player.name} has gained {enemy.lvl}XP!")
            if player.xp >= player.lvlNXT:
                player.xp = player.lvlNXT - player.xp
                player.lvlNXT = player.lvlNXT + 5
                player.lvl += 1
                print(f"{player.name} has leveled up!, is now level {player.lvl}")

    turn = 1
    while (player.hp > 0) and (enemy.hp > 0):
        
        print(f"\tTURN", turn)
        print(f"{player.name}\t\t{enemy.name}")
        print(f"(Level: {player.lvl})\t\t(Level:{enemy.lvl})")
        print(f"HP: {player.hp:.2f}/{player.maxHP:.2f}     \tHP: {enemy.hp:.2f}/{enemy.maxHP:.2f}")
        print(f"MP: {player.mp:.2f}/{player.maxMP:.2f}")
        
        print(f"\n1. Basic\t2. Skill\t3.Item\tX. Run")
        if player.prof == "KNIGHT":
            action = str(input(">"))
            if action == "1":
                player.basic(enemy)
            if action == "2":
                player.slash(enemy)
            if action == "3":
                pass
            if action == "X" or action == "x":
                chance = rdi(1,10)
                if chance > 5:
                    print("You have escaped.")
                    break
                if chance <= 5:
                    print("You have failed to flee.")
        if player.prof == "BARBARIAN":
            action = str(input(">"))
            if action == "1":
                player.basic(enemy)
            if action == "2":
                player.heavy(enemy)
            if action == "3":
                pass
            if action == "X" or action == "x":
                chance = rdi(1,10)
                if chance > 5:
                    print("You have escaped.")
                    break
                if chance <= 5:
                    print("You have failed to flee.")
        if player.prof == "MAGE":
            action = str(input(">"))
            if action == "1":
                player.basic(enemy)
            if action == "2":
                player.fireBall(enemy)
            if action == "3":
                pass
            if action == "X" or action == "x":
                chance = rdi(1,10)
                if chance > 5:
                    print("You have escaped.")
                    break
                if chance <= 5:
                    print("You have failed to flee.")
        if player.prof == "ARCHER":
            action = str(input(">"))
            if action == "1":
                player.basic(enemy)
            if action == "2":
                player.powerShot(enemy)
            if action == "3":
                pass
            if action == "X" or action == "x":
                chance = rdi(1,10)
                if chance > 5:
                    print("You have escaped.")
                    break
                if chance <= 5:
                    print("You have failed to flee.")

        checkHP()
        if (player.hp <= 0) or (enemy.hp <= 0):
            break

        enemy.attack(player)

        checkHP()
        if (player.hp <= 0) or (enemy.hp <= 0):
            break
        
        turn += 1