import time

username_default = "admin"
password_default = "supersecretpassword"

def timeout():
  print("You have been timed out for 20 seconds for putting the wrong username/password 3 times.")
  time.sleep(20)
  login()

def example_function(username):
  print(f"hi {username}")

def login():
  login_attempts = 0

  while True:
    if login_attempts >= 3:
      timeout()
    
    username_entry = input('What is the username?')  
    password_entry = input('What is the password?')
  
    if username_entry != username_default:
      print("Incorrect Username or Password")
      login_attempts = login_attempts + 1

  
    if password_entry != password_default:
      print("Incorrect Username or Password")
      login_attempts = login_attempts + 1

    else:
      print("Welcome!")
      example_function(username_entry)
      break
def Select_applation():
  print("What appliaction would u like\n""Calculator")

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
    input("\nPress ENTER to exit program")
# This will be the only thing that runs when the code first starts
login()
calculator()
