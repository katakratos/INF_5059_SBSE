from binary_search_with_sorted_list import binary_search

def linear_search(sorted_list,target_value):
    for index, value in enumerate(sorted_list):
        if value == target_value:
            return index
    return -1

if __name__ == "__main__":
    import time
    sorted_list = [i for i in range(1,1000001)]

    target_value = 999999

    start_time = time.time()
    linear_result = linear_search(sorted_list,target_value)
    end_time = time.time() 

    print(f" Linear search result : {linear_result}, start at : {start_time:.5f} seconds and end at : {end_time} seconds")   


    start_time = time.time()
    binary_result = binary_search(sorted_list,target_value)
    end_time = time.time() 

    print(f" Binary search result : {binary_result}, start at : {start_time:.5f} seconds and end at : {end_time} seconds")   