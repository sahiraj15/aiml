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

    @staticmethod
    def print_item_menu():
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

    def set_item_line(self, name, description, price, quantity):
        self.item_line[name] = {'description': description, 'price': float(price), 'quantity': int(quantity)}
        print("Added item {} to the Shopping Cart\n".format(name))

    def remove_item(self, current_item_name):
        self.item_line.pop(current_item_name)
        print("Removed the Item: {}\n".format(current_item_name))

    def modify_item_values(self, current_item_name, current_item_description, current_item_price, current_item_quantity):
        print(current_item_name, "elements before modification: {}".format(self.item_line[current_item_name]))

        modify_indicator = False
        if current_item_description.upper() != 'N' and current_item_description != self.item_line[current_item_name]['description']:
            self.item_line[current_item_name]['description'] = current_item_description
            modify_indicator = True

        elif current_item_price.upper() != 'N' and float(current_item_price) != self.item_line[current_item_name]['price']:
            self.item_line[current_item_name]['price'] = float(current_item_price)
            modify_indicator = True

        elif current_item_quantity.upper() != 'N' and float(current_item_quantity) != self.item_line[current_item_name]['price']:
            self.item_line[current_item_name]['quantity'] = float(current_item_quantity)
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

    def print_sc_item_descriptions(self, operation):
        if self.total_quantity != 0:
            if operation != 'r' and operation != 'c':
                print("{}'s Shopping Cart - {}".format(self.customer_name, self.shopping_date))
                print("Number of Items: {}".format(self.total_quantity))

            for item, details in self.item_line.items():
                print("{} {} @${} = ${}".format(item, details['quantity'], math.trunc(details['price']), math.trunc(details['quantity'] * details['price'])))

            total_cost = 0
            if operation == 'o':
                for item, total in self.item_line.items():
                    total_cost += total['quantity'] * total['price']
                print("Total: ${}\n".format(math.trunc(total_cost))) if total_cost != 0 else False

                print("Items Descriptions: ")
                for item, details in self.item_line.items():
                    print("{}: {}".format(item, details['description']))

                print("")

        else:
            print("SHOPPING CART IS EMPTY\n")


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
    print("Adding items to the Shopping Cart:                   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        sc.print_item_menu()
        item_flag = input("Choose an option: ")

        sc.get_num_items_in_cart()
        if item_flag == 'a':
            item_name = input("Enter the item name: ")
            if item_name in sc.item_line.keys():
                print("Item already exist in the Cart, Use 'c' option on main menu\n")

            else:
                item_description = input("Enter the item description: ")
                item_price = input("Enter the item price: ")
                item_quantity = input("Enter the item quantity: ")
                sc.set_item_line(item_name, item_description, item_price, item_quantity)

        elif item_flag == 'r':
            if not sc.item_line.keys():
                print("SHOPPING CART IS EMPTY, skipping to the main menu\n")

            else:
                sc.print_item_descriptions()

                item_name = input("Enter the item to be removed: ")
                if item_name not in sc.item_line:
                    print("Product not found in cart, nothing removed. Skipping to the main menu\n")

                else:
                    sc.remove_item(item_name)

                sc.get_num_items_in_cart()
                if sc.total_quantity != 0:
                    sc.print_sc_item_descriptions(item_flag)

                else:
                    print("SHOPPING CART IS EMPTY\n")
                    continue

        elif item_flag == 'c':
            if not sc.item_line.keys():
                print("SHOPPING CART IS EMPTY, skipping to the main menu\n")

            else:
                sc.print_sc_item_descriptions(item_flag)
                print("")

                item_name = input("Enter the item to be modified: ")
                if item_name not in sc.item_line:
                    print("Item not found in the Shopping Cart, skipping to the main menu\n")

                else:
                    print("Modifying the item: {}".format(item_name))
                    description = input("New item description(old: {}), N: NoChange: ".format(sc.item_line[item_name]['description']))
                    price = input("New item price(old: {}), N: NoChange: ".format(sc.item_line[item_name]['price']))
                    quantity = input("New item quantity(old: {}), N: NoChange: ".format(sc.item_line[item_name]['quantity']))

                    sc.modify_item_values(item_name, description, price, quantity)

        elif item_flag == 'i':
            if sc.item_line.keys():
                sc.print_item_descriptions()

            else:
                print("SHOPPING CART IS EMPTY, skipping to the main menu\n")

        elif item_flag == 'o':
            sc.get_num_items_in_cart()
            sc.print_sc_item_descriptions(item_flag)

        elif item_flag == 'q':
            print("Shopping Cart operations completed. ")
            break

        else:
            print("Enter a valid Shopping Cart operation, skipping to the main menu\n")
