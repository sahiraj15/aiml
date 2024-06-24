from datetime import datetime
import regex as re


class ShoppingCart:
    def __init__(self, customer_name: None, shopping_date):
        self.customer_name = customer_name
        self.shopping_date = shopping_date
        self.cart_items = []

        self.item_details = {
            'Nike Romaleos': {'description': 'Volt color, Weightlifting shoes', 'price': 189, 'quantity': 0},
            'Chocolate Chips': {'description': 'Semi-sweet', 'price': 3, 'quantity': 0},
            'Powerbeats 2 Headphones': {'description': 'Bluetooth headphones', 'price': 128, 'quantity': 0}
        }

        self.total_quantity = 0
        self.total_cost = 0

    @staticmethod
    def print_menu():
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("")

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        print("Added 1 item to the cart.")

    def remove_item(self, item_name):
        if item_name in self.cart_items:
            self.cart_items.remove(item_name)
            self.item_details[item_name]['quantity'] = 0
            print("Removed the cart item: {}".format(item_name))
        else:
            print("Item not found in cart, Nothing removed.")

    def modify_item(self, item_to_purchase, quantity):
        if item_to_purchase not in self.item_details:
            print("Item not found in cart. Nothing modified.")
        else:
            alter_items = self.item_details[item_to_purchase]
            print(item_to_purchase, " elements before modification:", alter_items)

            if quantity.upper() != 'N' and float(quantity) != self.item_details[item_to_purchase]['quantity']:
                self.item_details[item_to_purchase]['quantity'] = int(quantity)
            else:
                print("No modification applied to Item Quantity.")

            print(item_to_purchase, " elements after modification:", alter_items)

    def get_num_items_in_cart(self):
        self.total_quantity = 0
        for item, total in self.item_details.items():
            self.total_quantity += total['quantity']

        return self.total_quantity

    def get_cost_of_cart(self):
        self.total_cost = 0
        for item, total in self.item_details.items():
            self.total_cost += total['quantity'] * total['price']

        return self.total_cost

    def print_total(self, operation):
        if self.total_quantity != 0:
            if operation != 'r' and operation != 'c':
                print("OUTPUT SHOPPING CART")
                print("{}'s Shopping Cart - {}".format(self.customer_name, self.shopping_date))
                print("Number of Items: {}".format(self.total_quantity))

            for item, details in self.item_details.items():
                if details['quantity'] != 0:
                    print("{} {} @${} = ${}".format(item, details['quantity'], details['price'], details['quantity'] * details['price']))
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        print("")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.shopping_date))

        print("Item Descriptions")
        for item, details in self.item_details.items():
            print("{}: {}".format(item, details['description']))

        print("")


if __name__ == "__main__":
    invoice_date = datetime.now().strftime("%B %d, %Y")

    # Item selection starts here
    sc = ShoppingCart('John Doe', invoice_date)
    while True:
        sc.print_menu()

        option = input("Choose an option: ")
        sc.get_num_items_in_cart()
        sc.get_cost_of_cart()

        if re.search('[acior]', option):
            print("")

            if option == 'a':
                purchase_item = input("Add item to the purchase list: ")
                if purchase_item in sc.item_details:
                    if purchase_item not in sc.cart_items:
                        sc.add_item(purchase_item)
                        print(sc.cart_items)
                    else:
                        print("Items already added to the cart, please use 'c' option to modify the quantity.")

                    sc.item_details[purchase_item]['quantity'] += 1
                else:
                    print("Enter a valid purchase item, available items are: ")
                    sc.print_descriptions()
            elif option == 'r':
                if sc.total_quantity != 0:
                    print("Items in the cart are:")
                    sc.print_total(option)
                else:
                    print("SHOPPING CART IS EMPTY")
                    continue

                sc.remove_item(input("Enter the item name to be removed: "))
            elif option == 'c':
                if sc.total_quantity != 0:
                    print("Items in the cart are:")
                    sc.print_total(option)
                else:
                    print("SHOPPING CART IS EMPTY")
                    print("")
                    continue

                while True:
                    modify_item_name = input("Enter item name to be modified: ")
                    if modify_item_name not in sc.cart_items:
                        print("Enter a valid item name, or q for existing the choice: ")
                    elif modify_item_name == 'q':
                        print("Exiting the change option")
                        break
                    else:
                        sc.modify_item(modify_item_name, input("Enter new item quantity, Enter N for no change: "))
                        break

            elif option == 'i':
                sc.print_descriptions()
            elif option == 'o':
                sc.get_num_items_in_cart()
                sc.get_cost_of_cart()
                sc.print_total(option)
                print("Total: ${}".format(sc.total_cost))
            else:
                pass
        elif re.search('[q]', option):
            print("Cart operations aborted, items will be discarded. ")
            break
        else:
            print("Enter a valid item option. ")

        print("")
