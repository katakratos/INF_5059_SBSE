def knapsack(items, max_weight):
    n = len(items)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Build dp table
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(max_weight + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp

def get_selected_items(dp, items, max_weight):
    selected_items = []
    w = max_weight
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item `i-1` is included
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]  # Reduce weight capacity
    
    return selected_items

if __name__ == "__main__":
    # Example 1
    items = [(60, 10), (100, 20), (120, 30)]
    max_weight = 50
    dp_table = knapsack(items, max_weight)
    max_value = dp_table[len(items)][max_weight]
    selected_items = get_selected_items(dp_table, items, max_weight)
    
    print("Maximum Value:", max_value)
    print("Selected Items: (value, weight)", selected_items)
    
    # Example 2
    items = [(50, 5), (60, 10), (140, 20)]
    max_weight = 30
    dp_table = knapsack(items, max_weight)
    max_value = dp_table[len(items)][max_weight]
    selected_items = get_selected_items(dp_table, items, max_weight)
    
    print("Maximum Value:", max_value)
    print("Selected Items: (value, weight)", selected_items)
