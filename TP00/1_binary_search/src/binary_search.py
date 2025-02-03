def binary_search(tab, target_value):
    left = 0
    right = len(tab) - 1

    while left <= right:
        middle = (left + right) // 2 
        
        if tab[middle] == target_value:
            return middle  
        elif target_value < tab[middle]:
            right = middle - 1  
        else:
            left = middle + 1  
    
    return -1  

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    test_values = [7, 19, 1, 20]
    for value in test_values:
        result = binary_search(sorted_list, value)
        if result !=1:
            print(f"The target value {value} is at index {result}.")
        else:
            print(f"The target value {value} is not in the list.")    
