class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)

    def read(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None
