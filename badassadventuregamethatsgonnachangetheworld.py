import random

print("Adventure game!")

print()

print("At all questions, please answer in lower case letters")

print()

# User Name

un = input("Please enter Your Name here: ")
s = input("What species do you wish to be? ('sa fantasy world, go nuts):")

print()
print("----------------------------------------------------------------")
print()

print("Hello ", un.title(), "! Welcome to my adventure game!")

print()

# Start Variables

dj = 0

h = 100
print("Your starting Health is ", h)

xp = 0
print("Your starting XP is ", xp)

c = 50
print("Your starting Cash is ", c)

k = 0
print("Your starting Karma is", k, "(this is neutral, don't worry)")

f = 0
print("You have", f, "friends. In the game.")
print()
input("")
# Ogre attack

print("A huge ogre is standing in your way! What do you do?")
print()

print("Do you:")
print("A) Try to Befriend it?")
print("B) Run and hide?")
print("C) Try to fight it?")
a1 = input("Answer here:")

if a1 == ("a" or "A" or " a" or " A"):
    print()
    print("The ogre roars with laughter, and lets you run away unharmed")
    print()
    print("Note that ogres do not befriend anyone")

if a1 == ("b" or "B" or " b" or " B"):
    h = h - random.randint(10, 20)

    print()
    print("You escape, but the ogre takes a chunk out of you as you run.")

    print()
    print("Current health:", h)

if a1 == ("c" or "C" or " c" or " C"):
    h = h - random.randint(50, 75)

    print()
    print("The ogre strikes you where you stand before you can get a punch in, but kindly lets you limp off")

    print()
    print("Current health:", h)

print()

# The Woods

print("Well done! You survived your first encounter, and are now walking forwards, into the woods.")
print("This is a text based game, but as the Master, I must tell you, it is beautiful where you are.")
print("Sucks for you that I'm not better at coding.")
input("")

print()

print("Anyway, you see a small bird to the side of the path! What do you do?")

print("A) Step on it for no reason(MWAHAHAHAHA!)")
print("B) Reach up and help it into it's nest ")
print("C) Ignore it ")
a2 = input("Answer here:")

if a2 == ("a" or "A" or " a" or " A"):
    k = k - 20
    c = c - 5
    h = h - 10
    dj = dj + 5

    print("You are a lemming. I, as Game Master, now dislike you, and smite you for my own amusement.")
    print()

    print("Your health is now:", h)
    print("Your cash is now:", c)
    print("Your karma is now:", k)
    input("")

    print()
    print("If you think this is unfair, take it up with the developers.")
    print()
    input("")

    print("YOU HAVE A NEW STAT!")
    print("Developer Judgement:", dj)
    print("This affects nothing in the game, it just amuses me. You may earn my respect back.")
    input("")

if a2 == ("b" or "B" or " b" or " B"):
    c = c + 10
    h = h - 5

    print("As you return the baby bird to it's nest, it bites you!")
    print("However, the mother gives you some shiny things it found in compensation!")
    input("")

    print("Your cash is now:", c)
    print("Your health is now:", h)

if a2 == ("c" or "C" or " c" or " C"):
    dj = dj + 1

    print("-_- You are playing an adventure game you uncooked mushroom. Know that I am judging you.")
    print()
    input("")

    print("YOU HAVE A NEW STAT!")
    print("Developer Judgement:", dj)
    print("This affects nothing in the game, it just amuses me. You may earn my respect back.")
    input("")

print()

# Forest Path

if a2 == ("a" or "A" or " a" or " A"):
    print("After brutally murdering a defenceless baby bird and making the developer of the game you are playing hate "
          "you, you decide to walk on.")
    print("You immediately trip over a stone.")
    input("")

    print()

    print("Do you:")
    print("A) shoot your hands out")
    print("B) trust that the Developer won't be petty")
    print("C) try to regain balance")
    print()
    z=input("Answer here:")

    if z == ("a" or "A" or " a" or " A"):
        c = c - 1
        h = h - 1

        print()
        print(
            "You show good reasoning, and only lightly graze your hands. Some money falls out of your pocket, "
            "however you do not notice this.")
        input("")

        print("Current health:", h)
        print("Current cash:", c)

    if z == ("b" or "B" or " b" or " B"):
        h = h - 5
        dj = dj + 1
        c = c - 5

        print("You utter buffoon. You have learned nothing of the Game God.")
        print(
            "You smash your face, engraving some twigs in it. Much money falls  out of your pocket, but you do not "
            "notice through the pain.")
        print()

        print("Current health:", h)
        print("Current cash:", c)
        print("Amount I am judging you:", dj)

    if z == ("c" or "C" or " c" or " C"):
        c = c - 5

        print("You hilariously overestimate your abilities so early on in the game. You do not regain balance, "
              "however manage to fall on your shoulder, resulting in no harm to your health. However, much money "
              "falls out of your pocket unnoticed.")

        print("Current cash:", c)

    print()

if a2 == ("b" or "B" or " b" or " B"):
    print()

    c = c + 5

    print("After rescuing a defenceless baby bird, you find a small bag of gold!")
    print("You have", c, "cash")
    print()

print("You continue on, leaves crunching underfoot. You check carefully for traps, as pixie numbers are strong here. "
      "Up ahead, you see three paths. One leads to the castle, one leads to the sea, and one  leads further into the "
      "forest.")
print("I know full well this is far too generic, but I am thirteen years old and coding a thing. Back off.")
print()

print(
    "After judging the Developer (who has full control over how you do in this game), you realise you are yet to make "
    "a decision.")
print()

print("A) The castle")
print("B) The sea")
print("C) The forest, further")
print()

a3 = input("Answer here:")
print()

if a3 == ("a" or "A" or " a" or " A"):

    print("You walk towards the castle, probably endeavouring to rob it within an inch of it's inanimateness")
    print("I may permit this, but know that the royals are well into spy novels.")
    print("Therefore, they hide things in cool places.")
    print("You know the ancient egyptian grave robbers?")
    print("You may be so lucky.")
    input("")

    print("As you walk up, you notice there is a guard outside the gate, armed to the teeth.")
    print("Literally, its a Serpentooth, known for having small, psychic snakes live in their teeth and spit venom on "
          "wish.")
    print("Wacky imagination I have, I thought that up on the spot.")
    input("")

    print("Do you:")
    print("A) Try to seduce the guard")
    print("B) Try to convince the guard to rebel against The System")
    print("C) Try to kill the guard")
    print()

    aa1 = input("Answer here:")
    print()

    if aa1 == ("a" or "A" or " a" or " A"):
        print("The guard flushes uncomfortably. 'I am so sorry, I'm actually a heterosexual...'")
        print()
        print("Note: Due to the multitude of genders, sexes and species in the dating pool in this world, straights "
              "are rare.")
        print()
        print("'... so I'm not interested. Really sorry.' In the awkward tangle, they neglect your papers. You are "
              "through!")
        print()

    if aa1 == ("b" or "B" or " b" or " B"):
        print("")


# Game Rules

if h > 20:
    print()
    print("Your health is far too low! You must buy health potions!")
    print()

    p = input("What potion would you like to buy?"
              "A) +25 health (£5) "
              "B) +50 health (£10) "
              "C) +75 health (£15)"
              "Answer here:")

    if p == ("a" or "A" or " a" or " A"):
        h = (h + 25)
        c = (c - 5)

        print("Your health is now", h)
        print("Your cash is now", c)

    if p == ("b" or "B" or " b" or " B"):
        h = (h + 50)
        c = (c - 10)

        print("Your health is now", h)
        print("Your cash is now", c)

    if p == ("c" or "C" or " c" or " C"):
        h = (h + 75)
        c = (c - 15)

        print("Your health is now", h)
        print("Your cash is now", c)

if h <= 0:
    if k == 0:
        dj = dj + 100
        print("You had a neutral game life, and are going to a beige house to eat raw mushrooms in the afterlife.")

    if k > 0:
        print(
            "You had a positive game life, and are going to have a wonderful afterlife. Trust me, I thought it up, "
            "and gee whiz is it cool.")

    if k < 0:
        print(
            "You had a negative game life, and I'm not even going to describe game hell because you will puke. Trust "
            "me, I thought it up.")

    print(
        "You may have noticed how funny I am. Why not go back and try different combinations to experience more of my "
        "humour?")
