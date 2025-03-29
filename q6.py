def find_first_negative(lst):       # Task 1: Create function.
    i = 0
    while i < len(lst):             # Use WHILE loop to find in the given list.

        if lst[i] < 0:              # Check if value is negative.
           return lst[i]            # Return the negative value.
        else:
           i += 1
           continue

    return "No negatives"           # Return "No negatives" if no negative value found.

tst1 = [3, 5, -1, 7, -2, 8]
print(find_first_negative(tst1))    # Task 2: Invoke the function.
tst2 = [2, 10, 7, 0]
print(find_first_negative(tst2))    # Task 2: Invoke the function.
