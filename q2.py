
def find_and_replace(lst, find_val, replace_val):                                             # Task 1: Create function.

    for x in lst:                                                                             # Use for loop to Search in list.
        if x == find_val :                                                                    # Check find_val value in list.
            index = lst.index(x)                                                              # Get value index.
            lst[index] = replace_val                                                          # Update with replace_val value.

    return lst

find_and_replace([1, 2, 3, 4, 2, 2, 5], 2, 5)                           # Task 2: invoke function.

find_and_replace(["apple", "banana", "apple"], "apple", "orange")       # Task 2: invoke function.
