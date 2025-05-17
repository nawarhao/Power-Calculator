# Ask the user for a number

base = int(input("Enter the number you want to find powers of: "))
 # Ask how many powers they want to calculate
limit = int(input("How many powers do you want to calculate? "))

 # Use a for loop to calculate and print powers from 1 to limit
print(f"\nPowers of {base} from 1 to {limit}:\n")
for i in range(1, limit + 1):
        result = base ** i
print(f"{base}^{i} = {result}")

