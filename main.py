print("Welcome to Rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120: #1
    print("You can ride the rollercoaster!")
    
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <=55:
        print("Everything is gonna be ok. Have a ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wants_photo = input("Do you want a photo taken? Y or N. \n")
    if wants_photo == "Y":
        bill += 3     
        
    print(f"Your finnal bill is ${bill}")  

else: #2
    print("Sorry, you have to be taller before you can ride.")