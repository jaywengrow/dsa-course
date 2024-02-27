class Heap:
    def __init__(self):
        self.data = []

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def not_empty(self):
        return len(self.data) > 0

    def insert(self, value):
        self.data.append(value)
        new_node_index = len(self.data) - 1

        while (new_node_index > 0 and 
               (self.data[new_node_index] 
                < self.data[self.parent_index(new_node_index)])):

            parent_index = self.parent_index(new_node_index)
            self.data[parent_index], self.data[new_node_index] = \
                self.data[new_node_index], self.data[parent_index]

            new_node_index = parent_index

    def pop(self):
        if len(self.data) == 1:
            value_to_delete = self.data[0]
            self.data = []
            return value_to_delete

        value_to_delete = self.root_node()
        self.data[0] = self.data.pop()
        trickle_node_index = 0

        while self.has_smaller_child(trickle_node_index):
            smaller_child_index = self.find_smaller_child_index(trickle_node_index)

            self.data[trickle_node_index], self.data[smaller_child_index] = \
                self.data[smaller_child_index], self.data[trickle_node_index]

            trickle_node_index = smaller_child_index

        return value_to_delete
    
    def has_smaller_child(self, index):
        return ((self.left_child_index(index) < len(self.data) and
                self.data[self.left_child_index(index)] < self.data[index])
                or
                (self.right_child_index(index) < len(self.data) and
                self.data[self.right_child_index(index)] < self.data[index]))

    def find_smaller_child_index(self, index):
        if self.right_child_index(index) >= len(self.data):
            return self.left_child_index(index)

        if (self.data[self.right_child_index(index)]
                < self.data[self.left_child_index(index)]):
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)
