import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        if ((self.tail + 1) % self.size) == self.head:
            return False
        else:
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data
            return True

    
    def dequeue(self):
        
        #Lock the queue
        self.lock()

        #Check if the queue is empty
        while self.head == -1:
            print("Queue is empty. Consumer is waiting...")
            # Unlock the queue and wait one second
            self.unlock()
            time.sleep(1)
            # Lock the queue again
            self.lock()

        #Remove the element from the head of the queue
        num = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size

        #Unlock the queue and return the element that has been removed
        self.unlock()
        return num


def producer(queue):
    while True:
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)
        
        # Wait for the number of seconds equal to the random number
        time.sleep(num)
        
        # Enqueue the number to the queue
        queue.lock()
        while ((queue.tail + 1) % queue.size) == queue.head:
            print("Queue is full. Producer is waiting...")
            queue.unlock()
            time.sleep(1)
            queue.lock()
        queue.enqueue(num)
        queue.unlock()



def consumer(queue):
    while True:
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)

        # Wait for the number of seconds equal to the random number
        time.sleep(num)

        # Dequeue a number from the queue and print it
        queue.lock()
        if queue.head == -1:
            print("Queue is empty. Consumer is waiting...")
            queue.unlock()
            time.sleep(1)
        else:
            num = queue.queue[queue.head]
            if queue.head == queue.tail:
                queue.head = queue.tail = -1
            else:
                queue.head = (queue.head + 1) % queue.size
            print(f"Consumer dequeued {num} from the queue")
            queue.unlock()


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer, args=(q, ))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()