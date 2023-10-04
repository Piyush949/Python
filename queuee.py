from queue import Queue

# Creating a queue
my_queue = Queue(maxsize=5)  # You can specify the maximum size or leave it blank for an infinite queue

# Enqueue elements
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Display the queue
print("Queue:", my_queue.queue)

# Dequeue elements
item = my_queue.get()
print("Dequeue:", item)

# Display the updated queue
print("Queue:", my_queue.queue)
