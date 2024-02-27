import doubly_linked_list
import time


class LruCache:

    def __init__(self):
        self.hash_table = {}
        self.linked_list = doubly_linked_list.DoublyLinkedList()
        self.max_size = 4

    def read(self, key):
        if key in self.hash_table:  # Cache hit
            return self.freshen(key)
        else:                       # Cache miss
            return None
            
    def freshen(self, key):
        node = self.hash_table.get(key)
        self.linked_list.move_to_head(node)
        return node

    def cache(self, key, data):
        # If cache is full:
        if len(self.hash_table) >= self.max_size:
            self.evict()
             
        # Save new data in both linked list and hash table:
        new_node = self.linked_list.insert_head({"key": key, "data": data})
        self.hash_table[key] = new_node

    def evict(self):
        # LRU eviction policy:
        evicted_node = self.linked_list.pop_tail()
        del self.hash_table[evicted_node.data["key"]]

class PriceRequester:

    def __init__(self):
        self.cache = LruCache()

    def request_price_for(self, product):
        data = self.cache.read(product)
        if data:  # Cache hit
            price = data.price
        else:     # Cache miss
            price = self.search_web_for(product)
            self.cache.cache(product, price)
        
        return price

    def search_web_for(self, product):
        # Mock data:
        price = 1
        # Mimic time it takes to search web:
        time.sleep(0.25)

        return price
