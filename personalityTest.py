#task one day 2

# personality test
books = int(input("Enter the number of books purchased:"))

if books == 0:
    print("You earned 0 points")
elif books == 1:
    print("You earned 6 points")
elif books == 2:
    print("You earned 16 points")
elif books == 3:
    print("You earned 32 points")
elif books >= 4:
    print("You earned 60 points")
else:
    print("Invalid number of books!")






