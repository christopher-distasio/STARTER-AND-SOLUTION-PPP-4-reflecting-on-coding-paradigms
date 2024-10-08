# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

#VERSION 1 - Totally blank






print(flatten_and_sort(["c", ["d"], ["e", "f"], "l"]))


#VERSION 2 - Starter code in "jigsaw" style ... try to guess/replace the ???'s with the missing keyword (and use clues from errors when you run this file with python functional-practice.py (or python3 for Mac))


??? flatten_and_sort(array):
  arr = []
  ??? item in array:
    ??? i in item:
      arr.append(i)
??? sorted(arr)

print(flatten_and_sort(["c", ["d"], ["e", "f"], "l"]))


#Note: you may encounter indentation errors in error messages


'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?

Is this solution a pure function? Why or why not?

Is this solution a higher order function? Why or why not?

Would it have been easier to solve this problem using a different programming style?

Why in particular is functional programming a helpful paradigm when solving this problem?
'''
