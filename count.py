#3. Write a Python function to count the occurrences of a specific element in a list.


def count_occurrences(lst, element):
    # Count the number of times 'element' appears in 'lst'
    return lst.count(element)

# Example
my_list = [1, 2, 3, 2, 4, 2, 5]
# Element to count occurrences of
element_to_count = 2

# Call the function to count occurrences of 'element_to_count' in 'my_list'
count = count_occurrences(my_list, element_to_count)

# Print the number of occurrences
print(count)

# Output: 3
