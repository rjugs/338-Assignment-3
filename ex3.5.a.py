# Consider the following tasks. For each task, provide the code for an inefficient 
# implementation and an efficient implementation. State the worst-case complexity 
# of each. Then, provide the code for an experiment that demonstrates the difference. 
# The experiment should: 
# (i) time the execution of both implementations on realistic, 
#     large inputs (1000 elements or above); (ii) plot the distribution of measured values 
#     across multiple measurements (>= 100 measurements per task)
# (iii) print an aggregate of the measured values (min or average as appropriate).

# Search in a sorted array

import random
import timeit
import matplotlib.pyplot as plt

# inefficient implementation
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# efficient implementation
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# generate a list of 1000 random integers
test_list = [random.randint(0, 10000) for i in range(1000)]

# time the execution of inefficient function
inefficient_times = []
for i in range(100):
    x = random.choice(test_list)
    linear_search_time = timeit.timeit(lambda: linear_search(test_list, x), number=1000)
    inefficient_times.append(linear_search_time)

# time the execution of efficient function
efficient_times = []
for i in range(100):
    test_list.sort()
    x = random.choice(test_list)
    binary_search_time = timeit.timeit(lambda: binary_search(test_list, x), number=1000)
    efficient_times.append(binary_search_time)

# plot the distribution of measured values
plt.hist(inefficient_times, bins=20, alpha=0.5, label='Inefficient')
plt.hist(efficient_times, bins=20, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.title('Execution Time Distribution')
plt.xlabel('Time (s)')
plt.ylabel('Frequency')
plt.show()

# print the minimum and average measured values for each function
print('Linear Search:')
print('Min Time: {:.6f} s'.format(min(inefficient_times)))
print('Avg Time: {:.6f} s'.format(sum(inefficient_times) / len(inefficient_times)))
print('\nBinary Search:')
print('Min Time: {:.6f} s'.format(min(efficient_times)))
print('Avg Time: {:.6f} s'.format(sum(efficient_times) / len(efficient_times)))
