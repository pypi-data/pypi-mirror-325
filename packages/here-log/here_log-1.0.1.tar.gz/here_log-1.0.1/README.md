# Here

This package prints the current position (file name, line number) in your code.
You can use it as follows:

```python
from here import here

# Print the position
print(here)

# Print the position without print statement
here()

# Print a custom message
here("This is a custom message.")

# Print a custom message with a variable
variable = "test"
here(f"This is a custom message with a variable: {variable}")
```
