import math

# Get input values and convert to numbers
x1 = int(input("Enter x1: "))
y1= int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Calculate distance using correct formula
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

# Print the results
print(f"The distance between two point is: {distance}."