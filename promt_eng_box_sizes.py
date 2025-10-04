from itertools import product

# Define the box types and their properties
boxes = {
    'Small': {'volume': 10, 'price': 1.99},
    'Medium': {'volume': 22, 'price': 4.99},
    'Large': {'volume': 38, 'price': 5.99}
}

# Budget limit
budget = 20.00

# Function to find the best combination of boxes
def find_best_combination(boxes, budget):
    max_volume = 0
    best_combination = None

    # Generate all combinations of boxes with a reasonable limit on the quantity
    for quantities in product(range(0, 21), repeat=len(boxes)):
        total_cost = sum(quantities[i] * list(boxes.values())[i]['price'] for i in range(len(boxes)))
        total_volume = sum(quantities[i] * list(boxes.values())[i]['volume'] for i in range(len(boxes)))

        # Check if the total cost matches the budget
        if total_cost == budget:
            # Update if this combination has a higher volume
            if total_volume > max_volume:
                max_volume = total_volume
                best_combination = quantities

    return best_combination, max_volume

# Calculate the best combination
best_combination, max_volume = find_best_combination(boxes, budget)

# Output the results
if best_combination:
    print("Best combination of boxes:")
    for i, quantity in enumerate(best_combination):
        if quantity > 0:
            box_type = list(boxes.keys())[i]
            print(f'{quantity} x {box_type} Box (Volume: {boxes[box_type]['volume']}L)')
    print(f'Total Volume: {max_volume}L')
else:
    print("No combination found within the budget.")
