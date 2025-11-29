class MyStack:
    def __init__(self):
        self.count = 0
        self.elements = []
        self.size = 4

    def is_empty(self):
        return self.count == 0

    def push(self, element):
        if len(self.elements) == self.size:
            raise TypeError("Stack overflow")

        self.elements.append(element)
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise TypeError("Stack is empty")
        self.count -= 1
        return self.elements[self.count]

    def peek(self):
        if self.is_empty():
            raise TypeError("Stack is empty")
        return self.elements[self.count - 1]
