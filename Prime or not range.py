# Get the start and end values from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Ensure the range is valid
if start > end:
    print("Invalid range! Starting number must be less than or equal to the ending number.")
else:
    print(f"\nEven and Odd numbers from {start} to {end}:\n")
    for i in range(start, end + 1):  # Loop through the range
        if i % 2 == 0:  # Check if the number is even
            print(f"{i} is Even")
        else:  # If not even, then it's odd
            print(f"{i} is Odd")
