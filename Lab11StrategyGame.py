#Lab 11 Vasile Danciu, Josh Jones, Lavinia Uruc
#Spongebob SquarePants strategy text based game part 1

import random

def play():
  gameState = false
  printNow("******* Spongebob Squarepants Adventure Game *******")
  help()
  pineapple(gameState)

# exit function
def exit():
  printNow("Good bye Spongebob!")
  return

  # help function
def help():
  printNow("\nA long time ago in a Galaxy far, far away...\n")
  printNow("It is a time of great unrest as the evil Galactic Empire")
  printNow("continues to conquer, ensalve and ravage the free planets of")
  printNow("the galaxy. However, small bands of rebels have banded together") 
  printNow("to fight the tyranny of the Empire and seek to restore the freedom and") 
  printNow("justice known under the Old Republic. Unbeknownst to all, on the planet")
  printNow("Naboo, a lone rebel seeks to obtain and deliver plans of a new, terrible") 
  printNow("weapon created to crush the last vestiges of hope in the galaxy...")
  printNow("Welcome to the Star Wars Galaxy.  You will be able to explore eight worlds in this galaxy.")  
  printNow("On each world, you may jump to other select worlds by typing in one of the choices given.")
  printNow("You need to pick up the plans to the Death Star to stop the Empire.\n")
  printNow("Type \"help\" at any time to redisplay this introduction.")
  printNow("Type \"exit\" to quit the game at any time.\n")

# location one The Pineapple house
def pineapple(gameState):
  check = true
  # Description
  rmDesc = "------------ Pineapple house -----------\n"
  rmDesc += "You have arrived at the Naboo Spaceport.\n"
  rmDesc += "Naboo is a small pastoral world located\n"
  rmDesc += "near the border of the Outer Rim Territories.\n"
  rmDesc += "It is inhabited by two societies - an indigenous\n"
  rmDesc += "species of intelligent amphibians called the Gungans, and\n"
  rmDesc += "a group of peaceful humans who are referred to as the Naboo.\n" 
  rmDesc += "Destination choices are: \n Squidward's house,Sandy's house, The Krusty Krab, or EXIT to quit.\n"
  printNow (rmDesc)
  # destination choice loop
  while check == true:
    dstChc = "Where would you like to go, Spongebob?\n"
    dstChc += "Type 'west' to go to Squidward's house\n"
    dstChc += "Type 'south' to go to Sandy's house\n"
    dstChc += "Type 'east' to go to the Krusty Krab\n"
    dstChc += "Type 'help' for game info.\n"
    dstChc += "or just type 'exit' to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "west": # for Squidward's house
      check = false
      squidward(gameState)
    elif choice == "south": # for Sandy's house
      check = false
      sandy(gameState)
    elif choice == "east": # for Krusty Krab
      check = false
      krusty(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north":
      printNow("You cannot go "+ chc +" from here, try west, east, south, or type EXIT to quit.")
      check = true

# location two Squidward's house
def squidward(gameState):
  check = true
  # Description
  rmDesc = "------------ Squidward's house -----------\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "Destination choices are: \n Patrick's house, Pineapple house, or EXIT to quit.\n"
  printNow(rmDesc)
  # destination choice loop
  while check == true:
    dstChc = "Where would you like to go, Spongebob?\n"
    dstChc += "Type 'west' to go to Patrick's house\n"
    dstChc += "Type 'east' to go to the Pineapple house\n"
    dstChc += "Type 'help' for game info.\n"
    dstChc += "or just type 'exit' to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "west": # for Patrick's house
      check = false
      patrick(gameState)
    elif choice == "east": # for Pineapple house
      check = false
      pineapple(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "south":
      printNow("You cannot go "+ chc +" from here, try west, east, or type EXIT to quit.")
      check = true

# location three Patrick's house
def patrick(gameState):
  check = true
  # Description
  rmDesc = "------------ Patrick's house -----------\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "Destination choices are: \n Jellyfish Fields, Squidward's house, or EXIT to quit.\n"
  printNow(rmDesc)
  # destination choice loop
  while check == true:
    dstChc = "Where would you like to go, Spongebob?\n"
    dstChc += "Type 'south' to go to the Jellyfish Fields\n"
    dstChc += "Type 'east' to go to Squidward's house\n"
    dstChc += "Type 'help' for game info.\n"
    dstChc += "or just type 'exit' to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "south": # for Jellyfish Fields
      check = false
      jelly(gameState)
    elif choice == "east": # for Squidward's house
      check = false
      squidward(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "west":
      printNow("You cannot go "+ chc +" from here, try south, east, or type EXIT to quit.")
      check = true

# location four the Jellyfish Fields
def jelly(gameState):
  check = true
  # Description
  rmDesc = "------------ Jellyfish Fields -----------\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "Destination choices are: \n Patrick's house, Sandy's house, or EXIT to quit.\n"
  printNow(rmDesc)
  # destination choice loop
  while check == true:
    dstChc = "Where would you like to go, Spongebob?\n"
    dstChc += "Type 'north' to go to Patrick's house\n"
    dstChc += "Type 'east' to go to Sandy's house\n"
    dstChc += "Type 'help' for game info.\n"
    dstChc += "or just type 'exit' to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for Patrick's house
      check = false
      patrick(gameState)
    elif choice == "east": # for Sandy's house
      check = false
      sandy(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south" or chc == "west":
      printNow("You cannot go "+ chc +" from here, try north, east, or type EXIT to quit.")
      check = true

#location five Sandy's house
def sandy(gameState):
  check = true
  # Description
  rmDesc = "------------ Sandy's house -----------\n"
  rmDesc += "You have arrived at Sandy's glass dome house.\n"
  rmDesc += "description\n"
  rmDesc += "description\n"
  rmDesc += "description\n"
  rmDesc += "description\n"
  rmDesc += "Destination choices are: \n Jellyfish Fields, Pineapple house, the Chum Bucket, or EXIT to quit.\n"
  printNow (rmDesc)
  # destination choice loop
  while check == true:
    dstChc = "Where would you like to go, Spongebob?\n"
    dstChc += "Type 'north' to go to the Pineapple house\n"
    dstChc += "Type 'west' to go to the Jellyfish Fields\n"
    dstChc += "Type 'east' to go to the Chum Bucket\n"
    dstChc += "Type 'help' for game info.\n"
    dstChc += "or just type 'exit' to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for the Pineapple house
      check = false
      pineapple(gameState)
    elif choice == "west": # for the Jellyfish Fields
      check = false
      jelly(gameState)
    elif choice == "east": # for the Chum Bucket
      check = false
      chum(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south":
      printNow("You cannot go "+ chc +" from here, try west, east, north, or type EXIT to quit.")
      check = true


# location six the Chum Bucket
def chum(gameState):
  check = true
  # Description
  rmDesc = "------------ Chum Bucket -----------\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "Destination choices are: \n The Krusty Krab, Sandy's house, or EXIT to quit.\n"
  printNow(rmDesc)
  # destination choice loop
  while check == true:
    dstChc = "Where would you like to go, Spongebob?\n"
    dstChc += "Type 'north' to go to The Krusty Krab\n"
    dstChc += "Type 'west' to go to Sandy's house\n"
    dstChc += "Type 'help' for game info.\n"
    dstChc += "or just type 'exit' to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for The Krusty Krab
      check = false
      krusty(gameState)
    elif choice == "west": # for Sandy's house
      check = false
      sandy(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south" or chc == "east":
      printNow("You cannot go "+ chc +" from here, try north, west, or type EXIT to quit.")
      check = true


# location seven The Krusty Krab
def krusty(gameState):
  check = true
  # Description
  rmDesc = "------------ The Krusty Krab -----------\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "description line.\n"
  rmDesc += "Destination choices are: \n the Pinneaple house, the Chum Bucket, or EXIT to quit.\n"
  printNow(rmDesc)
  # destination choice loop
  while check == true:
    dstChc = "Where would you like to go, Spongebob?\n"
    dstChc += "Type 'south' to go to the Chum Bucket\n"
    dstChc += "Type 'west' to go to the Pineapple house\n"
    dstChc += "Type 'help' for game info.\n"
    dstChc += "or just type 'exit' to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "south": # for the Chum Bucket
      check = false
      chum(gameState)
    elif choice == "west": # for the Pineapple house
      check = false
      pineapple(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "east":
      printNow("You cannot go "+ chc +" from here, try south, west, or type EXIT to quit.")
      check = true

play()