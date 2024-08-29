"""Creating a dictionary to contain the name, quantity, and price of a new item."""
def create_item(name, quantity, price):
    return {
        'name': name,
        'quantity': quantity,
        'price': price
        }

"""Creating an inventory list dictionary called 'inventory'. The name of the new item created is used as the key in the inventory list 'inventory' and the quantity and price of the new item is stored as the values of the dictionary."""
def add_item(inventory, item):
    inventory[item['name']] = {
        'quantity': item['quantity'],
        'price': item['price']
        }

"""Function finds an item by using the key of the dictionary 'name' with the .get() method. If the name passed in does not match with an entry then the value None is given."""
def find_item(inventory, name):
    return inventory.get(name, None)

"""Function to modify an existing item details on the inventory dictionary based on the item name passed in."""
def update_item(inventory, name, quantity=None, price=None):
    if name in inventory:
        if quantity is not None:
            inventory[name]['quantity'] = quantity
        if price is not None:
            inventory[name]['price'] = price
        return f"Item '{name}' updated successfully."
    else:
        return "Item not found!"

"""Function to delete item off system based on the item name input."""
def delete_item(inventory, name):
    if name in inventory:
        del inventory[name]
        return f"Item '{name}' deleted successfully."
    else:
        return "Item not found!"

"""Function iterates through the inventory dictionary and takes all the quantity values and sums it."""
def total_stock(inventory):
    return sum(item['quantity'] for item in inventory.values())

"""Function checks is the item name inputted is in the dictionary and if its quantity is more than or equal to the quantity inputted. If it is the quantity inputted in is substracted for the quantity in the dictionary. The price is then calculated and added to the till balance."""
def purchase_item(inventory, till_balance, name, quantity):
    if name in inventory and inventory[name]['quantity'] >= quantity:
        inventory[name]['quantity'] -= quantity
        total_price = quantity * inventory[name]['price']
        till_balance += total_price
        return f"Purchased {quantity} of '{name}'. Total price: £{total_price}.", till_balance
    else:
        return "Item not available or insufficient quantity!", till_balance

"""Function checks if the name inputted is in the inventory. If it is then the quantity inputted is added on the value of the dictionary's quantity. The price of the refund is calculated and substracted from the till balance."""
def return_item(inventory, till_balance, name, quantity):
    if name in inventory:
        inventory[name]['quantity'] += quantity
        total_price = quantity * inventory[name]['price']
        till_balance -= total_price
        return f"Returned {quantity} of '{name}'. Amount deducted: £{total_price}.", till_balance
    else:
        return "Item not found!", till_balance

"""Function to create the user interface to test out all the difference use cases."""
def main_interface():
    inventory = {}
    till_balance = 0.0

    while True:
        print("\nWelcome to the Inventory Management System")
        print("1. Add a New Item")
        print("2. Find an Item")
        print("3. Update an Existing Item")
        print("4. Delete an Item")
        print("5. Display All Items")
        print("6. Return Total Stock Value")
        print("7. Purchase an Item")
        print("8. Return an Item")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter the item's name: ")
            quantity = int(input("Enter the quantity of the item: "))
            price = float(input("Enter the price of the item: "))
            item = create_item(name, quantity, price)
            add_item(inventory, item)
            print("Item added successfully.")

        elif choice == '2':
            name = input("Enter the name of the item to find: ")
            item = find_item(inventory, name)
            if item:
                print(f"Found: {name}, Quantity: {item['quantity']}, Price: £{item['price']}")
            else:
                print("Item not found.")

        elif choice == '3':
            name = input("Enter the name of the item to update: ")
            quantity = input("Enter the new quantity (press enter to skip): ")
            price = input("Enter the new price (press enter to skip): ")
            quantity = int(quantity) if quantity else None
            price = float(price) if price else None
            print(update_item(inventory, name, quantity, price))

        elif choice == '4':
            name = input("Enter the name of the item to delete: ")
            print(delete_item(inventory, name))

        elif choice == '5':
            if not inventory:
                print("No items available.")
            else:
                for name, details in inventory.items():
                    print(f"Name: {name}, Quantity: {details['quantity']}, Price: £{details['price']}")

        elif choice == '6':
            total = total_stock(inventory)
            print(f"Total stock in inventory: {total}")

        elif choice == '7':
            name = input("Enter the name of the item to purchase: ")
            quantity = int(input("Enter the quantity to purchase: "))
            message, till_balance = purchase_item(inventory, till_balance, name, quantity)
            print(message)
            print(f"Updated till balance: £{till_balance}")

        elif choice == '8':
            name = input("Enter the name of the item to return: ")
            quantity = int(input("Enter the quantity to return: "))
            message, till_balance = return_item(inventory, till_balance, name, quantity)
            print(message)
            print(f"Updated till balance: £{till_balance}")

        elif choice == '9':
            print("Exiting the Inventory Management System.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_interface()