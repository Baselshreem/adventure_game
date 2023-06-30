import time
import random

def print_pause(statment_printer):
    #this is a function to puse a masge 
    print(statment_printer)
    time.sleep(2)
    
def description():
    #this is a func use a puse a masge to description player 
    print_pause("Welcome to the adventure game. Thank you for choosing.\n")
                
    print_pause("Now you have reached the adventure game. There are two basic options in the game. A menu will be displayed to choose to start.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("There are slight differences in terms of the easy and difficult level of the game.\n")

 


def Start_Play(items, option):
    # Things that happen when the player fights  
    print_pause("Enter 1 to house or 2 cave.")
    print_pause("What would you like to do?")
    
    choice1 = input("(Please enter 1 or 2.)\n")
    if choice1 == '1':
        print_pause("\n\n\nThank you Home has been selected to play.\n\n\n")
        house(items, option)
         
    elif choice1 == '2':
        print_pause("\nThank you cave has been selected to play.")
        cave(items, option)
        
        
def cave(item, option):
    if "mona" not in item:
         
        print_pause("\nUnsuccessful selection, please play again.\n")
    while True:
      choi = input("Would you like to (1) start agin  or (2) Repeat_Play ""run away?")
      
      if choi == '1':
          
           if "mona" in item:
               print_pause("\nThank you successful .")
      
      
      
           else:
              print_pause("\nGood luck, please try again..\n")
              item.append("mona")
              Start_Play(item, option)    
    
    
      if choi == '2':
        Repeat_Play()
        break
 
    
def house(items, option):
    # Things that happen to the player in the house
 
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
   Start_Play(items, option)
 else:
   print_pause("backe playe ")
   Repeat_Play()
 

 
def Repeat_Play():
    # Things that happen when the player runs back to the field
    print_pause("\n.The game is restarting\n")    
    repeat = input("Would you like to repeat again, please select 1-OK 2-I do not agreen")
    
    if repeat == '1':
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif repeat == '2':
        print_pause("\n\n\n Thanks see you later.\n\n\n")
    else:
        Repeat_Play()
        
 

def play_game():
    items = []
    option = random.choice(["Basil", "Mohamad", "asad","shraime","sile","dina"])
    description()#function used a print and push a masge on screen to descrip game 
    Start_Play(items, option)#this is a call start game and tow parmeter the first items and socond is option random 



play_game()
