
def string_reverse(s):                  # Create function.

    if isinstance(s, str):              # Check if the given argument is string.
        return s[::-1]                  # If YES, reverse it by string SLICING, then return.

string_reverse("Hello World")           # Invoke the function "string_reverse" using: "Hello World"
string_reverse("Python")                # Invoke the function "string_reverse" using: "Python"
