def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
num = int(input("Enter a number: "))

# Calculate factorial
fact = factorial(num)

# Print the result
print("Factorial of", num, "is", fact)

#end of the program.