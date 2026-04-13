# Problem

# Write a function that checks whether a number is prime. A prime number is a number greater than 1 that has no divisors other than 1 and itself.

# Examples

# Copy code
# is_prime(2)     #Output: True 
# is_prime(11)  #Output: True  
# is_prime(15)  #Output: False  
# is_prime(1)  #Output:  False  
# is_prime(0) #Output:  False  
 

# Your Task

#     Define a function called is_prime that takes one integer as input.
#     Return True if the number is prime and False otherwise.
#     Use a loop to check divisibility — don’t use any external libraries or built-in prime checkers.

# Concepts Tested

#     Conditional logic
#     Loops
#     Modulo operator (%)
#     Efficiency and edge case handling

# Stretch Ideas

#     Improve performance by only looping up to the square root of the number
#     Write a second function that returns all prime numbers up to a given number
#     Accept user input and check multiple numbers in one run
#     Save all prime results to a file

# Hints:

#     Any number less than 2 is not prime.
#     Use % to check for divisibility.
#     If any number between 2 and n-1 divides evenly into n, it’s not prime.

# Why It Matters

# Prime checks are a classic example of how math and code intersect. They’re useful in cryptography, number theory, and performance testing. And they’re a great way to practice clean looping logic and working with conditionals.
number= int(input ("what number to check?: "))
def is_prime(number):
    if number< 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

print(is_prime(number))
