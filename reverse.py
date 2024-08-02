#2. Write a Python function to reverse a string.

def reverse_string(s):
    # Reverse the string using slicing with a step of -1
    return s[::-1]

# Example
original_string = "hello"
# Call the function
reversed_string = reverse_string(original_string)

# Print the original string
print(original_string)
# Print the reversed string
print(reversed_string) 

"""Output:
hello
olleh"""
