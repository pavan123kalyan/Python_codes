# You have:

# N books (numbered 1 to N)
# N shelves (positions 1 to N)
# A list of book pairs P
# Distance between two books: ∣shelf_position(book1)−shelf_position(book2)∣

# Your task:
# 👉 Arrange books on shelves
# 👉 So that total distance of all given pairs is minimum

from itertools import permutations
def min_distance_bruteforce(N, P):
    books = list(range(1, N+1))
    min_sum = float('inf')
    for perm in permutations(books):
        # Build position map
        position = {}
        for i in range(N):
            position[perm[i]] = i
        total = 0
        for a, b in P:
            total += abs(position[a] - position[b])
        min_sum = min(min_sum, total)
    return min_sum
print(min_distance_bruteforce(5, [[1,2],[1,3],[3,4]])) # Output:3
