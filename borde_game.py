#This is my script since long time of not coding in python.

import os

def main():
    # make some space in the termainal for better readability.
    giveSomeSpaceInTerminal()

    ####################################
    ##  Get the user's Data section  ###
    ####################################

    print("\033[92mSap NeueFische welcomes to the game of breaking the Bordomness\033[0m")
    print("\033[93mAre you bored?! Looking for some fun?!\033[0m")

    giveSomeSpaceInTerminal()

    while True:
        play = get_input("Do you want to play a game? (yes/no)")

        if play == "yes":
            print ("Great! Let's get started.")

            while True:
                getInput = get_input("Type manual or help to get the manual of the game:")
                if getInput.lower() in ["manual", "help"]:
                    manual()
                    break
                else:
                    print("\033[91mWARNING: Invalid command!\033[0m")
                    manual()

            #ask the user if they want to get advice.
            getAdvice = get_input("Do you want to get advice about your weight? (yes/no)")

            if getAdvice == "yes":
                print ("Great! Let's get started.")
                
                while True:
                    name, age, weight, height = get_user_data()

                    #Body Mass Index (BMI) is a numerical value used to estimate if an individual is at a healthy weight for their height
                    calc_print_BMI_categories(weight, height)
            else:
                print ("No worries! Maybe next time.")
        else:
            print ("No worries! Maybe next time. See Ya!")
            # Loop back to play prompt        


####################################
####   Functions section       #####
####################################
def giveSomeSpaceInTerminal():
    print ("\n \n \n")


def get_user_data():
    name   = get_input("What is your name? ")
    age    = get_input("What is your age? ")
    weight = get_input("What is your weight? ")
    height = get_input("What is your height? ")

    greet_user(name)
    
    return name, age, weight, height

#great the user
def greet_user(name):
    print ("Hello " + name )
    print ("welcome to the game of breaking the Bordom")

#manual of the game
def manual():
        print("\n######################################################    Manual of the game       ###########################################")
        print ("Break the Bordomness is a simple terminal game where you practice terminal commands and have fun with some random activities.\n")
        print ("manual/help : print the manual wherever you are in the game")
        print ("clear       : clear the terminal screen")
        print ("quit, exit  : exit the game simply type  in the terminal")
        print ("home        : to go back to the main menu")
        print ("games       : to access the games section")
        print ("advice      : to get advice about your weight")
        print("##############################################################################################################################\n")

def game_menu():
    print("\n--- Games Section ---")
    print("Available games:")
    print("1. chess - Chess bio")
    print("2. math - Simple math")
    print("3. joke - Tell a joke")
    print("4. random - Random reply")
    print("Type the game name to play, or 'back' to return.")
    
    while True:
        choice = input("Your choice: ").strip().lower()
        if choice == "chess":
            showChessBio()
        elif choice == "math":
            showMath()
        elif choice == "joke":
            giveJoke()
        elif choice == "random":
            rendomoReply()
        elif choice == "back":
            print("Returning to main game.")
            break
        else:
            print("Invalid choice. Please choose from the list or type 'back'.")

#funtion to print the BMI categories
def calc_print_BMI_categories( weight, height):
        #Body Mass Index (BMI) is a numerical value used to estimate if an individual is at a healthy
        BMI =  float(weight) / (float(height)/100)**2
        print ("Your BMI is:"+ str(BMI))

        # BMI Categories:
        if BMI < 18.5:
            print ("You are underweight.")
        elif BMI >= 18.5 and BMI < 25:
            print ("You are normal weight.")
        elif BMI >= 25 and BMI < 30:
            print ("You are overweight.")
        else:
            print ("You are obese.")



def get_input(prompt="> "):
    EXIT_COMMANDS = {"exit", "quit", "close", "stop"}

    while True:
        user_input = input(prompt).strip().lower()
        
        if user_input in EXIT_COMMANDS:
            print("Exiting game...")
            exit()
        elif user_input == "clear":
            os.system('clear')
            continue
        elif user_input == "games":
            game_menu()
            continue
        elif user_input in ["manual", "help"]:
            manual()
            continue
        else:
            # Normalize yes/no abbreviations
            if user_input in ["y", "yes"]:
                return "yes"
            elif user_input in ["n", "no"]:
                return "no"
            else:
                return user_input


#### Game Section

def gameSections():
    user_input = input(">").strip().lower()

    if user_input == "chess":
        showChessBio() 

    elif user_input == "math":
        showMath()

    elif user_input == "joke":
        giveJoke()

    elif user_input == "random":
        rendomoReply()
    else:
        letsChat()

    return user_input


def showChessBio():
    print("Here is my checss Bio on Diolingo, Bing me and lets play chess together")

def showMath():
    print("what is 2+2?")
 
def giveJoke():
    print("Why did the scarecrow win an award? Because he was outstanding in his field!")

def rendomoReply():
    print("This is a random reply. You can replace this with any fun or interesting response you'd like!")

def letsChat():
    get_user_data()





# Call the main function at the very bottom
if __name__ == "__main__":
    main()
   
# make some space in the termainal for better readability.
giveSomeSpaceInTerminal()
