from collections import OrderedDict

ordered_dict = OrderedDict()

# Insertion order is preserved
ordered_dict["apple"] = 1
ordered_dict["banana"] = 2
ordered_dict["orange"] = 3
print("Initialized ordered_dict \n", ordered_dict.items())

#################### Move element ####################
# Move the key to the end
ordered_dict.move_to_end("apple")
print("Move apple to the end \n", ordered_dict.items())

# Move the key to the beginning
ordered_dict.move_to_end("apple", last=False)
print("Move apple to the beginning \n", ordered_dict.items())

#################### Pop element ####################
# Pop the last item
ordered_dict.popitem()
print("Pop the last item \n", ordered_dict.items())

# Pop the first item
ordered_dict.popitem(last=False)
print("Pop the first item \n", ordered_dict.items())

# Pop the item with key
ordered_dict.pop("banana")
print("Pop the item with key \n", ordered_dict.items())

# Pop the item with key and default value
ordered_dict.pop("banana", "Not Found")
print("Pop the item with key and default value \n", ordered_dict.items())

#################### Set default ####################
# Set default value
ordered_dict.setdefault("banana", "Not Found")
print("Set default value \n", ordered_dict.items())

#################### Update ####################
# Update the dictionary
ordered_dict.update({"apple": 1, "banana": 2})
print("Update the dictionary \n", ordered_dict.items())

#################### Clear ####################
# Clear the dictionary
ordered_dict.clear()
print("Clear the dictionary \n", ordered_dict.items())

#################### Copy ####################
# Copy the dictionary
ordered_dict = OrderedDict({"apple": 1, "banana": 2})
new_dict = ordered_dict.copy()
print("Copy the dictionary \n", new_dict.items())

#################### Reversed ####################
# Reverse the dictionary
reversed_dict = OrderedDict(reversed(ordered_dict.items()))
print("Reverse the dictionary \n", reversed_dict.items())
