'''Made for Writing for Interactive Media by Anne Botwinik using Python.'''

letter = False
cheese = 0
cheeseEat = 0
def cheeseFunc(func):
  global cheese
  global cheeseEat
  print("Do you eat or pocket the cheese?")
  options = ["eat", "pocket", "quit"]
  userInput = ""
  while userInput not in options:
    print("Options: ")
    for i in options:
      print(" ==== ", i, end = ' ===== ')
    print("")
    userInput = input()
    if userInput == options[0]:
      print("You ate the cheese!")
      cheeseEat = cheeseEat + 1
      func()
    elif userInput == options[1]:
      print("You pocketed the cheese!")
      cheese = cheese + 1
      print("You have " +str(cheese)+ " cheeses!")
      func()
    elif userInput == options[2]:
      quit()
    else: 
      print("Please enter a valid option.")
def outside():
  print("")
  print("You suddenly notice the door to the apartment open. A young woman steps out - she is dressed very nice! You can hear her bickering.")
  print("'No Mom, I know she's a nice girl! But the meeting with my bosses - I know I know! I like her a lot. I just worry - A workaholic?! No, no... Mom, I've got to go. Love you too!'")
  print("")
  print("Follow the woman down the sidewalk? Or go through the window?")
  choices2("sidewalk", "window", sidewalk, thruWindow2)
def next2():
  print("")
  print("The woman picks up the briefcase and leaves.")
  inside()
def briefcase():
  print("")
  print("The woman picks up the briefcase, which you are now in! She walks out the door...")
  print("She walks out down the sidewalk...")
  office()
def office():
  global letter
  print("And onto a bus you go!")
  print("Now she gets off the bus, and into a building!")
  print("The woman sets the briefcase down.")
  if letter is True:
    print("You remember the letter you have... Now's your chance to show the woman the letter!")
    print("Or you could not show her at all!")
    choices2("now", "never", goodEnd, businessEnd)
  elif letter is False:
    businessEnd()
def businessEnd():
  print("")
  print("The woman has a meeting with her bosses.")
  print("The bosses say what a wonderful job she's been doing, and how she seems to prioritize work over everything else.")
  print("The woman sighs, but agrees.")
  print("The bosses say they will be giving her a promotion!")
  print("=== Promotion Ending ===")
  quit()
def goodEnd():
  global cheese
  print("")
  print("You push the letter out of the bag and onto the floor.")
  print("The woman spots the letter... and picks it up!")
  print("'Huh, must have been put in my bag,' the woman ponders to herself.")
  print("She opens it and reads it. She gasps, and takes her phone out.")
  print("")
  print("'Hello? Jane! I got your letter... I'll meet you at the park right now!'")
  print("She grabs the briefcase and runs out the door. 'Where are you going?' you hear someone say.")
  print("'I'm so sorry, I've got to reschedule the meeting! I'm busy!' The woman shouts behind her.")
  goodEnd2()
def goodEnd2():
  global cheese
  print("")
  print("The woman rushes to the park. There she stops abruptly. 'Jane?' She says, softly.")
  print("You, as a rat, realize they may need some privacy, so you jump out and hide in a bush. There you find some cheese!")
  cheese = cheese + 1
  print("You look back to see the two of them kissing. <3")
  print("=== Romantic Ending ===")
  quit()
def sadEnd():
  global letter
  print("")
  print("A different young woman sits on a bench by the bush. She sighs, and pulls out a wax seal with a heart on it.")
  print("She tosses the wax seal into the bush, right by you.")
  if letter is True:
    print("It looks just like the wax seal on the letter you have. It seems like she couldn't work up the courage to ask that other woman out.")
  print("The woman looks defeated. You hope the best for her in the future.")
  print("=== Sad Ending ===")
  quit()
def grabCheese():
  print("")
  print("You scurry and grab the cheese. No one seems to notice you... yet.")
  cheeseFunc(inside)
def grabCheese2():
  print("")
  print("You scurry and grab the cheese. No one seems to notice you... yet.")
  cheeseFunc(cheeseEnd)
def findCheeseTrash():
  print("")
  print("You keep inspecting the trash. You find a delicious cheese!")
  cheeseFunc(outside)
def house1():
  print("")
  print("You hop through the open window and into the apartment. There you see a young woman rushing around, getting dressed up in a business suit and packing a briefcase.")
  print("An older woman sits at the breakfast table, sipping coffee.")
  print("The woman is talking, '... and she was nervous, y'know? I was nervous too! She seemed to want to tell me something, but I'm not sure what. But my phone rang and I had to go.'")
  print("As the woman is talking, you notice she puts down her briefcase right next to you. You could jump in! At the same time, however, you notice a beautiful piece of cheese sitting on the counter...")
  choices2("jump", "cheese", briefcase, grabCheese)
def bakery():
  global letter
  print("")
  print("You are now at the bakery. There, a young woman sits sadly. She's wearing a name tag with the name 'Jane'")
  print("By her feet, a purse sits. On the counter, some cheese sits.")
  if letter is True:
    print("Now's your chance! Put Jane's letter in her bag, remind her to never give up! Or... You could go for the cheese.")
    choices2("letter", "cheese", giveLetter, grabCheese2)
  if letter is False:
    print("If only you had a way to cheer her up. Ah well. Go grab that cheese!")
    grabCheese2()
  quit()
def giveLetter():
  print("")
  print("You carefully place the letter in Jane's bag.")
  print("Jane sniffles, and reaches into the bag. She brushes the letter and looks down, surprised.")
  print("Jane grabs the letter, confused. Suddenly she perks up. She pickes up her phone.")
  print("'Judy? Judy! Hey, I was wondering if you could meet me at the park? I have something to tell you...")
  print("Judy hurredly picks up her things and rushes to the park, and you follow her.")
  print("She sits on the bench expectedly.")
  goodEnd2()
def cheeseEnd():
  print("")
  print("Looks like you've collected so much cheese!")
  print("You've collected " + str(cheese) + " cheeses!")
  print("You've eaten " + str(cheeseEat) + " cheeses!")
  print("=== Cheese Ending ===")
  quit()
def explore():
  print("As you explore you notice a nice picnic with a baby throwing food everywhere.")
  print("Wait... is that baby throwing... cheese?!")
  print("Go get some!")
  cheeseFunc(cheeseEnd)
def park():
  print("")
  print("You are now at the park! So much to see! Do you explore or sit in the bush nearby, and people watch?")
  choices2("explore", "bush", explore, sadEnd)
  quit()
def bus():
  print("")
  print("As you wait at the bus stop, the young woman waits to board the bus. From where you are, it seems her briefcas is the perfect height to hop in...")
  print("You hop into her briefcase!")
  office()
def sidewalkFirst():
  print("")
  print("As you walk down the sidewalk, a young woman rushes past you")
  sidewalk()
def sidewalk():
  print("")
  print("You come upon a park, right across the street from a bakery. Right in the middle is a bus stop.")
  print("Decisions decisions! Do you go to the park, the bakery, or wait at the bus stop?")
  choices3("park", "bakery", "bus", park, bakery, bus)
def thruWindow2():
  print("")
  print("An older woman sits at the breakfast table, sipping coffee. You notice a beautiful piece of cheese sitting on the counter...")
  grabCheese()
def inside():
  print("")
  print("Now that you have collected cheese, should you keep looking for more cheese? Or continue on your way? Leave or stay?")
  choices2("leave", "stay", getOut, catEnd)
def catEnd():
  print("")
  print("You scurry around looking for more cheese.")
  print("Suddenly an adorable blue eyed ragdoll cat creeps around the corner...")
  print("Time slows down. Perhaps it was hubris, to keep looking for this much cheese...")
  print("As you regret all decisions that have led up to this moment, the last thing you see are shiny white teeth. As the world goes dark, all you smell is fishbreath.")
  print("=== Get Got! Ending ===")
  quit()
def getOut():
  print("You hop out through the window and walk down the sidewalk.")
  sidewalk()
def findLetter():
  global letter
  print("")
  print("You found a pretty letter with a wax heart on it! Letter added to inventory!")
  letter = True
  print("The letter says:")
  print("")
  print("---- Dear Jane, I must confess I am in love with you! Meet me at the park this afternoon at noon sharp :) ----")
  print("")
  print("Keep searching for trash? Or go through the window? Or down the sidewalk?")
  choices3("trash", "window", "sidewalk", findCheeseTrash, house1, sidewalk)

def introScene():
  print("")
  print("You are outside an apartment complex this morning, in search of tasty trash food.")
  print("You see in front of you a trash can, an open window, or a sidewalk. What do you do?")
  choices3("trash", "window", "sidewalk", findLetter, house1, sidewalkFirst)

def choices2(type1, type2, choice1, choice2):
  options = [type1, type2, "quit"]
  userInput = ""
  while userInput not in options:
    print("Options: ")
    for i in options:
      print(" ==== ", i, end = ' ===== ')
    print("")
    userInput = input()
    if userInput == options[0]:
      choice1()
    elif userInput == options[1]:
      choice2()
    elif userInput == options[2]:
      quit()
    else: 
      print("Please enter a valid option.")
def choices3(type1, type2, type3, choice1, choice2, choice3):
  options = [type1, type2, type3, "quit"]
  userInput = ""
  while userInput not in options:
    print("Options: ")
    for i in options:
      print(" ==== ", i, end = ' ===== ')
    print("")
    userInput = input()
    if userInput == options[0]:
      choice1()
    elif userInput == options[1]:
      choice2()
    elif userInput == options[2]:
      choice3()
    elif userInput == options[3]:
      quit()
    else: 
      print("Please enter a valid option.")
def quit():
  print("")
  print("Thanks for playing!")
  exit()

if __name__ == "__main__":
  while True:
    print("")
    print("=========== Rat Game ===========")
    print("Welcome to the beautiful city of Seattle. You are a rat.")
    print("Your sole goal is to scavange for trash.")
    print("Whatever else happens is up to you.")
    print("")
    print("Let's start with your name, rat: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()
