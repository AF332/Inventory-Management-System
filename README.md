# Inventory-Management-System

## Overview

- The Inventory Management System is a Python-based command-line application designed to help manage and track stock items efficiently in a retail environment. The application provides a range of functionalities, from adding new items to searching, updating, purchasing, returning, and deleting existing inventory items.

## Features

Item Creation

- create_item Function: Constructs a new item dictionary from the provided name, quantity, and price. Each item's details are encapsulated in this dictionary, ready to be added to the main inventory list.

Item Addition

- add_item Function: Adds the newly created item dictionary to the central inventory dictionary, with the item's name as the key and its details (quantity and price) as the value. This method ensures that each item is uniquely identifiable by its name.

Item Search

- find_item Function: Searches the inventory dictionary for an item matching the given name. If found, it returns a dictionary containing the item's details; otherwise, it returns None.

Item Update

- update_item Function: Modifies an existing item's details based on the provided name. If the item is found, it allows updating the item's quantity and/or price. If the item does not exist, it reports that the item was not found.

Item Deletion

- delete_item Function: Removes an item from the inventory dictionary based on the provided name. If the item is found and successfully deleted, it confirms the deletion; if not, it reports that the item was not found.

Total Stock Calculation

- total_stock Function: Calculates the total quantity of all items currently in the inventory by summing up their respective quantities.

Item Purchase

- purchase_item Function: Checks if the specified item is available in sufficient quantity. If so, it deducts the purchased quantity from the inventory and updates the till balance accordingly. If not, it reports that the item is unavailable or insufficient in quantity.

Item Return

- return_item Function: Checks if the specified item is in the inventory. If so, it adds the returned quantity back to the inventory and adjusts the till balance accordingly. If the item does not exist, it reports that the item was not found.

User Interface Management

- main_interface Function: Provides a text-based menu system that prompts the user to choose from adding, searching, updating, deleting, purchasing, returning, displaying items, or exiting the application.

System Architecture

- The system is structured around a central dictionary (inventory) where all item information is stored. Each function interacts with this dictionary, performing specific operations as required. A till_balance variable tracks the financial transactions. This modular approach keeps the code clean, manageable, and scalable, facilitating efficient inventory management.

![image](https://github.com/user-attachments/assets/38140853-7468-4a4a-9453-659538fc48b1)
