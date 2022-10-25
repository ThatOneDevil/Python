# Checking for the car '@'

found = False
while found == False:
    email = input("Enter your email: ")
    for i in range(len(email)- 1):
        if (email[i]) == "@":
            found = True
            print("You have a @ in your gmail :)")
