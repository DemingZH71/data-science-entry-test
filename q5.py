def check_divisibility(num, divisor):                                           # Task 1: Create function.
    if isinstance(num, (int, float)) and isinstance(divisor, (int, float)):     # Check if num and divisor is numeric.

        if num % divisor == 0:                                                  # check if num is divisible by divisor
            return True                                                         # Return TRUE if YES.
        else:
            return False                                                        # Return FALSE if NOT.

print(check_divisibility(10, 2))                                    # Task 2: Invoke using: 10, 2.

print(check_divisibility(7, 3))                                     # Task 2: Invoke using: 7, 3.

