import math

"""
CSE 111 - Lauren Snyder
Computes and prints the number of boxes necessary to hold given items.
"""

num_items = input("Enter the number of items: ")
num_items_per_box = input("Enter the number of items per box: ")

total_boxes = math.ceil(int(num_items) / int(num_items_per_box))

print(f"For {num_items} items, packing {num_items_per_box} items in each box, you will need {total_boxes} boxes.")

