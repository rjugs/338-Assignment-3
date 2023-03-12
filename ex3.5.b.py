# Consider the following tasks. For each task, provide the code for an inefficient 
# implementation and an efficient implementation. State the worst-case complexity 
# of each. Then, provide the code for an experiment that demonstrates the difference. 
# The experiment should: 
# (i) time the execution of both implementations on realistic, 
#     large inputs (1000 elements or above); (ii) plot the distribution of measured values 
#     across multiple measurements (>= 100 measurements per task)
# (iii) print an aggregate of the measured values (min or average as appropriate).

# Insertion in and extraction from priority queue

import time
import random
import matplotlib.pyplot as plt
import heapq

class InefficientPriorityQueue:
    # inefficient implementation
    def __init__(self):
        self.queue = []

    def insert_item(self, item):
        self.queue.append(item)
        self.queue.sort(reverse=True)

    def extract_max(self):
        if not self.queue:
            return None
        return self.queue.pop(0)


class EfficientPriorityQueue:
    # efficient implementation
    
    def __init__(self):
        self.queue = []

    def insert_item(self, item):
        heapq.heappush(self.queue, -item)

    def extract_max(self):
        if not self.queue:
            return None
        return -heapq.heappop(self.queue)


# create a list of 1000 random integers
data = [random.randint(1, 10000) for _ in range(1000)]

# time the inefficient implementation
inefficient_times = []
for i in range(100):
    pq = InefficientPriorityQueue()
    start_time = time.time()
    for item in data:
        pq.insert_item(item)
    for _ in range(len(data)):
        pq.extract_max()
    end_time = time.time()
    inefficient_times.append(end_time - start_time)

# time the efficient implementation
efficient_times = []
for i in range(100):
    pq = EfficientPriorityQueue()
    start_time = time.time()
    for item in data:
        pq.insert_item(item)
    for _ in range(len(data)):
        pq.extract_max()
    end_time = time.time()
    efficient_times.append(end_time - start_time)

# print aggregate stats
print("Inefficient implementation:")
print(f"Average time: {sum(inefficient_times) / len(inefficient_times)}")
print(f"Minimum time: {min(inefficient_times)}")
print("\nEfficient implementation:")
print(f"Average time: {sum(efficient_times) / len(efficient_times)}")
print(f"Minimum time: {min(efficient_times)}")

# plot histogram of measured values
plt.hist([inefficient_times, efficient_times], bins=10, label=["Inefficient", "Efficient"])
plt.xlabel("Execution Time (s)")
plt.ylabel("Frequency")
plt.title("Distribution of Execution Times")
plt.legend()
plt.show()
