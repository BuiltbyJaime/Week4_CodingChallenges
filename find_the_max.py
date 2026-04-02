# Problem

# Write a function that takes a list of numbers and returns the maximum value in the list — the largest number.

# Examples

# Copy code
# find_max([4, 9, 1, 17, 2])   #Output : 17  
# find_max([-5, -9, -2, -12]) #Output :  -2  
# find_max([42])  #Output : 42
 

# Your Task

#     Define a function called find_max that accepts a list of integers or floats.
#     Return the largest number in the list.
#     Do not use the built-in max() function — try to solve it manually using:
#         A for loop to check each number
#         A variable to track the current maximum
#         A for loop to check each number
#         A variable to track the current maximum

# Concepts Tested

#     Looping through a list
#     Comparison and conditional logic
#     List handling
#     Defensive programming (optional)

# Stretch Ideas

#     Add error handling for empty lists
#     Allow the function to work with mixed positive and negative values
#     Return both the max value and its index in the list
#     Rewrite it using a while loop instead of a for loop

# Hint: You’ll need a variable to hold the current highest number as you loop through the list and update it whenever you find a bigger one.

multiple_lists = ([12, 45, 78, 23, 56, 89, 34, 67, 90, 41], [3, 66, 29, 84, 51, 17, 73, 38, 95, 42], [81, 14, 57, 92, 35, 68, 21, 74, 49, 5],[], [63, 27, 88, 44, 71, 19, 96, 32, 1000, 8],[77, 11, 54, 98, 33, 69, 22, 86, 40, 15], [])



def find_the_max (multiple_lists):
        counter = 0
        for lst in multiple_lists:
            counter+=1
            if  not lst:
                print(f'{counter}th list is empty')
                continue
            max_number = lst[0]
            for number in lst:
                if number > max_number: 
                        max_number = number
            print(f"The maximum value in the list:{counter} is: {max_number} ")


find_the_max(multiple_lists)