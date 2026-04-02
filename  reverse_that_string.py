# Challenge: Reverse That String!
# Problem

# Write a function that takes a single string as input and returns that string in reverse order.

# Example

# Copy code
# reverse_string("hello") # will output: olleh
# reverse_string("Python") # will output: nohtyP
 

# Your Task

#     Define a function called reverse_string that accepts one argument (a string).
#     Return the reversed version of the string.
#     Try using string slicing as a first approach.
#     Bonus: After you get it working, try writing a second version using a for loop to build the reversed string manually.

# Concepts Tested

#     String manipulation
#     Indexing and slicing
#     Looping through strings (if attempting the bonus)
#     Function definition and return values

# Stretch Ideas

#     Add a feature that ignores whitespace or punctuation
#     Make the function work for lists as well as strings
#     Compare the performance of slicing vs loop methods for long strings

# This one may seem simple, but thinking about different ways to solve it builds fluency — and will help with trickier string problems later.



word = input("what is the word you want to reverse?: ").lower().strip()
def reverse_string(word:str):
        print (f'This is the first word reversed is {word[::-1]}')
reverse_string(word)

word2 = input("what is the second word you want to reverse?: ").lower().strip()
def reverse_string2(word2):
        reverse = ''
        for letter in range(len(word2), 0, -1):
                reverse += word2[letter-1]
        return reverse
result = reverse_string2(word2)
print("This is the second word reversed: ", result)
