# Is It a Palindrome?
# Problem

# Write a function that checks whether a given string is a palindrome — a word or phrase that reads the same backward as forward (ignoring capitalization, spaces, and punctuation).

# Examples

# Copy code
# is_palindrome("racecar") # Output: True
# is_palindrome("hello") # Output: False
# is_palindrome("A man a plan a canal Panama") # Output: True
 

# Your Task

#     Define a function called is_palindrome that accepts a single string.
#     Return True if the string is a palindrome, and False otherwise.
#     Normalize the string by:
#         Converting it to lowercase
#         Removing spaces (and optionally punctuation)
#     Reverse the normalized string and compare it to the original normalized version.
#         Converting it to lowercase
#         Removing spaces (and optionally punctuation)

# Concepts Tested

#     String normalization
#     Comparison logic
#     Function design and return values
#     Optional: working with Python's re (regular expression) module for bonus cleanup

# Stretch Ideas

#     Use regular expressions to remove all non-alphanumeric characters
#     Adapt the function to check if a number is a palindrome
#     Return a message instead of a Boolean (e.g., "Yes, it's a palindrome!")
#     Make the function case-insensitive without altering the original input

# This is a great real-world-style logic challenge that builds on your string handling skills — and also prepares you for upcoming projects where cleaning and normalizing data is key.
word = input("what is the word you want to check" \
": ").lower().strip()
def ispalidrome (word):
    
    if word == word[::-1]:
        print("This word is a palidrome")
    else:
        print("This word is not a palidrome")
ispalidrome(word)
 