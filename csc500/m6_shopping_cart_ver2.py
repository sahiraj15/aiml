import math
from datetime import datetime


class ShoppingCart:
    def __init__(self):
        # Customer details
        self.customer_name = None
        self.shopping_date = None

        # Shopping details
        self.total_quantity = 0
        self.total_cost = 0
        self.cart_items = []

        # Product details
        self.item_line = {}

        self.item_name = None
        self.item_description = None
        self.item_price = 0.0
        self.item_quantity = 0

    def set_item_line(self, name, description, price):
        self.item_line[name] = {'description': description, 'price': float(price), 'quantity': 0}
        print("Added item {} to the ItemMaster\n".format(name))

    @staticmethod
    def print_item_menu():
        print("Item Operations: ")
        print("a - Add an Item")
        print("r - Remove an Item")
        print("m - Modify an Item")
        print("i - Output Items Description")
        print("d - Done adding items to master list ")
        print("")

    def remove_item(self, current_item_name):
        if current_item_name in self.item_line:
            self.item_line.pop(current_item_name)
            print("Removed the Item: {}\n".format(current_item_name))
        else:
            print("Product not found in cart, Nothing removed.")

    def modify_current_item_names(self, current_item_name, description, price):
        print(current_item_name, "elements before modification: {}".format(self.item_line[current_item_name]))

        modify_indicator = False
        if description.upper() != 'N' and description != self.item_line[current_item_name]['description']:
            self.item_line[current_item_name]['description'] = description
            modify_indicator = True
        elif price.upper() != 'N' and float(price) != self.item_line[current_item_name]['price']:
            self.item_line[current_item_name]['price'] = float(price)
            modify_indicator = True
        else:
            print("No modifications identified to the Item: {}\n".format(current_item_name))

        print(current_item_name, "elements post modification: {}\n".format(self.item_line[current_item_name])) if modify_indicator else None

    def print_item_descriptions(self):
        print("")

        print("Item Descriptions")
        for item, details in self.item_line.items():
            print("{}: {}".format(item, details['description']))
        print("")

    @staticmethod
    def print_menu():
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items descriptions")
        print("o - Output shopping cart")
        print("q - Quit.")
        print("")

    def set_customer_parameters(self, customer_name: str, shopping_date: str):
        self.customer_name = customer_name
        self.shopping_date = shopping_date

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        print("Added 1 item to the cart.")

    def remove_cart_item(self, current_item_name):
        if current_item_name in self.cart_items:
            self.cart_items.remove(current_item_name)
            self.item_line[current_item_name]['quantity'] = 0
            print("Removed the cart item: {}".format(current_item_name))
        else:
            print("Item not found in cart, Nothing removed.")

    def modify_cart_items(self, item_to_purchase, quantity):
        if item_to_purchase not in self.item_line:
            print("Item not found in cart. Nothing modified.")
        else:
            alter_items = self.item_line[item_to_purchase]
            print(item_to_purchase, " elements before modification:", alter_items)

            if quantity.upper() != 'N' and float(quantity) != self.item_line[item_to_purchase]['quantity']:
                self.item_line[item_to_purchase]['quantity'] = int(quantity)
            else:
                print("No modification applied to Item Quantity.")

            print(item_to_purchase, " elements after modification:", alter_items)

    def get_num_items_in_cart(self):
        self.total_quantity = 0
        for item, total in self.item_line.items():
            self.total_quantity += total['quantity']

        return self.total_quantity

    def get_cost_of_cart(self):
        self.total_cost = 0
        for item, total in self.item_line.items():
            self.total_cost += total['quantity'] * total['price']

        return self.total_cost

    def print_total(self, operation):
        if self.total_quantity != 0:
            if operation != 'r' and operation != 'c':
                print("{}'s Shopping Cart - {}".format(self.customer_name, self.shopping_date))
                print("Number of Items: {}".format(self.total_quantity))

            for item, details in self.item_line.items():
                if details['quantity'] != 0:
                    print("{} {} @${} = ${}".format(item, details['quantity'], math.trunc(details['price']), math.trunc(details['quantity'] * details['price'])))
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.shopping_date))
        print("Item Descriptions")
        for item, details in self.item_line.items():
            print("{}: {}".format(item, details['description']))

    def print_sc_item_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.shopping_date))
        print("Item Descriptions")
        for item, details in self.item_line.items():
            if item in self.cart_items:
                print("{}: {}".format(item, details['description']))


if __name__ == "__main__":
    # Collect user details
    sc = ShoppingCart()

    user_name = input("Enter Your Name: ")
    invoice_date = datetime.strptime(input("Enter the Invoice date('YYYY-MM-DD'): "), '%Y-%m-%d')
    require_date_format = invoice_date.strftime('%B %d, %Y')

    # Set instance parameters and print the item description
    sc.set_customer_parameters(user_name, require_date_format)
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Adding items to the Master List:                     ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    item_flag = 'a'
    while item_flag != 'd':
        sc.print_item_menu()
        item_flag = input("Enter product operation or quit: ")

        if item_flag == 'a':
            item_name = input("Enter the item name: ")

            if item_name in sc.item_line.keys():
                print("Item already exist in the ItemMaster list\n")
            else:
                item_price = input("Enter the item description: ")
                item_quantity = input("Enter the item price: ")
                sc.set_item_line(item_name, item_price, item_quantity)

        elif item_flag == 'r':
            if not sc.item_line.keys():
                print("No items available in the ItemMaster, operation can't be performed\n")
            else:
                item_name = input("Enter the item to be removed: ")
                if item_name not in sc.item_line:
                    print("Product not found in cart, Nothing removed\n")
                else:
                    sc.remove_item(item_name)

        elif item_flag == 'm':
            if not sc.item_line.keys():
                print("No items available in the ItemMaster, operation can't be performed\n")
            else:
                sc.print_item_descriptions()

                item_name = input("Enter the item to be modified: ")
                if item_name not in sc.item_line:
                    print("Item name not found, enter a valid name\n")
                elif item_name == 'q':
                    print("Exiting item modification\n")
                    break
                else:
                    print("Modifying the item: {}".format(item_name))
                    print("list : {}".format(sc.item_line))
                    new_description = input("Enter a new description(old: {}), N: NoChange: ".format(sc.item_line[item_name]['description']))
                    new_price = input("Enter a new price(old: {}), N: NoChange: ".format(sc.item_line[item_name]['price']))
                    sc.modify_current_item_names(item_name, new_description, new_price)

        elif item_flag == 'i':
            if sc.item_line.keys():
                sc.print_item_descriptions()
            else:
                print("No items available in the ItemMaster\n")

        elif item_flag == 'q':
            print("Cart operations aborted, any items added to the ItemMaster will be discarded. ")
            break

        else:
            print("Unidentified operation, please enter a valid input\n")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Processing the shopping cart items purchased:        ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if not sc.item_line.keys():
        raise Exception("No items found in the ItemMaster, please add them\n")

    while True:
        sc.print_menu()

        cart_operation = input("Choose a shopping cart operation: ")
        sc.get_num_items_in_cart()
        sc.get_cost_of_cart()

        if cart_operation == 'a' or cart_operation == 'c' or cart_operation == 'i' or cart_operation == 'o' or cart_operation == 'r':
            if cart_operation == 'a':
                purchase_item = input("Add item to the purchase list: ")
                if purchase_item in sc.item_line:
                    if purchase_item not in sc.cart_items:
                        sc.add_item(purchase_item)
                        print(sc.cart_items)
                    else:
                        print("Items already added to the cart, please use 'c' operation to modify the quantity.")

                    sc.item_line[purchase_item]['quantity'] += 1
                else:
                    print("Enter a valid purchase item, available items are: ")
                    sc.print_descriptions()
            elif cart_operation == 'r':
                if sc.total_quantity != 0:
                    print("Items in the cart are:")
                    sc.print_total(cart_operation)
                else:
                    print("SHOPPING CART IS EMPTY")
                    print("")
                    continue

                sc.remove_item(input("Enter the item name to be removed: "))
            elif cart_operation == 'c':
                if sc.total_quantity != 0:
                    print("Items in the cart are:")
                    sc.print_total(cart_operation)
                else:
                    print("SHOPPING CART IS EMPTY")
                    print("")
                    continue

                while True:
                    modify_item_name = input("Enter item name to be modified: ")
                    if modify_item_name not in sc.cart_items:
                        print("Enter a valid item name, or q for existing the choice: ")
                    elif modify_item_name == 'q':
                        print("Exiting the change operation")
                        break
                    else:
                        sc.modify_cart_items(modify_item_name, input("Enter new item quantity, Enter N for no change: "))
                        break

            elif cart_operation == 'i':
                sc.print_descriptions()

            elif cart_operation == 'o':
                sc.get_num_items_in_cart()
                sc.get_cost_of_cart()
                sc.print_total(cart_operation)

                print("Total: ${}\n".format(math.trunc(sc.total_cost))) if sc.total_cost != 0 else False
                sc.print_sc_item_descriptions()
                exit(0)
            else:
                pass
        elif cart_operation == 'q':
            print("Cart operations aborted, items will be discarded. ")
            break
        else:
            print("Enter a valid cart operation. ")

        print("")
