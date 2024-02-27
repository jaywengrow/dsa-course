class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

        if isinstance(data, dict):
            self.product = data.get("key")
            self.price = data.get("data")
