# Implement a function that will flatten and sort a List of integers in ascending order, and which adheres to a functional programming paradigm.

na = [['Moe', 'Jill'], ["Lacy", "Scooter"]]


def flatten_and_sort(data_list): # O(1)
    flattened_list = [] # O(1) 
    for sublist in data_list: # O(1) process of flattening is O(n)
        for item in sublist: # O(1)
            flattened_list.append(item) # process of appending to list is O(n)
    return sorted(flattened_list) # O(1) # process of sorting the list with 
#the built-in sorted method is O(n log n)

print(flatten_and_sort(na))

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?

Is this solution a pure function? Why or why not?

Is this solution a higher order function? Why or why not?

Would it have been easier to solve this problem using a different programming style?

Why in particular is functional programming a helpful paradigm when solving this problem?
'''

# The four characteristics of first-class functions are:

# Can Be Assigned to Variables: Functions can be assigned to variables and used like any other value.
# Can Be Passed as Arguments to Other Functions: Functions can be passed as parameters to other functions.
# Can Be Returned from Other Functions: Functions can be returned as the result of other functions.
# Can Be Stored in Data Structures: Functions can be stored in collections such as lists and dictionaries.


# Higher-Order Functions
# Definition:
# Higher-order functions are functions that can take other functions as arguments or return functions as their result.

# Key Differences:
# Scope:

# First-Class Functions: Refer to the general ability to treat functions as first-class citizens, meaning they can be assigned to variables, passed as arguments, returned from functions, and stored in data structures.
# Higher-Order Functions: Specifically refer to functions that operate on other functions, either by taking them as arguments or by returning them.
# Focus:

# First-Class Functions: Focus on the capabilities and flexibility of functions in the language.
# Higher-Order Functions: Focus on the specific behavior and use cases where functions are passed to or returned from other functions.
# Usage:

# First-Class Functions: Enable the existence of higher-order functions but also support other functional programming features like closures and function expressions.
# Higher-Order Functions: Utilize the first-class nature of functions to enable powerful abstractions and patterns like function composition, decorators, and more.




# Bonus 1: Make a version that doesn't use loops but uses built-in functions instead.


# Bonus 2: Make a version that doesn't use loops but uses an imported module instead.


# Bonus 3: Make a version that uses recursion. 