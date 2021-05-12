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

d = 0

h = 100
print("Your starting Health is ", h)

x = 0
print("Your starting XP is ", x)

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
aa = input("Answer here:")

if aa == ("a" or "A" or " a" or " A"):
    print()
    print("The ogre roars with laughter, and lets you run away unharmed")
    print()
    print("Note that ogres do not befriend anyone")

if aa == ("b" or "B" or " b" or " B"):
    h = h - random.randint(10, 20)

    print()
    print("You escape, but the ogre takes a chunk out of you as you run.")

    print()
    print("Current health:", h)

if aa == ("c" or "C" or " c" or " C"):
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
ab = input("Answer here:")

if ab == ("a" or "A" or " a" or " A"):
    k = k - 20
    c = c - 5
    h = h - 10
    d = d + 5

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
    print("Developer Judgement:", d)
    print("This affects nothing in the game, it just amuses me. You may earn my respect back.")
    input("")

if ab == ("b" or "B" or " b" or " B"):
    c = c + 10
    h = h - 5

    print("As you return the baby bird to it's nest, it bites you!")
    print("However, the mother gives you some shiny things it found in compensation!")
    input("")

    print("Your cash is now:", c)
    print("Your health is now:", h)

if ab == ("c" or "C" or " c" or " C"):
    d = d + 1

    print("-_- You are playing an adventure game you uncooked mushroom. Know that I am judging you.")
    print()
    input("")

    print("YOU HAVE A NEW STAT!")
    print("Developer Judgement:", d)
    print("This affects nothing in the game, it just amuses me. You may earn my respect back.")
    input("")

print()

# Forest Path

if ab == ("a" or "A" or " a" or " A"):
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
    ac = input("Answer here:")

    if ac == ("a" or "A" or " a" or " A"):
        c = c - 1
        h = h - 1

        print()
        print(
            "You show good reasoning, and only lightly graze your hands. Some money falls out of your pocket, "
            "however you do not notice this.")
        input("")

        print("Current health:", h)
        print("Current cash:", c)

    if ac == ("b" or "B" or " b" or " B"):
        h = h - 5
        d = d + 1
        c = c - 5

        print("You utter buffoon. You have learned nothing of the Game God.")
        print(
            "You smash your face, engraving some twigs in it. Much money falls  out of your pocket, but you do not "
            "notice through the pain.")
        print()

        print("Current health:", h)
        print("Current cash:", c)
        print("Amount I am judging you:", d)

    if ac == ("c" or "C" or " c" or " C"):
        c = c - 5

        print("You hilariously overestimate your abilities so early on in the game. You do not regain balance, "
              "however manage to fall on your shoulder, resulting in no harm to your health. However, much money "
              "falls out of your pocket unnoticed.")

        print("Current cash:", c)

    print()

if ab == ("b" or "B" or " b" or " B"):
    print()

    c = c + 5

    print("After rescuing a defenceless baby bird, you find a small bag of gold!")
    print("You have", c, "cash")
    print()

print("You continue on, leaves crunching underfoot. You check carefully for traps, as pixie numbers are strong here. "
      "Up ahead, you see three paths. One leads to the castle, one leads to the sea, and one leads further into the "
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

ad = input("Answer here:")
print()

# Castle

if ad == ("a" or "A" or " a" or " A"):

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

    ae = input("Answer here:")
    print()

    if ae == ("a" or "A" or " a" or " A"):
        print("The guard flushes uncomfortably. 'I am so sorry, I'm actually a heterosexual...'")
        print()
        print("Note: Due to the multitude of genders, sexes and species in the dating pool in this world, straights "
              "are rare.")
        print()
        print("'... so I'm not interested. Really sorry.' In the awkward tangle, they neglect your papers. You are "
              "through!")
        input("")

        print("Once inside, you come across three rooms in your immediate line of vision.")
        print("What do you do?")
        print("A) The throne room (get looting over and done with)")
        print("B) Staff room (potential for disguise)")
        print("C) Cellars (secret treasures?)")

        af = input("Answer here: ")
        print()

        if af == ("a" or "A" or " a" or " A"):

            print("You burst into the throne room, at which point you are met with an awful sight.")
            print("To you.")
            input("")
            print("The ruler is sitting there, coated in jewels and a veritable Taj Mahal balanced on their head.")
            input("")
            print("You try and retreat, but they have spotted you and begin to open their mouth, their lips painted "
                  "with expensive purple dye.")
            print("'How dare you burst into my throne room, and stand before me in those tattered rags, you "
                  "filthy", s, "!'")
            print("You stammer over a lie, but before you can utter the first word of your improvised story, "
                  "you are thrown from the castle by two boorish trolls with serious underbites.")
            input("")

            ag=input("You must find another way in (A), or you could give up and turn your efforts elsewhere (B)."
                  " What's it gonna be?: ")

            if ag == ("a" or "A" or " a" or " A"):
                print("You decide to *hem* lay siege to the castle. You can't get through via guard, so you must "
                      "climb through a high and tiny window.")
                input("")

                print("How to get there? If only there was a multiple choice for this kind of thing... ")
                input("")
                print("oh wait!")
                input("")

                print("A) Grappling hook"
                      "B) Manually"
                      "C) I give up.")

                ah=input("Answer here: ")

                if ah == ("a" or "A" or " a" or " A"):
                    print()
                    print("This option was here to give you false hope. You're going up with hands mate.")

                if (ah == ("b" or "B" or " b" or " B")) or (ah == ("a" or "A" or " a" or " A")):

                    print("You are going to ascend to the top of the tower on the off chance you can fit through a "
                          "small window.")
                    input("")
                    print("Only hands")
                    input("")
                    print("Brave. (For a ", s, ")")
                    input("")
                    
                    
                    
                                      
                    

            if ((ag == ("a" or "A" or " a" or " A")) or (ah == ("c" or "C" or " c" or " C"))):
                d=d+1
                print("Wimp. 'Just give up as soon as things get rough', you thought, ''snot like anyone's watching', "
                      "you thought.")
                input("")
                print("I'm watching.")
                input("")
                print("Amount I am  judging you:", d)

    if ae == ("b" or "B" or " b" or " B"):
        print("'...and that's why you should abandon your post and help me rob them!'")
        print("The Serpentooth nods slowly.")
        print("'You're right. I have been here for 10 years and have yet to get a promotion. I stand here, all day, "
              "every day, minimum wage, which I can't even live off, and I don't even get extra when there's acid "
              "rain! They even charge me when I use their plasters! Cheeky buggers. I'll march you in.'")
        print("You are through!")


# Game Rules

if (h > 20):
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

if (h <= 0):
    if k == 0:
        d = d + 100
        print("You had a neutral game life, and are going to a beige house to eat raw mushrooms in the afterlife.")

    if k > 0:
        print(
            "You had a positive game life, and are going to have a wonderful afterlife. Trust me, I thought it up, "
            "and gee whiz is it cool.")

    if k < 0:
        print(
            "You had a negative game life, and I'm not even going to describe game hell because you will puke. Trust "
            "me, I thought it up.")

print("You may have noticed how funny I am. Why not go back and try different combinations to experience more of my "
      "humour?")

print("Soz, haven't coded anymore, check back in I've got some good ideas")
