import math

def space():
    print("         ")
def hyphen():
    print("---")
def Else():
    print("Invalid input. You do not attempt to escape anymore. You eventually die of pneumonia.")

space()
print("You wake up. You do not know where you are. You look around and see that you are in a run down hospital room.")
print("There are lights flashing and you see a piece of paper on the door that states: CONTAMINATED AREA, HAZARDOUS GAS IN AIR.")
print("You freak out. You have to get out!!! You begin your escape. You run to the door, swing it open, and see two signs. For the remainder of your escape, press 1 for OPTION 1 and press 2 for OPTION 2.")
space()
option = int(input("The one pointing to the left says MORGUE and the right one says PEDIACTRICS. Type 1 to go to the morgue and 2 for peds.\n"))

#go to morgue
if option == 1:
    space()
    print("You enter the morgue and flip on the lights, except they don't turn on. You take a look and feel around. It is very cold and smells fishy. You stumble upon a fridge and your stomach is growling. You do not know if opening it will be a good idea.")
    hyphen()
    option = int(input("Do you take the risk and OPEN THE FRIDGE to search for food or do you CONTINUE ON? \n"))
    space()
    #choose to OPEN FRIDGE
    if option == 1:
        space()
        print("You open the fridge. It is dark. You feel around and think you have found some jello. In your hallucinated state, you take a bite. Crunch! Crunch! Seconds later, you drop dead. The jello was actually a contaminated flatten eyeball.")
        space()
    #choose to CONTINUE ON
    elif option == 2:
        print("You leave the morgue and see someone running down the other hallway, you think this person is your only chance to get out safe. But is it actually a person...")
        hyphen()
        option = int(input("Do you CONTINUE ON or GO AFTER THE PERSON?\n"))
        space()
        #choose to CONTINUE ON
        if option == 1:
            print("You go to the basemant. You're not sure how to get out. You see an axe.")
            hyphen()
            option=int(input("Do you PICK UP THE AXE AND HACK FOR YOUR LIFE or TAKE A NAP?\n"))
            space()
            #choose to PICK UP AXE
            if option == 1:
                print("You took the axe and hack at the walls but you accidentally hit a water pipe. Water starts flowing and you drown.")
                space()
            #choose to TAKE A NAP
            elif option == 2:
                print("Your time runs out and you slowly die from the poisonus gas.")
            else:
                Else()
        #choose to GO AFTER PERSON
        elif option == 2:
            space()
            print("You ran after the person and it led you to the asylum. As you go through the door, it shuts and locks you in. You slowly soffocate to death.")
        else:
            Else()
    else:
        Else()

#go to peds
elif option == 2:
    print("You enter the peds wing. You see dingy toys lying in a corner. You hear the laughter of children vaguely in the background, but you know that no one is here. You feel feel strangly drawn to the area.")
    hyphen()
    option = int(input("Do you want to STAY AND PLAY WITH THE TOYS or GO TO THE WAITING AREA?\n"))
    #choose to STAY AND PLAY
    if option == 1:
        space()
        print("You stay with the toys. The laughter grows louder and louder until you can no longer stand it. You suddenly find it harder to breathe. You suffocate. You die.")
    #choose to go to WAITING AREA
    elif option == 2:
        space()
        print("You enter the waiting area. You scan around the room looking for an exit. In the corner of your eye, you spot a phone. Hope fills your soul. On the other side of the room, there is a dark door that says DO NOT ENTER. There's police tape and dried blood stains on the door. You see a hazard sign taped on the door. Clearly, this is a restricted area.")
        hyphen()
        option = int(input("Do you USE THE PHONE TO CALL FOR HELP or GO IN THE DOOR?\n"))
        #choose to PHONE FOR HELP
        if option == 1:
            space()
            print("You use the phone, but you realize that the line is disconnected. You lose all hope. You slowly roll yourself into a ball and die of malnourishment.")
        #choose to GO IN DOOR
        elif option == 2:
            space()
            print("You enter the room. There is a bunch of medication lying around the floor. There is also another door on the opposite side of the room.")
            hyphen()
            option = int(input("Do you TAKE SOME MEDICATION to reduce your anxiety or do you TRY THE DOOR?\n"))
            #choose to TAKE SOME MEDICATION
            if option == 1:
                space()
                print("You overdose and die.")
            #choose to TRY THE DOOR
            elif option == 2:
                space()
                print("The door easily opens. You hear birds chirping and the sun is just beginning to set. Congrats! You've made it out alive!")
            else:
                Else()
        else:
            Else()
    else:
        Else()
#if user inputs anything other than 1 or 2
else:
    print("Invalid input. You do not attempt to escape. You stay in the room and eventually die of pneumonia.")
