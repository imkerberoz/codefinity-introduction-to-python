# 1. Create the Dictionary
grocery_inventory ={
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# 2. Check and Update Price ===

# TWO ways to get the eggs price =
# FIRST way:
eggs_data  = grocery_inventory.get("Eggs")     # returns ("Dairy", 5.50, 30)
eggs_price = eggs_data[1]                     # index 1 → 5.50
print("Price of Eggs is:", eggs_price)

#SECOND way (CLEANER AND MORE CONSICE WAY)
eggs_price = grocery_inventory["Eggs"][1]
print(eggs_price)

if "Eggs" in grocery_inventory and eggs_price > 5:
    print( "Eggs are too expensive, reducing the price by $1.")
    new_eggs_price = eggs_price - 1
else:
    print("The price of Eggs is reasonable.")

# 3. Add a New Item
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

# 4. Manage Stock for MILK

stock_of_milk = grocery_inventory["Milk"][2]
if stock_of_milk < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    new_stock = stock_of_milk + 20
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        new_stock,
    )
else:
    print("Milk has sufficient stock.")

# ANOTHER way to do the same ===

# instead of dozens of lines just for "Milk",
# loop over a one-element list and unpack directly:
for item in ["Milk"]:
    category, price, stock = grocery_inventory[item]
    if stock < 10:
        print(f"{item} needs to be restocked. Increasing stock by 20 units.")
        grocery_inventory[item] = (category, price, stock + 20)
    else:
        print(f"{item} has sufficient stock.")

"""
1. Loops over whatever items you want to check (here, just "Milk").
2. Unpacks (category, price, stock) in one go.
3. Updates the dictionary in a single assignment."""'


# 5. Remove Item Based on Price

apple_price = grocery_inventory["Apples"][1]
if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

# 6. Final Print
print("Updated inventory:", grocery_inventory)