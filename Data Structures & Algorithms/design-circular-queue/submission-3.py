class MyCircularQueue:

    def __init__(self, k: int):
        self.values = [0] * k
        self.front, self.rear = -1, -1 # -1 used to denote empty
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.values[self.front] = value
            return True
        index = (self.rear + 1) % self.k
        if index == self.front:
            return False
        self.values[index] = value
        self.rear = index
        return True

    def deQueue(self) -> bool:
        if self.front == -1:
            return False
        if self.front == self.rear: 
            self.values[self.front] = 0
            self.front, self.rear = -1, -1
            return True
        self.values[self.front] = 0
        self.front = (self.front + 1) % self.k
        return True
    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.values[self.front]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        return self.values[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        if self.front == -1:
            return False
        if (self.rear + 1) % self.k == self.front: 
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()