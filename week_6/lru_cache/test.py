import doubly_linked_list



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
