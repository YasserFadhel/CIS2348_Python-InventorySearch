"""
Program: Inventory Checker
Author: Yasser Fadhel

This program is primarily built to find an item within a set/list. It asks the user for an input and then searches for items that match the input. It performs some extra steps to ensure that the system ignores any mistakes done during user input. The system will also recommend other items of similar value to the one being searched for.

Process/Algorithm:
1- Define a class that handles all the item details (ItemID, manufacturer, type, price, service date, damage status) and a string function that sets the formatting for the output later on.
2- Define a class that handles the inventory operations like adding, finding and updating the inventory items that are saved in a list.
3- Define a Main function that will execute on execution and populate the inventory list. It will ask the user for an input and perform the operations defined in the classes we built.



To test the program we recommend the following:

1- To test the input formatting feature, simply input:
    "nice Dell Laptop" or "Dell Banana Laptop"

2- To test the hidden damaged items feature, simply input:
    "Samsung Tablet"

3- To test the alternative recommendation feature, simply input:
    "Dell Laptop"

"""

import datetime                                                                                     # Importing the datetime module (used to check for service date)

class InventoryItem:                                                                                # Defining a class for inventory items
    def __init__(self, itemId, manufacturer, itemType, price, serviceDate, isDamaged):              # Initializing the class with attributes
        self.itemId = itemId                                                                        # Assigning the item ID
        self.manufacturer = manufacturer.lower()                                                    # assigning the manufacturer name and Converting it to lowercase so the user doesn't have to worry about case sensitivity when searching for their item.
        self.itemType = itemType.lower()                                                            # Converting the item type to lowercase and assigning it
        self.price = price                                                                          # Assigning the price
        self.serviceDate = datetime.datetime.strptime(serviceDate, '%Y-%m-%d')                      # Parsing the service date string into a datetime object, ChatGPT was used to improve the date.time function (check the notes at the bottom for more details)
        self.isDamaged = isDamaged                                                                  # Assigning whether the item is damaged or not

    def __str__(self):                                                                                                                                        # Defining a string for the class
        return f"\n Item ID: {self.itemId}, Manufacturer: {self.manufacturer.capitalize()}, Item: {self.itemType.capitalize()}, Price: ${self.price:.2f} \n"  # Returning a formatted string representation of the item and its attributes

class Inventory:                                                # We define a class for the inventory
    def __init__(self):                                         # We initialize the class
        self.items = []                                         # we create an empty list to store inventory items
        self.knownManufacturers = set()                         # we create an empty set to store known manufacturers (This is used later when we parse the user input to remove any unrealted words)
        self.knownItemTypes = set()                             # we create an empty set to store known item types  (This is used later when we parse the user input to remove any unrealted words)

    def addItem(self, item):                                    # we add a function that can add an item to the inventory
        self.items.append(item)                                 # we append the item to the inventory list
        self.updateKnownSets(item)                              # This will also update the known manufacturers and item types sets by calling the function that handles that (to make sure our parsing function works with added items as well)

    def updateKnownSets(self, item):                            # Initialize a function to update known manufacturers and item types
        self.knownManufacturers.add(item.manufacturer)          # We add the manufacturer of the item to the known manufacturers set
        self.knownItemTypes.add(item.itemType)                  # We add the item type of the item to the known item types set

    def findItem(self, manufacturer, itemType):                 # We define a function to find an item in the inventory
        currentDate = datetime.datetime.now()                   # Getting the current date and time from the datetime module.

        # Filtering items based on manufacturer, item type, service date, and damage status
        # we use a for loop to search for the item attributes,  it sets a set of conditions that have to be met using "and" arguments
        validItems = [item for item in self.items if item.manufacturer == manufacturer and     # we first check if the manufacturer being input by the user matches the ones in the list
                       item.itemType == itemType and                                           # we then check for a matching item type
                       item.serviceDate > currentDate and not item.isDamaged]                  # we finally check if the service date is bigger than the current date (found using datetime module). We also add a "and not" to find items that are not damaged.
        if not validItems:                                                                     # If no valid items are found, we return nothing
            return None  
        return max(validItems, key=lambda item: item.price)                                    # If an calid item is found, we return the item with the maximum price among the valid items

    def findClosestPricedItem(self, itemType, referencePrice):                                 # We define a function to find the closest priced item using variables for item type and
        currentDate = datetime.datetime.now()                                                  # Getting the current date and time

        # Filtering items based on item type, service date, damage status, and price difference with the reference price
        # we use a for loop to search for the item attributes,  it sets a set of conditions that have to be met using "and" arguments
        similarItems = [item for item in self.items if item.itemType == itemType and             # we first check for a matching item type
                         item.serviceDate > currentDate and not item.isDamaged and               # we then check if the service date is bigger than the current date (found using datetime module). We also add a "and not" to find items that are not damaged.
                         item.price != referencePrice]
        if not similarItems:                                                                     # If no similar items are found, we return nothing
            return None 
        return min(similarItems, key=lambda item: abs(item.price - referencePrice))              # if we find a similar item, we return the item with the minimum price difference from the reference price

    def parseInput(self, userInput):                                                             # We define a function to parse user input and look for the manufacturer and item type within the input and disregard any other words. ChatGPT was used to improve this function (check the notes at the bottom for more details)
        words = userInput.lower().split()                                                        # we split the user input when there is a space, we make sure the words are turned into lowercase words.
        
        manufacturer = next((word for word in words if word in self.knownManufacturers), None)   # we find the first word in the user input that matches a known manufacturer, or None if no match is found
        itemType = next((word for word in words if word in self.knownItemTypes), None)           # we find the first word in the user input that matches a known item type, or None if no match is found
        return manufacturer, itemType                                                            # we return manufacturer and item type

def main():                                                                                      # we define a Main function, this is where the user interaction will occur.
    inventory = Inventory()                                                                      # we create an instance of the Inventory class

    # Adding inventory items (we can add more, but I added enough to just test the different functionalities required for this project)
    inventory.addItem(InventoryItem('001', 'Apple', 'MacBook', 1500, '2024-12-31', False))
    inventory.addItem(InventoryItem('002', 'Dell', 'Laptop', 1400, '2024-12-31', False))
    inventory.addItem(InventoryItem('003', 'Dell', 'Laptop', 2100, '2024-12-31', False))
    inventory.addItem(InventoryItem('004', 'Apple', 'iMac', 1800, '2025-01-01', False))
    inventory.addItem(InventoryItem('005', 'Samsung', 'Tablet', 300, '2024-05-20', True))
    inventory.addItem(InventoryItem('006', 'Samsung', 'Chromebook', 350, '2025-06-15', False))

    while True:                                                                                  # We create an infinite loop with "while true" to keep asking the user with the same prompt
        userInput = input("Enter the manufacturer and item type or 'q' to quit: ")               # the prompt is to ask the user for his input
        if userInput.lower() == 'q':                                                             # if the user input (changed to lowercase) is the letter q (for quit)
            print("\nThank you for shopping with us!\n")                                         # 1- Print a thank you message
            break                                                                                # 2- Break out of the loop
        
        manufacturer, itemType = inventory.parseInput(userInput)                                 # We then parse the user input using the function we deinfed in the inventory class
        if not manufacturer or not itemType:                                                     # If manufacturer or item type is not found
            print("Invalid input, please try again.")                                            # 1- Print an error message
            continue                                                                             # 2- Continue to the next iteration of the loop

        item = inventory.findItem(manufacturer, itemType)                                        # we then attempt to find an item from the user input using the function we defined in the inventory class
        if item:                                                                                 # If the item is found
            print("\n Your item is:", item)                                                      # 1- Print the item (it calls the __str__ function from the InventoryItem class for the formatted string)
            otherItem = inventory.findClosestPricedItem(itemType, item.price)                    # 2- call the "find closest price function" from the inventory class.
            if otherItem:                                                                              # If another item is found
                print("You may, also, consider:", otherItem)                                           # 1- Print the other item (again, it calls the __str__ function from the InventoryItem class for the formatted string)
        else:                                                                                    # If the item is not found (returns to th find item function)
            print("No such item in inventory!")                                                  # Print a message indicating that the item is not found

if __name__ == "__main__":
    main() 






"""
The use of ChatGPT in this program:




1- The date time formatting within the __init__ function in InventoryItem class

my prompt: I have a variable with a date as a string. how can i use the date time module to convert it to a date format?

ChatGPT reply:

You can use the datetime module in Python to convert a string representing a date into a datetime object. Here's how you can do it:

from datetime import datetime

# Assuming your string date is in the format 'YYYY-MM-DD'
date_string = '2024-04-26'

# Convert the string to a datetime object
date_object = datetime.strptime(date_string, '%Y-%m-%d')

print(date_object)

I used the datetime.strptime function in my code with some modifications (mainly because I called the module itself at the top of the script without specifying the function of "datetime" so I had to add it to my line code every time i needed to call it)




2- The parse function within Inventory Class

My Attempt:
Basic assumption: manufacturer and item type are likely the first two words

def parse_input(user_input):
    words = user_input.lower().split()
    if len(words) < 2:
        return None, None
    return words[0], ' '.join(words[1:])

This didn't work as intended. I had to ask GPT for a better way to parse the user input to ignore any unrelated words no matter where they appear in the sentence.

My prompt: I am writing a program that asks the user for his input and then matches the input to items in a set.
I want to allow the user to input anything but the system shouldn't account for meaningless words. 
I have established two sets that contain the words it needs to look for.
if the customer inputs "nice apple computer", the system should ignore the word "nice" and only look for apple and computer in the sets, no matter where nice appears within that sentence.

I tried to parse the sentence but my attempt failed, what would be a good parse technique to achieve what I desire the system to achieve?


ChatGPT replt: 
It sounds like you're trying to implement a system that filters out certain words from user input before matching them against predefined sets. One approach you could take is to use tokenization and then filter out the irrelevant words. Here's a step-by-step guide on how you could achieve this:

Tokenization: Split the user input into individual words.
Filtering: Remove any words that you consider meaningless or irrelevant. For example, if you have a list of stopwords (commonly used words that typically do not carry much meaning, like "nice" in your example), you can filter them out.
Matching: Compare the remaining words against your predefined sets to find matches.

        # Define your predefined sets
        set1 = {"apple", "banana", "orange"}
        set2 = {"computer", "keyboard", "mouse"}

        # Function to filter out meaningless words
        def filter_words(words, stopwords):
            return [word for word in words if word.lower() not in stopwords]

        # User input
        user_input = input("Enter your input: ")

        # Tokenization
        words = user_input.split()

        # Define your list of stopwords
        stopwords = {"nice", "good", "great", "excellent"}  # Add more as needed

        # Filter out meaningless words
        filtered_words = filter_words(words, stopwords)

        # Match against predefined sets
        matches_set1 = set(filtered_words) & set1
        matches_set2 = set(filtered_words) & set2

        print("Matches in set 1:", matches_set1)
        print("Matches in set 2:", matches_set2)


My 2nd prompt: What if I were to condense it into a function?


ChatGPT reply:

Certainly! You can encapsulate the functionality into a function for reusability. Here's how you can do it:

        def filter_and_match(user_input, predefined_sets, stopwords):
            # Tokenization
            words = user_input.split()
            
            # Filter out meaningless words
            filtered_words = [word for word in words if word.lower() not in stopwords]
            
            # Match against predefined sets
            matches = {}
            for name, predefined_set in predefined_sets.items():
                matches[name] = set(filtered_words) & predefined_set
            
            return matches

            
I then used this as a blueprint to create my function (used in the code above) with some modifications.
"""
