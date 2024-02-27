#START:P1
import double_ended_node


class DoublyLinkedList:

    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def append(self, data):
        new_node = double_ended_node.Node(data)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
        
        return new_node
    
    def insert_head(self, data):
        new_node = double_ended_node.Node(data)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.next_node = self.first_node
            self.first_node.previous_node = new_node
            self.first_node = new_node

        return new_node

    def pop_head(self):
        popped_node = self.first_node
        self.first_node = self.first_node.next_node
        self.first_node.previous_node = None
        return popped_node
    
    def pop_tail(self):
        popped_node = self.last_node
        self.last_node = self.last_node.previous_node
        self.last_node.next_node = None
        return popped_node
    
    def move_to_head(self, node):
        if node == self.first_node:
            return
        
        if node.next_node:
            node.previous_node.next_node = node.next_node
            node.next_node.previous_node = node.previous_node
        else:  # node is the tail
            node.previous_node.next_node = None
            self.last_node = node.previous_node
        
        node.next_node = self.first_node
        node.next_node.previous_node = node
        node.previous_node = None
        self.first_node = node
    #END:P1
    #START:P2
    def pop_index(self, index):
        if index == 0:
            return self.pop_head()

        current_node = self.first_node
        for i in range(index):
            current_node = current_node.next_node

        if current_node == self.last_node:
            return self.pop_tail()
        
        current_node.previous_node.next_node = current_node.next_node
        current_node.next_node.previous_node = current_node.previous_node

        return current_node
    #END:P2
