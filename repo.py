#program to take input from user and return if the number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num,"is even")
else:
    print(num,"is odd")

#the same problem using p for loop
# Ask the user how many numbers they want to check
count = int(input("How many numbers do you want to check? "))

# Use a for loop to iterate for the given count
for i in range(count):
    # Take a number from the user
    num = int(input(f"Enter number {i + 1}: "))
    
    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

done-with both loops
