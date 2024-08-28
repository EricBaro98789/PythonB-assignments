# List of products and their prices
products = ["Laptop", "Smartphone", "Tablet", "Smartwatch"]
prices = [1000, 500, 300, 200]

# Print each product with its price and index
i = 0
for product in products:
    print(f"{i + 1}. {product} costs ${prices[i]}")
    i += 1
