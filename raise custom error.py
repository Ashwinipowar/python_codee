# 🔹 What is a custom error?
# In Python, you can create your own error types to make 
# your code clearer and more specific when something goes wrong


class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    print(f"Age set to {age}")

# Try it
set_age(-5)


# 🧠 Why use custom errors?
# To make your code easier to debug

# To handle specific problems in a meaningful way

# To give clear error messages to users or developers