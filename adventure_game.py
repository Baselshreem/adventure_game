import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)
    
def intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
                
    print_pause("Rumor has it that a "  + " is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")

 


def fight(items, option):
    # Things that happen when the player fights  
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(items, option)
            break
        elif choice1 == "2":
            cave(items, option)
            break
        
def cave(item, option):
    if "sward" not in item:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou walk back to the field.\n")
    while True:
      choi = input("Would you like to (1) fight or (2) ""run away?")
      
      if choi == '1':
          
           if "sward" in item:
               print_pause("\nYou peer cautiously into the cave.")
      
      
      
           else:
              print_pause("\nYou peer cautiously into the cave.")
              print_pause("\nIt turns out to be only a very small cave.")
              print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
              print_pause("\nYou have found the magical Sword of Ogoroth!")
              print_pause("\nYou discard your silly old dagger and take "
                    "the sword with you.")
              print_pause("\nYou walk back out to the field.\n")
              item.append("sward")
              fight(item, option)    
    
    
      if choi == '2':
        print_pause("\nYou run back into the field. ""\nLuckily,you don't seem to have been ""followed.\n")
          
        field()
        break
 
    
def house(items, option):
    # Things that happen to the player in the house
 print_pause("\n\n\nThank you Home has been selected to play.\n\n\n")
 choise = input("1. Enter through the door\n"
                "2. Entry from the window\n")
                  
 if choise == '1':
      print_pause("\n\n\nThank you for making the right choice ...\n\n\n")
      againe = input("Would you like to play again? (y/n)").lower()
      
 
      if againe == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        house(items, option)
      else:
       print_pause("\n\n\nThank you for making the right choice ...\n\n\n")
 elif choise == '2':     
   print_pause("game over ")
   print_pause("restart selected another choices,   method game ")
   fight(items, option)
 else:
   print_pause("backe playe ")
   field()
 

 
def field():
    # Things that happen when the player runs back to the field
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        field()
        
 

def play_game():
    items = []
    option = random.choice(["wicked fairie", "pirate", "dragon","troll","gorgon"])
    intro()
    fight(items, option)


play_game()