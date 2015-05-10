# Victor Duan
# text-based Puzzle & Dragons damage calculator



def main():
    # blah = raw_input("enter fire combos: ").split()
    # print blah

    # print [int(x) for x in blah]
    # return

    # get team stats
    fire  = int(input("Enter fire damage:  "))
    water = int(input("Enter water damage: "))
    wood  = int(input("Enter wood damage:  "))
    dark  = int(input("Enter dark damage:  "))
    light = int(input("Enter light damage: "))
    heart = int(input("Enter recovery:     "))

    # total combo multiplier
    combos = int(input("\nEnter total number of combos: "))
    comboMultiplier = 1.0 + (float(combos) - 1) / 4.0

    # get orb matches
    print """Enter the number of orbs for each type. For each color, you may enter the orbs cleared
             with spaces between the combos. For example, if you cleared 2 sets of 3 and a set of 5,
             enter 3 3 5 (in any order)."""

    fireorb  = [int(x) for x in raw_input("Enter fire combos:  ").split()]
    waterorb = [int(x) for x in raw_input("Enter water combos: ").split()]
    woodorb  = [int(x) for x in raw_input("Enter wood combos:  ").split()]
    darkorb  = [int(x) for x in raw_input("Enter dark combos:  ").split()]
    lightorb = [int(x) for x in raw_input("Enter light combos: ").split()]
    heartorb = [int(x) for x in raw_input("Enter heart combos: ").split()]

    # calculate orb multipliers
    fireMultiplier  = sum([1.0 + (float(x) - 3) / 4.0 for x in fireorb])
    waterMultiplier = sum([1.0 + (float(x) - 3) / 4.0 for x in waterorb])
    woodMultiplier  = sum([1.0 + (float(x) - 3) / 4.0 for x in woodorb])
    darkMultiplier  = sum([1.0 + (float(x) - 3) / 4.0 for x in darkorb])
    lightMultiplier = sum([1.0 + (float(x) - 3) / 4.0 for x in lightorb])
    heartMultiplier = sum([1.0 + (float(x) - 3) / 4.0 for x in heartorb])

    print combos
    print len(fireorb + waterorb + woodorb + darkorb + lightorb + heartorb)
    # make sure combos match up
    assert (combos == len(fireorb + waterorb + woodorb + darkorb + lightorb + heartorb))
    # if (combos != len(fireorb + waterorb + woodorb + darkorb + lightorb + heartorb)):
    #     "Input doesn't match up. Make sure you entered combos correctly."
    #     return

    # Row enhance
    print "Enter the number of rows for each color, followed by the number of row enhance."

    fireRe  = [int(x) for x in raw_input("Enter fire rows and row enhance:  ").split()]
    waterRe = [int(x) for x in raw_input("Enter water rows and row enhance: ").split()]
    woodRe  = [int(x) for x in raw_input("Enter wood rows and row enhance:  ").split()]
    darkRe  = [int(x) for x in raw_input("Enter dark rows and row enhance:  ").split()]
    lightRe = [int(x) for x in raw_input("Enter light rows and row enhance: ").split()]

    # make sure these are entered correctly
    assert(len(fireRe) == len(waterRe) == len(woodRe) == len(darkRe) == len(lightRe) == 2)

    # get RE multipliers
    fireReMultiplier  = 1.0 + 0.1 * fireRe[0]  * fireRe[1]
    waterReMultiplier = 1.0 + 0.1 * waterRe[0] * waterRe[1]
    woodReMultiplier  = 1.0 + 0.1 * woodRe[0]  * woodRe[1]
    darkReMultiplier  = 1.0 + 0.1 * darkRe[0]  * darkRe[1]
    lightReMultiplier = 1.0 + 0.1 * lightRe[0] * lightRe[1]

    # leader attack multipliers
    leaderAtk1 = float(input("Enter leader skill 1 attack multiplier: "))
    leaderAtk2 = float(input("Enter leader skill 2 attack multiplier: "))
    leaderAtk = leaderAtk1 * leaderAtk2

    # leader RCV multipiers
    leaderRcv1 = float(input("Enter leader skill 1 recovery multiplier: "))
    leaderRcv2 = float(input("Enter leader skill 2 recovery multiplier: "))
    leaderRcv = leaderRcv1 * leaderRcv2



    # calculate damage and recovery
    fireDamage  = fire  * comboMultiplier * fireMultiplier  * fireReMultiplier  * leaderAtk
    waterDamage = water * comboMultiplier * waterMultiplier * waterReMultiplier * leaderAtk
    woodDamage  = wood  * comboMultiplier * woodMultiplier  * woodReMultiplier  * leaderAtk
    darkDamage  = dark  * comboMultiplier * darkMultiplier  * darkReMultiplier  * leaderAtk
    lightDamage = light * comboMultiplier * lightMultiplier * lightReMultiplier * leaderAtk
    recovery    = heart * comboMultiplier * heartMultiplier * leaderRcv

    # print out the damage
    print "Fire damage:  ", fireDamage
    print "Water damage: ", waterDamage
    print "Wood damage:  ", woodDamage
    print "Dark damage:  ", darkDamage
    print "Light damage: ", lightDamage
    print "\nTotal damage: ", fireDamage + waterDamage + woodDamage + darkDamage + lightDamage
    print "Recovery:     ", recovery



if __name__ == "__main__":
    main()
