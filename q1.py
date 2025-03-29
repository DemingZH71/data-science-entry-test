
def swap(x, y):                                                     # Task 1: Create a function to swap x and Y.

    if isinstance(x, (int, float)) and isinstance(y, (int, float)): # Check the type of x and Y .
        x, y = y, x                                                 # Swap x and Y if both are int or float type.
        print(x, y)                                                 # Print swapped value.
        return x, y                                                 # Return swapped numeric x and Y.

    else:
        return -1                                                   # Return -1 if x and y are not numeric.

swap("Apple",10)                                              # Task 2: Call and invoke the function. with "Apple", 10.
swap(9,17)                                                    # Tsk 2: Call and invoke the function. with 9, 17.
