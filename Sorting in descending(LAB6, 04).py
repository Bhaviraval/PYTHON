food_items = [('chocolates', 50), ('strawberry', 20), ('milk', 30)]

sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)
print("Sorted food items by price:", sorted_items)
