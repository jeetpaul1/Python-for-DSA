#Write a program to remove a key-value pair from a dictionary.


person = {"name": "Alice", "age": 30, "city": "London"} #solution

# Remove a key-value pair
removed_value = person.pop("city")

# Print updated dictionary and removed value
print("Updated Dictionary:", person)
print("Removed Value:", removed_value)
