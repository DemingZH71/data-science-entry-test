
def string_reverse(s):                  # Create function.

    if isinstance(s, str):              # Check if the given argument is string.
        return s[::-1]                  # If YES, reverse it by string SLICING, then return.
    else:
        return -1                       # Return -1 if s is not string.

string_reverse("Hello World")           # Invoke the function "string_reverse" using: "Hello World"
string_reverse("Python")                # Invoke the function "string_reverse" using: "Python"
