prices = [12.99, 8.50, 15.75, 23.00, 7.25]

# Write your code here
total = 0              # 1) initialize accumulator
for price in prices:   # 2) loop over each item
    total += price     # 3) update accumulator
print(total)           # 4) use the accumulated result


"""This exercise is all about using a loop to accumulate a running total. Here are the main concepts at play:

    Accumulator Pattern
    – You start by creating a variable (often called an “accumulator”) and initialize it to a base value—in this case 0.
    – Inside the loop, you continually update that accumulator by adding each new element’s value to it.

    For-Loop Iteration
    – A for loop lets you step through each element of a list one by one.
    – On each iteration, the loop variable (here named price) holds the current element from the list.

    In-Place Addition
    – Writing total += price is shorthand for total = total + price. It takes whatever value total holds now and adds the new price, then stores the result back into total.

    Final Output
    – After the loop has visited every item, total contains the sum of all prices.
    – You then print (or return) that final value.

Putting these together, the pattern looks like:

python
1
2
3
4
total = 0              # 1) initialize accumulator
for price in prices:   # 2) loop over each item
    total += price     # 3) update accumulator
print(total)           # 4) use the accumulated result

This pattern—initialize, loop/update, then use—appears often whenever you need to sum, count, or combine values from a collection.

can you explain in which real life scenario this loop is practical? I don't quite get its purpose

A classic real-world use case for this kind of loop is in any situation where you need to aggregate or sum up a series of numeric values—for example:

    Grocery store checkout
    • As each item is scanned, its price is added to a running total.
    • The loop automates “take next scanned price → add to total” until the basket is empty.

    Expense tracking
    • You have a list of daily expenditures (coffee, lunch, transport, etc.).
    • A loop sums them all to show your total spend for the week or month.

    Invoicing or billing systems
    • Line-items on an invoice each carry a price.
    • A for-loop quickly computes the grand total before applying taxes or discounts.

    Budget forecasting
    • You project various cost categories (rent, utilities, salaries).
    • Summing them gives your overall budget requirement.

In each case, the pattern is identical:

• Start total = 0
• For each price in your price list, do total += price
• Once the loop finishes, total holds the sum of all entries.
"""