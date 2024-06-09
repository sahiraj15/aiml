import math


class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.total_cost = 0

    def set_item_comps(self, x_item_name, x_item_price, x_item_quantity):
        self.item_name = x_item_name
        self.item_price = x_item_price
        self.item_quantity = x_item_quantity

    def get_item_comps(self):
        pass

    def print_item_cost(self):
        if self.item_price - math.trunc(self.item_price) > 0:
            self.total_cost = self.item_quantity * self.item_price
        else:
            self.total_cost = self.item_quantity * int(self.item_price)
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.total_cost))


if __name__ == "__main__":
    item_list = []

    print("")
    item_dict1 = {"item_name1": input("Item1 Name: "), "item_price1": float(input("Item1 Price: ")), "item_quant1": int(input("Item1 Quantity: "))}
    item_list.append(item_dict1)

    print("")
    item_dict2 = {"item_name2": input("Item2 Name: "), "item_price2": float(input("Item2 Price: ")), "item_quant2": int(input("Item2 Quantity: "))}
    item_list.append(item_dict2)

    # Input validations
    if item_list[0]["item_price1"] <= 0:
        raise "Item1 price shall be a positive integer or decimal value."
    elif item_list[0]["item_quant1"] <= 0:
        raise "Item1 quantity shall be a positive integer value."
    elif item_list[1]["item_price2"] <= 0:
        raise "Item2 price shall be a positive integer or decimal value."
    elif item_list[1]["item_quant2"] <= 0:
        raise "Item2 quantity shall be a positive integer value."

    print("")
    purchase_items1 = ItemToPurchase()
    purchase_items1.set_item_comps(item_list[0]["item_name1"], item_list[0]["item_price1"], item_list[0]["item_quant1"])

    print("")
    purchase_items2 = ItemToPurchase()
    purchase_items2.set_item_comps(item_list[1]["item_name2"], item_list[1]["item_price2"], item_list[1]["item_quant2"])

    print("")
    purchase_items1.print_item_cost()
    purchase_items2.print_item_cost()
    total_purchase_cost = purchase_items1.total_cost + purchase_items2.total_cost
    print("Total: {}".format(total_purchase_cost))
