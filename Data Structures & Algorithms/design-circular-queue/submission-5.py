class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.front = -1
        self.rear = -1
        self.arr = [0] * self.capacity

    def enQueue(self, value: int) -> bool:
        if self.front == -1:
            self.front, self.rear = 0, 0 
            self.arr[0] = value
            return True
        index = (self.rear + 1) % self.capacity
        if index == self.front:
            return False
        self.arr[index] = value
        self.rear = index
        return True
    def deQueue(self) -> bool:
        if self.front == -1:
            return False
        if self.front == self.rear:
            self.arr[self.front] = 0 
            self.front, self.rear = -1, -1
            return True
        self.arr[self.front] = 0
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.front != -1:
            return self.arr[self.front]
        return -1

    def Rear(self) -> int:
        if self.rear != -1:
            return self.arr[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return (self.front == -1)

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()