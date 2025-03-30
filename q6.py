def find_first_negative(lst):       # Task 1: Create function.
    i = 0
    while i < len(lst):             # Use WHILE loop to find in the given list.

        if lst[i] < 0:              # Check if value is negative.
           return lst[i]            # Return the negative value.
        i += 1

    return "No negatives"           # Return "No negatives" if no negative value found.

find_first_negative([3, 5, -1, 7, -2, 8])    # Task 2: Invoke the function.

find_first_negative([2, 10, 7, 0])    # Task 2: Invoke the function.
