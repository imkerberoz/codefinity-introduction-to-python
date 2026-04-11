#Initializing 
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Main List
deli_dept = [meat, cheese, condiment]

print(f"Initial Deli List:", deli_dept)

# Restock Item algorithm
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100
    
# Seasonal Meat (Append)
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#Condiment removal
deli_dept.remove(condiment)

# Sorting
deli_dept.sort()

print(f"Updated Deli List:", deli_dept)


