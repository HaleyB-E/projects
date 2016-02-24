from collections import Counter

#this doesn't get used anywhere but it's nice to have - only contains the mundanes!
propertyDict = { 'fluidity': ['sulphur', 'water', 'air', 'gold', 'silver', 'magnesium'],
                 'solidity': ['salt','earth','iron','tin','lead','stone'],
                 'life': ['mercury','water','air','gold','copper','magnesium'],
                 'death': ['fire','iron','arsenic'],
                 'luxury': ['fire','gold','silver','antimony','cinnabar'],
                 'spirit': ['sulphur','mercury','air','fire','bismuth'],
                 'binding': ['salt','earth','gold','lead','arsenic','stone'],
                 'freeing': ['sulphur','mercury','air','fire','silver'],
                 'destroying': ['sulphur','fire','iron','tin','lead','magnesium'],
                 'creating': ['salt','earth','water','copper','antimony'],
                 'displacing': ['mercury','silver'],
                 'concealing': ['mercury','earth','silver','antimony','magnesium','cinnabar'],
                 'revealing': ['fire','iron','bismuth','stone'],
                 'healing': ['water','tin','bismuth'],
                 'harming': ['copper','arsenic','magnesium','cinnabar'],
                 'summoning': ['sulphur','silver','copper','lead','bismuth'],
                 'banishing': ['tin','antimony','arsenic','stone','cinnabar']}

typeDict = { 'salt': ['solidity','binding','creating'],
             'sulphur': ['fluidity','spirit','freeing','destroying','summoning'],
             'mercury': ['life','spirit','freeing','concealing','displacing'],
             'earth': ['solidity','binding','creating','concealing'],
             'water': ['fluidity','life','creating','healing'],
             'air': ['fluidity','life','spirit','freeing'],
             'fire': ['death','luxury','spirit','freeing','destroying','revealing'],
             'gold': ['fluidity','life','luxury','spirit','binding'],
             'silver': ['fluidity','luxury','freeing','concealing','summoning','displacing'],
             'copper': ['life','creating','harming','summoning'],
             'iron': ['solidity','death','destroying','revealing'],
             'tin': ['solidity','destroying','healing','banishing'],
             'lead': ['solidity','binding','destroying','summoning'],
             'antimony': ['luxury','creating','concealing','banishing'],
             'arsenic': ['death','binding','harming','banishing'],
             'bismuth': ['spirit','revealing','healing','summoning'],
             'magnesium': ['fluidity','life','destroying','concealing','harming'],
             'stone': ['solidity','binding','revealing','banishing'],
             'cinnabar': ['luxury','concealing','harming','banishing'],
             'calcination': ['solidity','death','binding','concealing','healing','summoning'],
             'congelation': ['solidity','creating','healing','displacing'],
             'fixation': ['life','binding','revealing','displacing'],
             'dissolution': ['fluidity','death','freeing','destroying','concealing','banishing'],
             'digestion': ['death','revealing','harming','displacing'],
             'distillation': ['spirit','binding','healing','summoning'],
             'sublimation': ['fluidity','freeing','harming','banishing'],
             'separation': ['death','freeing','harming','banishing'],
             'incineration': ['death','spirit','freeing','destroying','revealing','harming'],
             'fermentation': ['spirit','creating','healing','displacing'],
             'multiplication': ['life','creating','revealing','displacing'],
             'projection': ['spirit','concealing','summoning','displacing']}

wardDict = { 'government armour':['life','creating','binding','spirit'],
             'dodge':['fluidity','displacing','freeing','healing'],
             'fratbro armour': ['solidity','displacing','banishing','healing'],
             'reflect':['spirit','displacing','concealing','healing'],
             'heal maim':['healing','solidity','creating','binding'],
             'vanish':['concealing','fluidity','displacing','summoning'],
             'damage up':['death','harming','destroying','revealing'],
             'maim':['harming','fluidity','destroying','freeing'],
             'root':['harming','solidity','binding','revealing'],
             'fear':['banishing','harming','death','spirit'],
             'block wych-kin':['displacing','concealing','banishing','fluidity'],
             'bind wych-kin':['binding','harming','life','spirit'],
             'damage up to wych-kin':['harming','spirit','death','revealing'],
             'extend duration':['binding','creating','life','solidity']}

wardDifficulty = { 'government armour':1,
                   'dodge':5,
                   'fratbro armour':5,
                   'reflect':5,
                   'heal maim':1,
                   'vanish':5,
                   'damage up':1,
                   'maim':1,
                   'root':1,
                   'fear':5,
                   'block wych-kin':10,
                   'bind wych-kin':5,
                   'damage up to wych-kin':10,
                   'extend duration':10}

wardEffectNoItem = { 'government armour':"take 1 damage, gain 1 armour: ward",
                   'dodge':"whether it hits you or not, take the first called effect by a wych-kin in the next combat you're in",
                   'fratbro armour':"You lose all of 1 type of armour you have",
                   'reflect':"You can't interact with mechanics (except combat and stealth abilities being done to you) for 5 minutes",
                   'heal maim':"You get 1 call of heal maim, root to all within ZoC",
                   'vanish':"Put on a silver headband for 5 minutes. You cannot interact physically with the world for that long and look like a ghost",
                   'damage up':"Your next attack deals 0 damage",
                   'maim':"You may throw 1 Maim packet, but upon doing so are rooted for 5 minutes",
                   'root':"You may throw 1 Root packet, but upon doing so are maimed for 5 minutes",
                   'fear':"You may not get within ZoC of other people for 5 minutes",
                   'block wych-kin':"Wych-kin are drawn by this place's energies - tape the Ward up to the wall and remove it in an hour or write the end time on it clearly",
                   'bind wych-kin':"You get the sense that wych-kin will be more drawn to you than usual for the next hour (GM, tell npcs)",
                   'damage up to wych-kin':"For the next hour, wych-kin in this location will deal +1 damage on every 3rd shot - tape the Ward to the wall and remove it in an hour or write the end time on it clearly",
                   'extend duration':"any ward effects on you cut in half - round down"}

wardEffectWithItem = { 'government armour':"You gain 1 armour:ward on yourself and can bestow 1 armour:ward on someone else",
                   'dodge':"You gain 1 dodge vs. wych-kin",
                   'fratbro armour':"For the next 6 hours, you gain 1 Armour:Ward per hour",
                   'reflect':"Up to 5 minutes after you are hit with an attack incant (NOT an elemental type), you may attach that incant to one of your attacks. Works once, then Ward is expended",
                   'heal maim':"You may immediately recover from a MAIM effect once",
                   'vanish':"",
                   'damage up':"Your next attack to wych-kin deals 2 more damage than it otherwise would",
                   'maim':"You may call MAIM once against a wych-kin",
                   'root':"You may call ROOT once against a wych-kin",
                   'fear':"You may call FEAR once against a wych-kin",
                   'block wych-kin':"wych-kin cannot pass through the place that the Ward was constructed for the next hour - tape it up on the wall and write BLOCK on it-remove in an hour or write end time clearly on it",
                   'bind wych-kin':"binds wych-kin magically to not attack players (or allows you to attack with BIND for the next hour)",
                   'damage up to wych-kin':"For the next hour, each PC deals +1 damage to wych-kin every 3rd attack - tape it up on the wall and write the effect, remove it in an hour or write the end time clearly on it",
                   'extend duration':"any ward effects on you double (doubling armour ward stacks)"}

while(1):
    #loops until you've added all the elements from the ward
    elementList = []
    print("Hints for ward checker: 'sulphur' is spelled weird! Also, if there are multiple of the"+
              " same glyph in the ward it does not change the effect")
    while(1):
        value = raw_input("What elements are in the Ward? (press return to finish) ")
        if len(value) > 0:
            while value not in typeDict:
                value = raw_input("Input not found! Try again. ")
            elementList.append(value)
        else:
            break
    print "The contents of the Ward are: "
    print elementList

    print "\n Possible tagged properties are..."
    propertyList = []
    for item in elementList:
        propertyList.append(typeDict[item])

    propertyCount = Counter()

    for item in propertyList:
        propertyCount.update(item)

    print(propertyCount)
    dict(propertyCount)
            
    validWards = dict()

    #lvl 1 only
    for ward in wardDict:
        tagging = dict()

        #account for difficulty with these:
        numGlyphs = 3
        numProps = 2
        if wardDifficulty[ward] == 5:
            numGlyphs = 5
            numProps = 3
        elif wardDifficulty[ward] == 10:
            numGlyphs = 10
            numProps = 5
            
        if len(elementList) < numGlyphs:
            print "Ward " + ward + " fails - not enough glyphs"
        else:

            #grabs every property only demonstrated by one glyph
            for prop in wardDict[ward]:
                if propertyCount[prop] == 1:
                    for item in propertyList:
                        if prop in item:
                            tagging[elementList[propertyList.index(item)]]= prop
                            break

            #fills out with rest of useful elements
            for element in elementList:
                if element not in tagging.keys():
                    for prop in wardDict[ward]:
                        if prop in propertyList[elementList.index(element)]:
                            tagging[element] = prop
                            break
                        
            #test if luxury is present
            if numGlyphs == 10:
                for item in propertyList:
                    if 'luxury' in item:
                        element = elementList[propertyList.index(item)]
                        if element in tagging:
                            tagging[element]='luxury'
                        break

        if (len(tagging.keys()) > 2) and (len(set(tagging.values())) > 1):
            fail = 0
            for element in elementList:
                if element not in tagging:
                    print "Ward " + ward + " fails - junk glyph"
                    fail = 1
                    break
            if fail == 0:
                print "Ward " + ward + " is valid!"
                validWards[ward] = tagging
        else:
            print "Ward " + ward + " fails - not enough properties"
            
    if len(validWards) == 0:
        print "\nNo valid wards!"

    else:
        showfull = raw_input("\nPress 'v' for full list of properties tagged, anything else for summary ")
        for key in validWards:
            if showfull is "v":
                print "\nWard effect '" + key + "' creatable by tagging:"
                print validWards[key]
            else:
                print "\nWard effect '" + key + "' creatable with these glyphs."

    while(1):
        wardtoshow = raw_input("\nWhich effect do you want to see? (press return to skip) ")
        if len(wardtoshow) > 0:
            while wardtoshow not in validWards.keys():
                wardtoshow = raw_input("\nThat wasn't a valid ward with these elements! Try again: ")
            itemtoggle = "a"
            while (not (itemtoggle[0] is "y")) and (not(itemtoggle[0] is "n")):
                itemtoggle = raw_input("\nDid they have correct items for every symbol in the ward? (y/n) ")
            print "\n"
            if itemtoggle[0] is "y":
                print wardEffectWithItem[wardtoshow]
            else:
                print wardEffectNoItem[wardtoshow]
        else:
            break

    tryagain = raw_input("Try a new ward? (press 'q' to quit) ")
    if tryagain is "q":
        break
print 'done'