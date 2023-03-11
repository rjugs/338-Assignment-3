import json
import time
import matplotlib.pyplot as plt

# load the array and tasks from their respective json files
with open('ex2data.json', 'r') as f:
    array = json.load(f)
with open('ex2tasks.json', 'r') as f:
    tasks = json.load(f)

def binary_search(arr, x, first_midpoint):
    """
    Searches for the index of the element x in a sorted array arr.
    Assumes that arr is already sorted in ascending order.
    Returns the index of x in arr if it is present, else -1.
    The first midpoint for the search can be set using the first_midpoint parameter.
    """
    start = 0
    end = len(arr) - 1
    mid = first_midpoint

    while start <= end:
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2

    return -1

def time_binary_search(arr, task):
    """
    Times the performance of binary_search function with a few optimal initial midpoints.
    Returns the best initial midpoint for the given task.
    """
    midpoints = [0, (len(arr)//2) - (len(arr)//4), len(arr)//2, (len(arr)//2) + (len(arr)//4), len(arr) - 1]  # Check the beginning, middle and end of the array
    best_midpoint = None
    best_time = float('inf')
    for i in midpoints:
        start_time = time.time()
        binary_search(arr, task, i)
        end_time = time.time()
        duration = end_time - start_time

        if duration < best_time:
            best_midpoint = i
            best_time = duration

    return best_midpoint


# find the best midpoint for each task
best_midpoints = [time_binary_search(array, task) for task in tasks]

# plot each element of task against its respective optimized midpoint
plt.scatter(tasks, best_midpoints)
plt.title("Search tasks vs Their Ideal Midpoint Using a Binary Search Algorithm")
plt.xlabel('Search task')
plt.ylabel('Best initial midpoint')
plt.show()
