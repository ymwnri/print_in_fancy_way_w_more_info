# Ask for name, last name and dream job
# Display the user info in a fancy way
# Print a progress bar while the program is loading

# Import Modules
from itertools import cycle
from time import sleep

# Ask for user input
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
dream_job = input("Enter your Dream Job: ") 

# Ask for more information
favorite_hobby = input("Enter your Favorite Hobby: ") 
favorite_color = input("Enter your Favorite Color: ")
school = input("Enter your School: ")

# Print fx
print("\nInitializing . . . . .")

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)
    
# Print user info
print(f"\n\nHello, I am {first_name} {last_name}! My dream job is to become a {dream_job}. \nMy favorite hobby is {favorite_hobby} and my favorite color is {favorite_color}. \nI am studying at {school}.")