from markdown_it.rules_core.normalize import NULL_RE

from stack import MyStack


class MyQueue:
    def __init__(self):
       self.count = 0
       self.elements = []
       self.size = 5


    def is_empty(self):
        return self.count == 0

    def myOffer(self, element):
        if self.count <= 5:
            self.elements.append(element)
            self.count += 1
        return self.count <= 5

    def myAdd(self, element):
        if self.count == self.size:
            raise ValueError("Queue is full")
        self.elements.append(element)
        self.count += 1
        return self.count < self.size

    def myPoll(self):
        if self.is_empty():
            return None
        removed = self.elements.pop(0)
        self.count -= 1
        return removed

    def myRemove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        removed = self.elements.pop(0)
        self.count -= 1
        return removed

    def element(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.elements[0]

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[0]





