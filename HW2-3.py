# 2
# The difference between a list and a tuple is that a tuple is immutable—you cannot modify it, and it does not have
# functions for modification, unlike a list. Additionally, tuples are faster than lists.
# It is best to use a list when you have variables that you may want to change. On the other hand, a tuple is best used
# when you want your code to be faster and when you do not need to modify the variables.

# 3
data_tuple = (
    {"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
)
data_tuple[0]["age"] = 31
data_tuple[0].clear()

print(data_tuple)

# This code does not cause an error because the item being modified is a dictionary inside a tuple. When one of the
# items in a tuple is a dictionary or a list, it is possible to modify the elements within them.
