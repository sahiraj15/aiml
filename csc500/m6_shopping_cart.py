import datetime
import logging
import regex as re


class ShoppingCart:
    def __init__(self, customer_name: None, shopping_date):
        self.customer_name = customer_name
        self.shopping_date = shopping_date
        self.cart_items = []

        self.item_details = {
            'Nike Romaleos': {'item_description': 'Volt color, Weightlifting shoes', 'item_price': 189, 'item_quantity': 0},
            'Chocolate Chips': {'item_description': 'Semi-sweet', 'item_price': 3, 'item_quantity': 0},
            'Powerbeats 2 Headphones': {'item_description': 'Bluetooth headphones', 'item_price': 128, 'item_quantity': 0}
        }

    def print_menu(self):
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("")

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        print("Added 1 item to the cart.")

    def remove_item(self, item_name):
        if item_name in self.cart_items:
            self.cart_items.remove(item_name)
            self.item_details[item_name]['item_quantity'] = 0
            print("Removed the cart item: {}".format(item_name))
        else:
            print("Item not found in cart, Nothing removed.")

    def modify_item(self, ItemToPurchase, item_description, item_price, item_quantity):
        if ItemToPurchase not in self.item_details:
            print("Item not found in cart. Nothing modified.")
        else:
            alter_items = self.item_details[ItemToPurchase]
            print(ItemToPurchase, " elements before modification:", alter_items)

            if item_description.upper() != 'N' and item_description != self.item_details[ItemToPurchase]['item_description']:
                self.item_details[ItemToPurchase]['item_description'] = item_description
            else:
                print("No modification to Item Description.")

            if item_quantity.upper() != 'N' and float(item_quantity) != self.item_details[ItemToPurchase]['item_quantity']:
                self.item_details[ItemToPurchase]['item_quantity'] = float(item_quantity)
            else:
                print("No modification to Item Quantity.")

            if item_price.upper() != 'N' and float(item_price) != self.item_details[ItemToPurchase]['item_price']:
                self.item_details[ItemToPurchase]['item_price'] = float(item_price)
            else:
                print("No modification to Item Price.")

            print(ItemToPurchase, " elements after modification:", alter_items)

    def get_num_items_in_cart(self):
        self.total_quantity = 0
        for item, total in self.item_details.items():
            self.total_quantity += total['item_quantity']

        return self.total_quantity

    def get_cost_of_cart(self):
        self.total_cost = 0
        for item, total in self.item_details.items():
            self.total_cost += total['item_quantity'] * total['item_price']

        return self.total_cost

    def print_total(self, option):
        if self.total_quantity != 0:
            if option != 'r' and option != 'c':
                print("OUTPUT SHOPPING CART")
                print(self.customer_name,"'s Shopping Cart - ", self.shopping_date)
                print("Items Description")
                print("Number of Items: {}".format(self.total_quantity))

            for item, details in self.item_details.items():
                if details['item_quantity'] != 0:
                    print("{} {} @${} = ${}".format(item, details['item_quantity'], details['item_price'], details['item_quantity'] * details['item_price']))
        else:
            print("SHOPPING CART IS EMPTY")

        print("")

    def print_descriptions(self):
        print("")
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(self.customer_name,"'s Shopping Cart -", self.shopping_date)

        print("Item Descriptions")
        for item, details in self.item_details.items():
            print("{}: {}".format(item, details['item_description']))

        print("")


if __name__ == "__main__":
    sc = ShoppingCart('John Doe', datetime.datetime)

    # Item selection starts here
    while True:
        sc.print_menu()

        option = input("Choose an option: ")
        if re.search('[acior]', option):
            print("")

            if option == 'a':
                purchase_item = input("Add item to the purchase list: ")
                if purchase_item in sc.item_details:
                    if purchase_item not in sc.cart_items:
                        sc.add_item(purchase_item)
                        print(sc.cart_items)

                    sc.item_details[purchase_item]['item_quantity'] += 1
                else:
                    print("Enter a valid purchase item, available items are: ")
                    sc.print_descriptions()
            elif option == 'r':
                print("Items in the cart are:")
                sc.get_num_items_in_cart()
                sc.get_cost_of_cart()
                sc.print_total(option)

                sc.remove_item(input("Enter the item name to be removed: "))
            elif option == 'c':
                print("Items in the cart are:")
                sc.get_num_items_in_cart()
                sc.get_cost_of_cart()
                sc.print_total(option)

                while True:
                    modify_item_name = input("Enter item name to be modified: ")
                    if modify_item_name not in sc.cart_items:
                        print("Enter a valid item name, or q for existing the choice: ")
                    elif modify_item_name == 'q':
                        print("Exiting the Change option")
                        break
                    else:
                        item_description = input("Enter new item description, Enter N for no change: ")
                        item_price = input("Enter new item price, Enter N for no change: ")
                        item_quantity = input("Enter new item quantity, Enter N for no change: ")

                        sc.modify_item(modify_item_name, item_description, item_price, item_quantity)
                        break

            elif option == 'i':
                sc.print_descriptions()
            elif option == 'o':
                sc.get_num_items_in_cart()
                sc.get_cost_of_cart()
                sc.print_total(option)
            else:
                pass
        elif re.search('[q]', option):
            print("Option selection completed.")
            sc.get_num_items_in_cart()
            sc.get_cost_of_cart()
            sc.print_total(option)
            break
        else:
            print("Enter a valid option. ")

        print("")
