# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

apple_count = shelf.count("apples")
grape_count = shelf.count("grapes")
orange_count = shelf.count("oranges")

print("Number of Apples:",apple_count)

orange_index = shelf.index("oranges")
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)
#-------------------------------------------------
if apple_count <  5:
    print("Apples need to be restocked.")
else: 
    print("Apples are sufficiently stocked.")
#-------------------------------------------------
if grape_count ==  1:
    print("Grapes need to be restocked.")
else: 
    print("Grapes are sufficiently stocked.")
#-------------------------------------------------
if "oranges" in shelf:
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")
#-------------------------------------------------
















