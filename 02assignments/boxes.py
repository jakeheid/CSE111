import math

items = input("Please enter the number of items my guy: ")
box = input("Please enter the number of items per box broh: ")

numb_items = int(items)
items_box = int(box)

numb_box = math.ceil(numb_items / items_box)
print(f"the total number of boxes needed to pack {numb_items} items with {items_box} items per box is {numb_box}. ")