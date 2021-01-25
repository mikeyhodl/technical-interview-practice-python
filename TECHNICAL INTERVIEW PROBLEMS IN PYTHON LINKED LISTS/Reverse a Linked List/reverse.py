from linked_list import LinkedList, Node

test_linked_list = LinkedList()

test_linked_list.add('d')
test_linked_list.add('c')
test_linked_list.add('b')
test_linked_list.add('a')


def reverse(linked_list):
    prev = None
    current_node = linked_list.head
    while current_node:
      tmp = current_node.next
      current_node.next = prev
      prev = current_node
      current_node = tmp
    return LinkedList(prev)


print("Pre-reverse: {0}".format(test_linked_list))

reversed_linked_list = reverse(test_linked_list)

print("Post-reverse: {0}".format(reversed_linked_list))
