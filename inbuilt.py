# ------ Python Lists

nums = [1,2,3,4,5]  # Integer list
fruits = ["apple", "banana", "grapes"]  # String list

print(len(nums))        # To find the number of items in the list

nums.append(6)          # Add an item at the end of the list

nums.extend(fruits)     # Add a list to the existing list

nums.insert(1, 10)      # Insert an item at a given position

nums.remove(1)          # Remove the item from list

nums.pop()              # Remove an item at index position 3

nums.sort()             # Sort the itemsof the list in place

nums.reverse()          # Reverse the elements in the list


# ------ Dictionaries

thisdict = {
    'key1':'val1',
    'key2':'val2',
    'key3':'val3'
}                               # Declaring a dictionary

thisdict1 = {}                  # Declaring an empty dictionary

print(thisdict['key1'])         # Accessing the elements in dictionary

thisdict['key4'] = 'val4'       # Adding entry to the existing dictionary

del thisdict['key4']            # Delete an entry from dictionary

'key1' in thisdict              # Returns True if the key exists in the dictionary

thisdict1.clear()               # Clears all the key value from dictionary

thisdict.keys()                 # Returns all keys in dict

thisdict.values()               # Returns all values in dict

for k, v in thisdict.items():    # Loop through both keys and values
    print(k, v)
    
    
# ------ Sets

thisset = {"apple", "banana", "grapes"}

emptyset = set()            # Declare an empty set

print(len(thisset))         # Get length of the set

emptyset.add('a')           # Add item to a set

emptyset.update(thisset)    # Add items from another set into the current set

emptyset.remove("banana")   # To remove an item in a set

del thisset                 # To delete the set



# ------ Tuples

thistuple = ("apple", "banana", "grapes", "oranges")

emptytuple = ()          # Declare an empty tuple

t = tuple(fruits)        # Creating a tuple from a list

del thistuple            # To delete tuple


