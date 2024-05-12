import threading
import time
import queue

# Define a queue to hold the items
queue_size = 5
q = queue.Queue(queue_size)

# Define a function for the producer
def producer():
    for i in range(10):
        item = f"Item {i}"
        q.put(item)
        print(f"Produced {item}")
        time.sleep(1)

# Define a function for the consumer
def consumer():
    while True:
        item = q.get()
        print(f"Consumed {item}")
        time.sleep(2)

# Create two threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start both threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()
