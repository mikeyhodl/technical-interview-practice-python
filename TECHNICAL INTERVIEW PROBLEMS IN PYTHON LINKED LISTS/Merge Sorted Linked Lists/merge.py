from linked_list import LinkedList, Node

linked_list_a = LinkedList()
linked_list_b = LinkedList()
linked_list_a.add('z')
linked_list_a.add('x')
linked_list_a.add('c')
linked_list_a.add('a')
linked_list_b.add('u')
linked_list_b.add('g')
linked_list_b.add('b')


def merge(linked_list_a, linked_list_b):
  
  current_node_a = linked_list_a.head
  current_node_b = linked_list_b.head
  
  if current_node_a.val < current_node_b.val:
    start_node = current_node_a
    current_node_a = current_node_a.next
  else:
    start_node = current_node_b
    current_node_b = current_node_b.next

  head = start_node
  
  while current_node_a or current_node_b:
    if not current_node_a:
      start_node.next = current_node_b
      current_node_b = current_node_b.next
    elif not current_node_b:
      start_node.next = current_node_a
      current_node_a = current_node_a.next
    elif current_node_a.val < current_node_b.val:
      start_node.next = current_node_a
      current_node_a = current_node_a.next
    else:
      start_node.next = current_node_b
      current_node_b = current_node_b.next
    start_node = start_node.next
    
  return LinkedList(head)

merged_linked_list = merge(linked_list_a, linked_list_b)

print("Merged list should contain all nodes in sorted order:\na -> b -> c -> g -> u -> x -> z ->")
print("Your function returned:\n{0}".format(merged_linked_list))
