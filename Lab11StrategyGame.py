#Lab 11 Vasile Danciu, Josh Jones, Lavinia Uruc
#Spongebob SquarePants strategy text based game part 1

def play():
  printNow("******* Spongebob Squarepants Adventure Game *******")
  help()
  pineapple()

# exit function
def exit():
  printNow("Good bye Spongebob!")
  return

  # help function
def help():
  printNow("\nHow to play the game\n")
  printNow("description line how to play ")
  printNow("description line how to play ")
  printNow("description line how to play ")
  printNow("description line how to play ")
  printNow("description line how to play ")
  printNow("Type 'help' at any time to redisplay this introduction.")
  printNow("Type 'exit' to quit the game at any time.\n")

# location one The Pineapple house
def pineapple():
  check = true
  # Description
  descr = "------------ Pineapple house -----------\n"
  descr += "You have arrived home at the Pineapple house.\n"
  descr += "description\n"
  descr += "more descriptions.\n"
  descr += "more descriptions.\n"
  descr += "more descriptions.\n"
  descr += "Destination choices are: \n Squidward's house,Sandy's house, The Krusty Krab, or EXIT to quit.\n"
  printNow (descr)
  # destination choice loop
  while check == true:
    dirChc = "Where would you like to go, Spongebob?\n"
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
    elif chc == "north":
      printNow("You cannot go "+ chc +" from here, try west, east, south, or type EXIT to quit.")
      check = true

# location two Squidward's house
def squidward():
  check = true
  # Description
  descr = "------------ Squidward's house -----------\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "Destination choices are: \n Patrick's house, Pineapple house, or EXIT to quit.\n"
  printNow(descr)
  # destination choice loop
  while check == true:
    dirChc = "Where would you like to go, Spongebob?\n"
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

# location three Patrick's house
def patrick():
  check = true
  # Description
  descr = "------------ Patrick's house -----------\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "Destination choices are: \n Jellyfish Fields, Squidward's house, or EXIT to quit.\n"
  printNow(descr)
  # destination choice loop
  while check == true:
    dirChc = "Where would you like to go, Spongebob?\n"
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

# location four the Jellyfish Fields
def jelly():
  check = true
  # Description
  descr = "------------ Jellyfish Fields -----------\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "Destination choices are: \n Patrick's house, Sandy's house, or EXIT to quit.\n"
  printNow(descr)
  # destination choice loop
  while check == true:
    dirChc = "Where would you like to go, Spongebob?\n"
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

#location five Sandy's house
def sandy():
  check = true
  # Description
  descr = "------------ Sandy's house -----------\n"
  descr += "You have arrived at Sandy's glass dome house.\n"
  descr += "description\n"
  descr += "description\n"
  descr += "description\n"
  descr += "description\n"
  descr += "Destination choices are: \n Jellyfish Fields, Pineapple house, the Chum Bucket, or EXIT to quit.\n"
  printNow (descr)
  # destination choice loop
  while check == true:
    dirChc = "Where would you like to go, Spongebob?\n"
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


# location six the Chum Bucket
def chum():
  check = true
  # Description
  descr = "------------ Chum Bucket -----------\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "Destination choices are: \n The Krusty Krab, Sandy's house, or EXIT to quit.\n"
  printNow(descr)
  # destination choice loop
  while check == true:
    dirChc = "Where would you like to go, Spongebob?\n"
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


# location seven The Krusty Krab
def krusty():
  check = true
  # Description
  descr = "------------ The Krusty Krab -----------\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "description line.\n"
  descr += "Destination choices are: \n the Pinneaple house, the Chum Bucket, or EXIT to quit.\n"
  printNow(descr)
  # destination choice loop
  while check == true:
    dirChc = "Where would you like to go, Spongebob?\n"
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
    elif chc == "north" or chc == "east":
      printNow("You cannot go "+ chc +" from here, try south, west, or type EXIT to quit.")
      check = true

play()