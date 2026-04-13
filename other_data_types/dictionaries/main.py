grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

#Retrieve the details of the item "Bread" from the dictionary and store them in the bread_details variable.
bread_details = grocery_inventory["Bread"]
print("Details of Bread:", bread_details)
#Add a new item, "Cookies", with product ID 143 and category "Bakery".
grocery_inventory.update({"Cookies": (143, "Bakery")})
#Another way to add a new value or update a dictionary
print("Inventory after adding Cookies:", grocery_inventory)
grocery_inventory["Cookies"] = (143, "Bakery")
#Remove the item "Eggs" from the dictionary.

grocery_inventory.pop("Eggs") #HERE WE REMOVE ENTIRELY FROM THE DICTIONARY
print("Inventory after removing Eggs:",grocery_inventory)

