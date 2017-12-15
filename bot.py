import DragonKnight
import random
import time

game = DragonKnight.DragonKnight()
game.login("eriz18", "testtest")

# Bot game loop
while True:
    try:
        time.sleep(5)  # Making sure we don't go hard on the server
        if game.is_fighting() and not game.is_dead():
            print "Enemy found. Attacking..."
            game.do_melee_attack()
            continue

        if game.hp < 50 and game.mp > 5:
            print "Health low. Casting healing spell..."
            game.do_fast_spell(1)  # Healing spell
            continue

        if game.hp < 35:
            print "Health low. Resting..."
            game.go_town(2)
            game.get_rest()
            continue

        game.go_direction(random.choice(["north", "east", "south", "west"] + ["north", "east"] * 2))

        print "X: %s Y: %s Level: %s XP: %s Gold: %s HP: %s MP: %s" % (
        game.x_coord, game.y_coord, game.level, game.exp, game.gold, game.hp, game.mp)
    except Exception, e:
        print "Error occured: %s. Trying again in 10 seconds." % e
        time.sleep(10)