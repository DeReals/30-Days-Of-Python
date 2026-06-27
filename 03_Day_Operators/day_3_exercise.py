""""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

# replicate this

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

# type check
print(type("10") == type(10))  # should be false

# decimal check
#print(int('9.8') == 10)  # error: cannot down play from float to int

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hr = int(input("Enter hours: "))
rate = int(input("Rate per hour: "))

print(f"Gross Income: {hr*rate}")