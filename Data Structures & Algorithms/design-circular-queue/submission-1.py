class MyCircularQueue:

    def __init__(self, k: int):
        self.positions = [0] * k 
        self.front, self.rear = -1, -1  
        self.k = k     

    def enQueue(self, value: int) -> bool:
        if self.front == -1:
            self.front, self.rear = 0, 0
            self.positions[self.front] = value
            return True
        index = (self.rear + 1) % self.k
        if index == self.front:
            return False
        self.positions[index] = value
        self.rear = index
        return True

    def deQueue(self) -> bool:
        if self.front == -1:
            return False
        self.positions[self.front] = 0
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.k
        return True
    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.positions[self.front]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        return self.positions[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.k == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()