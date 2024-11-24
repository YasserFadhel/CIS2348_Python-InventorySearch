# Inventory Checker

**Author**: Yasser Fadhel  
**Program Purpose**: A Python script to manage and query an inventory system with intelligent search and recommendation capabilities. This program is designed to provide user-friendly functionality while handling potential input errors gracefully.

---

## **Features**
- Search for an item based on **manufacturer** and **type**.
- Provides recommendations for items of similar value when available.
- Ignores irrelevant input text for seamless user interaction.
- Hides damaged or expired items from search results automatically.

---

## **How It Works**
1. **Inventory Item Class**:
   - Represents an inventory item with details such as:
     - Item ID
     - Manufacturer
     - Item type
     - Price
     - Service date
     - Damage status

2. **Inventory Class**:
   - Manages a collection of inventory items.
   - Core functionalities include:
     - Adding items
     - Searching for items
     - Finding the closest-priced items
     - Parsing user input for effective query handling

3. **User Interaction**:
   - Enter the manufacturer and item type in any order (e.g., `"Nice Dell Laptop"`).
   - Irrelevant words (e.g., `"nice"`) are ignored automatically.
   - To **exit the program**, type `q`.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. Run the Python script:
   ```bash
   python FinalInventoryQuery.py



## **Usage**
1. Run the script and follow the prompts:

    - Example Inputs:
        Input: "Nice Dell Laptop"
        Output: Item found and an alternative suggestion.

        Input: "Samsung Tablet"
        Output: "No such item in inventory!" (if the item is damaged).

         Input: "q"
        Output: Exits the program with a thank-you message.

3. Test Cases:

    - Format Handling:
        Input: "Dell Banana Laptop"
        Observe how the system ignores unrelated words like "Banana".
    - Recommendations:
        Input: "Dell Laptop"
      
    See suggestions for alternative items.



## **Dependencies**

   Python Version: Requires Python 3.6+.
   
   Modules: Uses the built-in datetime module for handling dates.


## **Development Notes**
### **1. Date Formatting**:
- The program uses **`datetime.strptime()`** for parsing service dates.
- **Example**:  
  `"2024-12-31"` is converted into a `datetime` object for comparison.

### **2. Input Parsing**:
- The **`parseInput()`** function intelligently ignores irrelevant words.
- **Example**:  
  - **User Input**: `"Nice Apple Computer"`  
  - **Parsed Result**: `("Apple", "Computer")`

### **GPT-Generated Enhancements**:
- **Date Handling**: Provided optimized code snippets for working with **`datetime`**.
- **Input Parsing**: Improved logic to dynamically filter out unrelated words.

---


## **Future Improvements**
- **Persistent Storage**: Integrate a database backend for storing inventory data.
- **GUI Development**: Create a graphical user interface for improved usability.
- **Advanced Search Filters**: Add support for filtering by price ranges or categories.
- **Enhanced Recommendations**: Personalize recommendations based on user preferences.

---


## **Acknowledgments**
This project was developed with assistance from **OpenAI's ChatGPT**, which provided guidance on specific functionalities and code optimization. We were encouraged to use ChatGPT in some part of our code development.

---
