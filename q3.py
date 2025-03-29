def update_dictionary(dct, key, value):                    # Task 1: Create function to update given dict dictionary.

    if key in dct:                                         # Check if key exists in dct.
        print("The original value was: ", dct[key])        # If YES, print original value.
        dct[key] = value                                   # update new key-value pair.
    else:
        dct[key] = value                                   # If key not found in dct, add the pair to dct.

    return dct                                             # Return dct

update_dictionary({}, "name", "Alice")      # Task 2: invoke function.

update_dictionary({"age": 25}, "age", 26)   # Task 2: invoke function.
