import doubly_linked_list
import lru_cache


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")

# Doubly Linked List - Append
print("Doubly Linked List - Append")
dlist = doubly_linked_list.DoublyLinkedList()
dlist.append("A")
assert_equal(dlist.first_node.data, "A")
assert_equal(dlist.last_node.data, "A")
dlist.append("B")
dlist.append("C")
assert_equal(dlist.first_node.data, "A")
assert_equal(dlist.last_node.data, "C")

# Doubly Linked List - pop head
print("Doubly Linked List - pop head")
popped_node = dlist.pop_head()
assert_equal(popped_node.data, "A")
assert_equal(dlist.first_node.data, "B")
assert_equal(dlist.last_node.data, "C")
assert_equal(dlist.first_node.previous_node, None)

# Doubly Linked List - pop tail
print("Doubly Linked List - pop tail")
popped_node = dlist.pop_tail()
assert_equal(popped_node.data, "C")
assert_equal(dlist.first_node.data, "B")
assert_equal(dlist.last_node.data, "B")
assert_equal(dlist.first_node.previous_node, None)
assert_equal(dlist.first_node.next_node, None)

# Doubly Linked List - insert head
print("Doubly Linked List - insert head")
popped_node = dlist.insert_head("A")
assert_equal(dlist.first_node.data, "A")
assert_equal(dlist.last_node.data, "B")

# Doubly Linked List - move to head
print("Doubly Linked List - move to head")
dlist = doubly_linked_list.DoublyLinkedList()
a = dlist.append("A")
b = dlist.append("B")
c = dlist.append("C")
dlist.move_to_head(b)
assert_equal(dlist.first_node, b)
assert_equal(dlist.first_node.previous_node, None)
assert_equal(dlist.first_node.next_node, a)
assert_equal(dlist.first_node.next_node.next_node, c)
assert_equal(dlist.first_node.next_node.next_node.next_node, None)
assert_equal(dlist.last_node, c)
assert_equal(dlist.last_node.previous_node, a)
assert_equal(dlist.last_node.previous_node.previous_node, b)
dlist.move_to_head(b)
assert_equal(dlist.first_node, b)
assert_equal(dlist.last_node, c)
dlist.move_to_head(c)
assert_equal(dlist.first_node, c)
assert_equal(dlist.last_node, a)

# Doubly Linked List - pop index
print("Doubly Linked List - pop index")
dlist = doubly_linked_list.DoublyLinkedList()
dlist.append("A")
dlist.append("B")
dlist.append("C")
dlist.append("D")
dlist.pop_index(1)
assert_equal(dlist.first_node.data, "A")
assert_equal(dlist.first_node.next_node.data, "C")
dlist.pop_index(0)
assert_equal(dlist.first_node.data, "C")
dlist.pop_index(1)
assert_equal(dlist.first_node.data, "C")
assert_equal(dlist.last_node.data, "C")

# LRU Cache
print("LRU Cache - filling the cache")
lru = lru_cache.LruCache()
lru.cache("a", 1)
assert_equal(lru.hash_table.get("a").price, 1)
lru.cache("b", 2)
assert_equal(lru.hash_table.get("a").price, 1)
assert_equal(lru.hash_table.get("b").price, 2)
lru.cache("c", 3)
lru.cache("d", 4)  # cache is now: d, c, b, a
assert_equal(lru.linked_list.first_node.product, "d")
assert_equal(lru.linked_list.first_node.next_node.product, "c")
assert_equal(lru.linked_list.last_node.previous_node.product, "b")
assert_equal(lru.linked_list.last_node.product, "a")

print("LRU Cache - freshen")
lru.freshen("a")   # cache is now: a, d, c, b
assert_equal(lru.linked_list.first_node.product, "a")
assert_equal(lru.linked_list.first_node.next_node.product, "d")
assert_equal(lru.linked_list.last_node.previous_node.product, "c")
assert_equal(lru.linked_list.last_node.product, "b")
assert_equal(lru.linked_list.first_node.previous_node, None)
assert_equal(lru.linked_list.last_node.next_node, None)

print("LRU Cache - caching into full cache")
lru.cache("e", 5)  # cache is now: e, a, d, c
assert_equal(lru.hash_table.get("b"), None)
assert_equal(lru.hash_table.get("e").price, 5)
assert_equal(lru.linked_list.first_node.product, "e")
assert_equal(lru.linked_list.first_node.next_node.product, "a")
assert_equal(lru.linked_list.last_node.previous_node.product, "d")
assert_equal(lru.linked_list.last_node.product, "c")
assert_equal(lru.linked_list.first_node.previous_node, None)
assert_equal(lru.linked_list.last_node.next_node, None)

# Price Requester
print("Price Requester")
req = lru_cache.PriceRequester()
assert_equal(req.request_price_for("a"), 1)
assert_equal(req.request_price_for("b"), 1)
assert_equal(req.request_price_for("c"), 1)
assert_equal(req.request_price_for("d"), 1)
assert_equal(req.request_price_for("a"), 1)
assert_equal(req.request_price_for("b"), 1)
assert_equal(req.request_price_for("c"), 1)
assert_equal(req.request_price_for("d"), 1)
assert_equal(req.request_price_for("e"), 1)
assert_equal(req.request_price_for("a"), 1)
