# 1. Get the number of cities and the number of investment updates
line1 = input().split()
number_of_cities = int(line1[0])
total_updates = int(line1[1])

# 2. Create a list to track changes (Difference Array)
# We use size + 2 to handle 1-based indexing easily
investment_diff = [0] * (number_of_cities + 2)

# 3. Process each update one by one
for i in range(total_updates):
    update_line = input().split()
    start_city = int(update_line[0])
    end_city = int(update_line[1])
    amount = int(update_line[2])
    
    # Mark the start of the increase
    investment_diff[start_city] += amount
    # Mark where the increase stops (one city after the end)
    if end_city + 1 <= number_of_cities:
        investment_diff[end_city + 1] -= amount

# 4. Calculate the running total and find the maximum
max_investment_found = 0
running_total = 0
for i in range(1, number_of_cities + 1):
    running_total += investment_diff[i]
    # Update the high score if we find a larger value
    if running_total > max_investment_found:
        max_investment_found = running_total
# 5. Print the final answer
print(max_investment_found)