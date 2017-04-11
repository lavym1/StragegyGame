#Lab 13 Vasile Danciu, Josh Jones, Lavinia Uruc
#Spongebob SquarePants strategy text based game with added SNAZZ

object1picked = false #spatula
object2picked = false #krabby patty
object3picked = false #secret formula
name = requestString("Enter your name:")
def play():
  printNow("******* Spongebob Squarepants Adventure Game *******")
  printNow("Are you ready, kids?")
  printNow("Aye, aye, captain!")
  printNow("I can't hear you!")
  printNow("Aye, aye, captain!")
  help()
  pineapple()

# exit function
def exit():
  printNow("Good bye Spongebob!")
  return

# help function
def help():
  global name
  descr = "Hi," + name + "! "
  descr+= "How to play the game:"
  descr+= "\nYour mission is to pick a Krabby Patty from the Krusty Krab and take it to Patrick's house. "
  descr+="You are going to need a spatula to pick the krabby patty! "
  descr+="To travel from one location to another, "
  descr+="type a word like 'north', 'south', 'west',or 'east' to reach a destination. "
  descr+="You can also pick objects at some locations by typing 'pick object_name'. "
  descr+="Type 'help' at any time to redisplay this introduction. "
  descr+="Type 'exit' to quit the game at any time."
  showInformation(descr)
  #showInformation("nHow to play the game: \nYour mission is to pick a Krabby Patty from the Krusty Krab and take it to Patrick's house. You are going to need a spatula to pick the krabby patty! To travel from one location to another, type a word like 'north', 'south', 'west',or 'east' to reach a destination. You can also pick objects at some locations by typing 'pick object_name'.\nType 'help' at any time to redisplay this introduction.\nType 'exit' to quit the game at any time.")

###################################
# location one: The Pineapple house
###################################
def pineapple():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ Pineapple house ~~~~~~~~~~~~\n"
  descr += "You have arrived at the Pineapple house.\n"
  descr += "This is your home. You live in a pineapple house under the sea\n"
  descr += "with your pet snail Gary, \n"
  descr += "There is a not totally obvious SECRET room inside the Pineapple House.\n"
  descr += "If you type the name of the pet snail you might gain entrance\n"
  descr += "If you go to work at Krusty Krab, type 'pick spatula' to take your frying spatula\n"
  descr += "Destination choices are: \n Squidward's house,Sandy's house, The Krusty Krab, or EXIT to quit.\n"
  printNow (descr)
  
  # destination choice loop
  while check == true:
    dirChc = "You are in the PINEAPPLE HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'west' to go to Squidward's house\n"
    dirChc += "Type 'south' to go to Sandy's house\n"
    dirChc += "Type 'east' to go to the Krusty Krab\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "west": # for Squidward's house
      check = false
      squidward()
    elif choice == "south": # for Sandy's house
      check = false
      sandy()
    elif choice == "east": # for Krusty Krab
      check = false
      krusty()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "gary": # to the secret room
      check = false
      gary()
    elif chc == "pick spatula": # to the secret room
      global object1picked
      object1picked = true
      printNow("You have picked the spatula!")
    elif chc == "north":
      printNow("You cannot go "+ chc +" from here, try west, east, south, or type EXIT to quit.")
      check = true

#################################
# location two: Squidward's house
#################################
def squidward():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ Squidward's house ~~~~~~~~~~~~\n"
  descr += "The Squidward's House is located west of the Pineaple House.\n"
  descr += "Squidward is a cranky octopus who dislikes neighbors.\n"
  descr += "Try not to spend to much time here.\n"
  descr += "Squidward could get angry and you could not finish your mission in time.\n"
  descr += "Visit other neighbors.\n"
  descr += "Destination choices are: \n Patrick's house, Pineapple house, or EXIT to quit.\n"
  printNow(descr)
  
  # destination choice loop
  while check == true:
    dirChc = "You are in SQUIDWARD'S HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'west' to go to Patrick's house\n"
    dirChc += "Type 'east' to go to the Pineapple house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "west": # for Patrick's house
      check = false
      patrick()
    elif choice == "east": # for Pineapple house
      check = false
      pineapple()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "south":
      printNow("You cannot go "+ chc +" from here, try west, east, or type EXIT to quit.")
      check = true

#################################
# location three: Patrick's house
#################################
def patrick():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ Patrick's house ~~~~~~~~~~~~\n"
  descr += "The house is a large brown rock with a wind vane on top.\n"
  descr += "Like a door, the rock has hinges to open and close. \n"
  descr += "The front yard has a long black path connecting the front of the rock and Conch Street.\n"
  descr += "Your best friend, Patrick Star lives here.\n"
  descr += "He is an unintelligent and overweight pink sea star,\n"
  descr += "and he is very hungry for a KRABBY PATTY!\n"
  descr += "Destination choices are: \n Jellyfish Fields, Squidward's house, or EXIT to quit.\n"
  printNow(descr)
  
  if (object2picked == true):#if player has object2picked (the patty), he wins the game
    showInformation("Congratulations " + name + ", you won the game! Patrick ate the delicious krabby patty!\nGame Over")
    check = false
    exit()
  
  # destination choice loop
  while check == true:
    dirChc = "You are in PATRICK'S HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'south' to go to the Jellyfish Fields\n"
    dirChc += "Type 'east' to go to Squidward's house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "south": # for Jellyfish Fields
      check = false
      jelly()
    elif choice == "east": # for Squidward's house
      check = false
      squidward()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "west":
      printNow("You cannot go "+ chc +" from here, try south, east, or type EXIT to quit.")
      check = true

#####################################
# location four: the Jellyfish Fields
#####################################
def jelly():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ Jellyfish Fields ~~~~~~~~~~~~\n"
  descr += "A vast area in which over 4 million jellyfish reside.\n"
  descr += "Other creatures live here such as clams, leeches, and poisonous sea urchins.\n"
  descr += "You come here wih Patrick to have fun catching jellyfishes with your nets \n"
  descr += "Destination choices are: \n Patrick's house, Sandy's house, or EXIT to quit.\n"
  printNow(descr)
  
  # destination choice loop
  while check == true:
    dirChc = "You are at the JELLYFISH FIELDS\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'north' to go to Patrick's house\n"
    dirChc += "Type 'east' to go to Sandy's house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for Patrick's house
      check = false
      patrick()
    elif choice == "east": # for Sandy's house
      check = false
      sandy()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south" or chc == "west":
      printNow("You cannot go "+ chc +" from here, try north, east, or type EXIT to quit.")
      check = true

#############################
#location five: Sandy's house
#############################
def sandy():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ Sandy's house ~~~~~~~~~~~~\n"
  descr += "You have arrived at your friend Sandy Cheeks glass dome house, the Treedome\n"
  descr += "It is air-locked and contains no water, the only place in Bikini Bottom where Sandy can survive without her suit.\n"
  descr += "Its floor is covered in grass, and features a large tree, which contains Sandy's living quarters. \n"
  descr += "The Treedome also humorously includes a giant hamster wheel, among other backyardish things.\n"
  descr += "The dome produces snow during the winter\n"
  descr += "Destination choices are: \n Jellyfish Fields, Pineapple house, the Chum Bucket, or EXIT to quit.\n"
  printNow (descr)
  # destination choice loop
  while check == true:
    dirChc = "You are in SANDY'S HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'north' to go to the Pineapple house\n"
    dirChc += "Type 'west' to go to the Jellyfish Fields\n"
    dirChc += "Type 'east' to go to the Chum Bucket\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for the Pineapple house
      check = false
      pineapple()
    elif choice == "west": # for the Jellyfish Fields
      check = false
      jelly()
    elif choice == "east": # for the Chum Bucket
      check = false
      chum()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south":
      printNow("You cannot go "+ chc +" from here, try west, east, north, or type EXIT to quit.")
      check = true

###############################
# location six: the Chum Bucket
###############################
def chum():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ Chum Bucket ~~~~~~~~~~~~\n"
  descr += "Located directly across the street from the Krusty Krab.\n"
  descr += "Evil Plankton serves awful food here\n"
  descr += "He is always trying to steal the Krabby Patty secret Formula.\n"
  descr += "The restaurant looks like a bucket with a blue hand (could be a glove).\n"
  descr += "Destination choices are: \n The Krusty Krab, Sandy's house, or EXIT to quit.\n"
  printNow(descr)
  
  if (object3picked == true):# if player went to Chum Bucket with object3picked (secret formula), he loses the game
    global name
    showInformation("Plankton stole your Krabby Patty Secret Formula, " + name + " and you lost the game!\nGame Over")
    check = false
    exit()
  
  # destination choice loop
  while check == true:
    dirChc = "You are at the CHUM BUCKET\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'north' to go to The Krusty Krab\n"
    dirChc += "Type 'west' to go to Sandy's house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for The Krusty Krab
      check = false
      krusty()
    elif choice == "west": # for Sandy's house
      check = false
      sandy()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south" or chc == "east":
      printNow("You cannot go "+ chc +" from here, try north, west, or type EXIT to quit.")
      check = true

################################
# location seven The Krusty Krab
################################
def krusty():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ The Krusty Krab ~~~~~~~~~~~~\n"
  descr += "A fast food restaurant located in Bikini Bottom, founded and owned by Eugene H. Krabs.\n"
  descr += "It is the most popular restaurant in Bikini Bottom. Mr. Krabs loves money!\n"
  descr += "This is were you work as a fry cook.\n"
  descr += "If you have your spatula with you, you can pick a delicious krabby patty!\n"
  descr += "To pick a krabby patty type 'pick patty'\n"
  descr += "To pick the Krabby Patty Secret Formula type 'pick formula'\n"
  descr += "Destination choices are: \n the Pinneaple house, the Chum Bucket, or EXIT to quit.\n"
  printNow(descr)
  
  # destination choice loop
  while check == true:
    dirChc = "You are at THE KRUSTY KRAB\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'south' to go to the Chum Bucket\n"
    dirChc += "Type 'west' to go to the Pineapple house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "south": # for the Chum Bucket
      check = false
      chum()
    elif choice == "west": # for the Pineapple house
      check = false
      pineapple()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "pick patty":
      if object1picked == true: # player has the spatula required to pick krabby patty
        global object2picked
        object2picked = true
        printNow("You have picked the krabby patty! Now take it to Patrick to win the game")
      else:
        printNow("You need to pick the spatula from the Pineaple house FIRST!")
        printNow("Go back to the Pineapple house, type 'pick spatula', and then come back.")
    elif chc == "pick formula": # to pick the secret formula
      global object3picked
      object3picked = true
      printNow("You have picked the krabby patty secret formula! Do not take it to the Chum Bucket!!!!")
    elif chc == "north" or chc == "east":
      printNow("You cannot go "+ chc +" from here, try south, west, or type EXIT to quit.")
      check = true

############
#SECRET ROOM
############
def gary():
  check = true
  
  # Description
  descr = "~~~~~~~~~~~~ Gary's secret room ~~~~~~~~~~~~\n"
  descr += "You found the SECRET ROOM where your belowed pet snail hides sometimes\n"
  descr += "Gary is a domesticated house pet with similar mannerisms to a cat, but has royal blood,\n"
  descr += "Gary has great intelligence (at least for a snail).\n"
  descr += "Gary is known for his characteristic 'meow'- in contrast to the barking of the sea worms\n"
  descr += "Destination choice is: \n the Pinneaple house, or EXIT to quit.\n"
  printNow(descr)
  
  # destination choice loop
  while check == true:
    dirChc = "You are in GARY'S SECRET ROOM\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'pineapple' to exit Garry's SECRET room\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "pineapple": # for the Pineapple house
      check = false
      pineapple()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "east" or chc == "west" or chc == "south":
      printNow("You cannot go "+ chc +" from here, try 'pineapple' to exit the secret room, or type EXIT to quit.")
      check = true


play()