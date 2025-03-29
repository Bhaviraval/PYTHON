grocery_prices = {
    "apple": 50,
    "banana": 30,
    "milk": 60,
    "bread": 40,
    "eggs": 70
}

grocery_quantity = {
    "apple": 2,
    "banana": 5,
    "milk": 1,
    "bread": 2,
    "eggs": 1
}

total_bill = sum(grocery_prices[item] * grocery_quantity[item] for item in grocery_prices if item in grocery_quantity)

print("Total Bill:", total_bill)
