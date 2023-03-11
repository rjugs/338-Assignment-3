import sys

prev_capacity = sys.getsizeof([])

for i in range(64):
    lst = list(range(i))
    curr_capacity = sys.getsizeof(lst)
    
    if curr_capacity != prev_capacity:
        print(f"List capacity is changed at {i} elements: {prev_capacity} bytes -> {curr_capacity} bytes")
        prev_capacity = curr_capacity
