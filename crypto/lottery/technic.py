from math import comb

def generate_combinations_with_switch(n, k, t):
    # combinations_list = list(combinations(range(1, n + 1), k))
    selected_combinations = []

    current_combination = list(range(1, k + 1))
    selected_combinations.append(tuple(current_combination))

    while len(selected_combinations) < t:
        # Find the rightmost element that can be incremented
        i = k - 1
        while i >= 0 and current_combination[i] == n - k + i + 1:
            i -= 1

        if i >= 0:
            current_combination[i] += 1

            # Switch a different number with the one at index i
            new_num = current_combination[i]
            while new_num == current_combination[i]:
                new_num = random.randint(1, n)

            current_combination[i] = new_num

            selected_combinations.append(tuple(current_combination))
        else:
            break

    return selected_combinations

# Example usage
import random

n = 18  # Number of elements in each set
k = 6   # Number of elements to choose in each combination
t = 7   # Total number of combinations (tickets) needed

combinations = generate_combinations_with_switch(n, k, t)

# Print or use the combinations as needed
for combo in combinations:
    print(combo)