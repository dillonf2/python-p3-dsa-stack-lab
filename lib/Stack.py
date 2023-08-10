class Stack:
    
    def __init__(self, items = [], limit= 100):
        self.stack = []
        self.limit=limit
        self.items=items if items is not None else []
        for item in items:
            if len(self.stack) < self.limit:
                self.stack.append(item)

    def isEmpty(self):
        return len(self.stack)==0

    def push(self, item):
        if len(self.stack) < self.limit:
            self.stack.append(item)
        else:
            return None

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
    
    def size(self):
        return len(self.stack)

    def full(self):
        return len(self.stack) == self.limit

    def search(self, target):
        return self.stack.index(target)
