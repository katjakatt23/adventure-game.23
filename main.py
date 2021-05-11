print("Adventure game!")

print()

print("At all questions, please answer in lower case letters")

print()

#User Name

un=input("Please enter Your Name here:")

print()
print("----------------------------------------------------------------")
print()

print("Hello ", un.title(), "! Welcome to my adventure game!")

print()

#Start Variables

h=(100)

print("Your starting health is ", h)

print()

xp=(0)

print("Your starting XP is ", xp)

print()

c=(50)

print("Your starting cash is ", c)

print()

#Ogre attack

print("A huge ogre is standing in your way! What do you do?")

act=input("Do you: A) Try to Befriend it? B) Run and hide? C) Try to fight it? (no caps answer):")

if act=="a":

    print()
    print("The ogre roars with laughter, and lets you run away unharmed")
    print()
    print("Note that ogres do not befriend anyone")
    print()

if act=="b":

    import random
    h=(h-(random.randint(10, 20)))

    print()
    print("You escape, but the ogre takes a chunk out of you as you run.")
    print()
    print("Current health:", h)
    print()

if act=="c":

    import random
    h=(h-(random.randint(50,75)))

    print()
    print("The ogre strikes you where you stand, before you can get a punch in, but kindly lets you limp off")
    print()
    print("Current health:", h)

#The Woods

#Game Rules

if h<=20:
    print("Your health is far too low! You must buy health potions!")
    print()

    p=input("What potion would you like to buy? A) +25 health (£5) B) +50 health (£10) C) +75 health (£15)")

    if p=="a":

        h=(h+25)
        c=(c-5)

        print("Your health is now", h)
        print("Your cash is now", c)

if h<=0:
    print("You are now dead. I, the game master, congratulate you, as I made the game and therefore know what the afterlife is like for you, and gee whizz, you're doin' good.")