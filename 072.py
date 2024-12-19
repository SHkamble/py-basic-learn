products = [
    {"name": "Laptop","price":1000},
    {"name": "Smartphone", "price":500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]
print(type(products))
print(type(products[0]))


def is_affordable(item):
    return item["price"] < 500

affordable_items = list(filter(is_affordable,products))
print(affordable_items[0]["name"]+str (affordable_items[0]["price"]))
print(affordable_items[1]["name"]+str (affordable_items[1]["price"]))