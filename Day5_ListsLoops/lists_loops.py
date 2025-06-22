# Shopping List Formatter

items = ["bread", "milk", "coffee", "avocado"]

print("🛒 Shopping List:")

for index, item in enumerate(items, start=1):
    print(f"{index}. {item.title()}")
