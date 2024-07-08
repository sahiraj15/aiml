import math
from datetime import datetime


class ItemToPurchase:
    def __init__(self):
        # Product entities
        self.item_line = {}
        self.total_cost = 0

    def add_item(self, inp_name, inp_desc, inp_price, inp_quantity):
        self.item_line[inp_name] = {'description': inp_desc, 'price': float(inp_price), 'quantity': int(inp_quantity)}

    def print_item_wise_cost_summary(self):
        print("\nTOTAL COST")

        self.total_cost = 0
        for item_val in self.item_line.keys():
            item_cost = 0
            eval_price = self.item_line[item_val]['price']
            eval_quantity = self.item_line[item_val]['quantity']

            if eval_price - math.trunc(eval_price) > 0:
                item_cost = eval_quantity * eval_price
                print("{} {} @ ${} = ${}".format(item_val, eval_quantity, eval_price, item_cost))
            else:
                item_cost = eval_quantity * int(eval_price)
                print("{} {} @ ${} = ${}".format(item_val, eval_quantity, int(eval_price), item_cost))

            self.total_cost += item_cost

        print("Total: ${}".format(self.total_cost))


class ShoppingCart:
    def __init__(self, customer_name: str = 'none', shopping_date: str = 'none', items_list: dict = {}):

        # Customer details
        self.customer_name = customer_name
        self.shopping_date = shopping_date

        # Purchase entities
        self.total_quantity = 0
        self.total_cost = 0

        # Cart parameters
        self.cart_items = []
        self.item_line = items_list

    def add_item(self, inp_name, inp_desc, inp_price, inp_quantity):
        self.item_line[inp_name] = {'description': inp_desc, 'price': float(inp_price), 'quantity': int(inp_quantity)}

    def remove_item(self, curr_item_name):
        self.item_line.pop(curr_item_name)
        print("Removed the Item: {}\n".format(curr_item_name))

    def modify_item_values(self, curr_item_name, current_item_desc, curr_item_price, curr_item_quantity):
        print(curr_item_name, "elements before changes: {}".format(self.item_line[curr_item_name]))

        price_ind = (-100 if str(curr_item_price).upper() != 'N' else 0)
        quant_ind = (-100 if str(curr_item_quantity).upper() != 'N' else 0)

        modify_indicator = False
        if current_item_desc.upper() != 'N' and current_item_desc != self.item_line[curr_item_name]['description']:
            self.item_line[curr_item_name]['description'] = current_item_desc
            modify_indicator = True

        if price_ind == -100 and curr_item_price != str(self.item_line[curr_item_name]['price']):
            self.item_line[curr_item_name]['price'] = float(curr_item_price)
            modify_indicator = True

        if quant_ind == -100 and curr_item_quantity != str(self.item_line[curr_item_name]['quantity']):
            print("Inside the loop: {} | {}".format(int(curr_item_quantity), self.item_line[curr_item_name]['quantity']))
            self.item_line[curr_item_name]['quantity'] = int(curr_item_quantity)
            modify_indicator = True

        if not modify_indicator:
            print("No changes identified to the item: {}\n".format(curr_item_name))

        print(curr_item_name, "elements post changes: {}\n".format(self.item_line[curr_item_name])) if modify_indicator else None

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

    @staticmethod
    def print_customer_info(inp_user_name, inp_shopping_date):
        print("\nCustomer name: {}".format(inp_user_name))
        print("Today's date:: {}\n".format(inp_shopping_date))

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
                print("")

        else:
            print("SHOPPING CART IS EMPTY\n")

    def print_item_descriptions(self, operation):
        print("\nItem Descriptions") if operation == 'i' or operation == 'o' else False
        for item, details in self.item_line.items():
            print("{}: {}".format(item, details['description']))
        print("")

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


# Main program starts here
if __name__ == "__main__":
    items = ItemToPurchase()

    print("\nItem1")
    item_name1 = input("Enter the item name: \n")
    # item_desc1 = input("Enter the item description: \n")
    item_price1 = input("Enter the item price: \n")
    item_quant1 = input("Enter the item quantity: \n")

    print("\nItem2")
    item_name2 = input("Enter the item name: \n")
    # item_desc2 = input("Enter the item description: \n")
    item_price2 = input("Enter the item price: \n")
    item_quant2 = input("Enter the item quantity: \n")

    # Input validations
    if float(item_price1) <= 0:
        raise "Item1 price shall be a positive integer or decimal value."
    elif int(item_quant1) <= 0:
        raise "Item1 quantity shall be a positive integer value."
    elif float(item_price2) <= 0:
        raise "Item2 price shall be a positive integer or decimal value."
    elif int(item_quant2) <= 0:
        raise "Item2 quantity shall be a positive integer value."

    items.add_item(item_name1, 'Item1 description', item_price1, item_quant1)
    items.add_item(item_name2, 'Item2 description', item_price2, item_quant2)
    items.print_item_wise_cost_summary()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ShoppingCart inputs start here
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("")
    print("# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("# Shopping cart interation starts:                          ")
    print("# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("")
    user_name = input("Enter customer's name: \n")
    cart_date = input("Enter today's date: \n")
    # invoice_date = datetime.strptime(input("Enter today's date('YYYY-MM-DD'): \n"), '%Y-%m-%d')
    # cart_date = invoice_date.strftime('%B %d, %Y')

    # Set instance parameters and print the item description
    sc = ShoppingCart(user_name, cart_date, items.item_line)
    sc.print_customer_info(sc.customer_name, sc.shopping_date)

    # Shopping cart modification done from here
    while True:
        sc.print_item_menu()
        item_flag = input("Choose an option: ")

        sc.get_num_items_in_cart()
        if item_flag == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            if item_name in sc.item_line.keys():
                print("Item already exist in the Cart, Use 'c' option for modifying an item in the cart\n")

            else:
                item_description = input("Enter the item description: ")
                item_price = input("Enter the item price: ")
                item_quantity = input("Enter the item quantity: ")
                sc.add_item(item_name, item_description, item_price, item_quantity)
                print("Added item {} to the Shopping Cart\n".format(item_name))

        elif item_flag == 'r':
            print("\nREMOVE ITEM FROM CART")
            if not sc.item_line.keys():
                print("SHOPPING CART IS EMPTY, skipping to the main menu\n")

            else:
                sc.print_item_descriptions(item_flag)

                item_name = input("Enter name of item to remove: \n")
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
            print("\nCHANGE ITEM QUANTITY")
            if not sc.item_line.keys():
                print("SHOPPING CART IS EMPTY, skipping to the main menu\n")

            else:
                sc.print_sc_item_descriptions(item_flag)

                item_name = input("\nEnter the item name: \n")
                if item_name not in sc.item_line:
                    print("Item not found in the Shopping Cart, skipping to the main menu\n")

                else:
                    print("Modifying the item: {}".format(item_name))
                    description = input("Enter new description(old: {}), N: NoChange: \n".format(sc.item_line[item_name]['description']))
                    price = input("Enter new price(old: {}), N: NoChange: \n".format(sc.item_line[item_name]['price']))
                    quantity = input("Enter new quantity(old: {}), N: NoChange: \n".format(sc.item_line[item_name]['quantity']))

                    sc.modify_item_values(item_name, description, price, quantity)

        elif item_flag == 'i':
            if sc.item_line.keys():
                sc.print_item_descriptions(item_flag)

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
