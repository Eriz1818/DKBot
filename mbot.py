import DraganKnight
import random
import time

game = DraganKnight.DraganKnight()
game.login("username", "password")

# Bot Game Loop
while True:
    try:
        time.sleep(5)
        if game.tp <= 30:
            print "Travelling to town 1 to recover ...."
            game.go_town(1)
            game.get_rest()
            continue

        if (abs(game.x_coord) > 180 or abs(game.y_coord) > 170) and game.tp < 30 and not game.is_fighting():
            print "Travelling to safe area..."
            game.go_town(1)
            continue

        if (abs(game.x_coord) > 180 or abs(game.y_coord) > 170) and not game.is_fighting():
            print "Travelling to safe area..."
            game.go_town(4)
            continue

        if (abs(game.x_coord) < 90 or abs(game.y_coord) < 90) and not game.is_fighting():
            print "Travelling outside...."
            game.go_town(4)
            continue

        if game.is_fighting() and not game.is_dead():
            print "Enemy Found. Attacking..."
            if game.hp < 40:
                print "Running from fight...."
                game.run_from_fight()
                continue
            game.do_melee_attack()
            continue

        if game.hp < 50 and game.mp > 50:
            print "Health low. Casting Breath spell..."
            game.do_fast_spell(4)  # Breath Spell
            continue

        if game.hp < 50 and game.mp > 25:
            print "Health low. Casting life spell..."
            game.do_fast_spell(3)  # Life Spell
            continue

        if game.hp < 50 and game.mp > 15:
            print "Health low. Casting revive spell..."
            game.do_fast_spell(2)  # Revive Spell
            continue

        if game.hp < 50 and game.mp > 10:
            print "Health low. Casting healing spell..."
            game.do_fast_spell(1)  # Healing Spell
            continue

        if (game.hp < 45 or game.mp < 10) and game.tp < 35:
            print "Health low and Mana... Resting in Town 1..."
            game.go_town(1)
            game.get_rest()
            continue

        if game.hp < 45 or game.mp < 10:
            print "Health low and Mana... Resting in Town 4..."
            game.go_town(4)
            game.get_rest()
            continue

        game.go_direction(random.choice(["north", "east", "south", "west"] + ["north", "east"] * 2))

        print "X: %s Y: %s Level: %s XP: %s Gold: %s HP: %s MP: %s TP: %s" % (
            game.x_coord, game.y_coord, game.level, game.exp, game.gold, game.hp, game.mp, game.tp)

    except Exception, e:
        print "Error Occured: %s Trying in 10 seconds." % e
        time.sleep(10)
