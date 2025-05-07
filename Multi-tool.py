import time

username_default = "admin"
password_default = "supersecretpassword"
application1 = "calculator"
application2 = "sleep calculator"
application3 = "guessing game"

def timeout():
  print("You have been timed out for 20 seconds for putting the wrong username/password 3 times.")
  time.sleep(20)
  login()

def login():
  login_attempts = 0

  while True:
    if login_attempts >= 3:
      timeout()
    
    username_entry = input('What is the username? ')  
    password_entry = input('What is the password? ')
  
    if username_entry != username_default:
      print("Incorrect Username or Password")
      login_attempts = login_attempts + 1

  
    if password_entry != password_default:
      print("Incorrect Username or Password")
      login_attempts = login_attempts + 1

    else:
      print(f"\nWelcome! {username_entry}\n")
      break

def calculator():
  print("Welcome to the calculator\n""Please enter your two numbers - one at a time")
  number = int(input())
  number1 = int(input())
  print("please enter what you would like to do with these numbers")
  function = input()
  if function == "add":
    answer = number + number1
    print(answer)
  if function == "subtract":
    answer = number - number1
    print(answer)
  if function == "divide":
    answer = number / number1
    print(answer)
  if function == "mutliple":
    answer = number * number1
    print(answer)
  print ("Would u like to try a appliation")
  input("Yes or No")
  if input == "yes":
    Select_application()
  else:
    input("\nPress ENTER to exit program")

def sleep():
  print("Welcome to the Sleep Calculator")
  hourspernight = input("How many hours per night do you sleep? ")
  hoursperweek = int(hourspernight) * 7
  print ("You sleep",hoursperweek,"hours per week")
  hourspermonth = float(hoursperweek) * 4.35
  print ("You sleep",hourspermonth,"hours per month")
  dayspermonth = float(hourspermonth) / 24
  print ("This equates to",dayspermonth,"days per month")
  hoursperyear = float(hourspermonth) * 52
  print ("You sleep",hoursperyear,"hours per year")
  print ("Would u like to try a appliation")
  input("Yes or No")
  if input == "yes":
    Select_application()
  else:
    input ("\nPress ENTER to exit program")

def guessing_game():
  import random
  rnumber = random.randint(1,100)
  unumber = int(input("Enter a number "))
  attempts = 0
  while unumber != rnumber:
    if unumber < rnumber:
      print("You have guessed to low")
      unumber = int(input("try again "))
      attempts = attempts + 1
    elif unumber >rnumber:
      print("You have guessed to high")
      unumber = int(input("try again "))
      attempts = attempts + 1
  print("You Win! You had",attempts,"at guessing.")
  print ("Would u like to try a appliation")
  input("Yes or No")
  if input != "yes":
    Select_application()
  else:
    input ("\nPress ENTER to exit program")

# The select appication not working 
def Select_application():
  print("What appliaction would u like\n""Calculator\n""Sleep Calculator\n""Guessing Game\n")

  choice = input("Please enter the application: \n").lower()
  if choice == application1:
    calculator()

  if choice == application2:
    sleep()

  if choice == application3:
    guessing_game()

  else:
    print("\nPlease enter a valid application\n")
    Select_application()

# This will be the only thing that runs when the code first starts
login()
Select_application()