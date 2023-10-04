class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.capacity
            print()


# Example usage:
if __name__ == "__main__":
    capacity = 5
    cq = CircularQueue(capacity)

    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)

    cq.display()

    print("Dequeue:", cq.dequeue())
    print("Dequeue:", cq.dequeue())

    cq.display()

    cq.enqueue(6)
    cq.display()
