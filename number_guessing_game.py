#Number Guessing Game using Python
import random  #Importing a module from pythons inbuilt libraries
def display_title():  #Function to display welcome message for game
    print("="*50)
    print("         NUMBER GUESSING GAME          ")
    print("="*50)
def play_game(): 
    guess=range(1,101) #Accepting numbers from 1 to 100.because 101 while be excluded in range(start,excluded)
    computer=random.choice(guess) #Computer guess the number
    attempt=0 #Intial attempt is zero.As loop run it will increase based on number of time loop run
    while True: #Until True game continues
        try:
            player=int(input("Guess a number between 1 to 100. "))  
        except Exception as e:
            print("Please enter only numbers.",e)#If user enters strings the program gets terminated by function exit()
            exit()                                # as strings not supported here for int case
        if player < 0 or player > 100:
            print("Error.Choose between 1 to 100!")
            exit()
        attempt+=1
        if player > computer:
            print('Too High')
        
        elif player < computer:
            print('Too Low')
        
        elif player == computer:
            print("Congratulations!")
            print('Correct.You guessed it.')
            break
    return computer,attempt

def calculate_status(attempt):
        if 1<=attempt<=3:
            status="Excellent Guessing."
        elif 4<=attempt<=6:
            status="Very Good." 
        elif 7<=attempt<=10:
            status="Good."
        else:
            status="Needs More practice."
        return status
def display_report(computer,attempt,status): #Displaying to print
    print("="*50)
    print("         GAME REPORT          ")
    print("="*50)
    print("Computer Guessed Number: ",computer)
    print("Total attempts         : ",status)
    print("Performance            : ",attempt)
    print("="*50)
def main():
    while True:
        display_title()
        computer,attempt=play_game()
        status=calculate_status(attempt)
        display_report(computer,status,attempt)
        choice=input("\nPlay Again? (Y/N): ").upper()
        if choice == "N":
            print("\nThank you for playing.")
            break
        elif choice != "Y":
            print("Invalid choice.Exiting....... ..")
            break
main() #Calling the functions