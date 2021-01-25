from linked_list import LinkedList, Node, build_test_case

linked_list_a, linked_list_b = build_test_case()

def add_two(linked_list_a, linked_list_b):
  
  result = LinkedList()
  carry = 0
  
  a_node = linked_list_a.head
  b_node = linked_list_b.head
  
  while a_node or b_node:
    
    if b_node:
      b_val = b_node.val
      b_node = b_node.next
    else:
      b_val = 0
      
    if a_node:
      a_val = a_node.val
      a_node = a_node.next
    else:
      a_val = 0
      
    to_sum = a_val + b_val + carry
    
    if to_sum > 9:
      carry = 1
      to_sum %= 10
    else:
      carry = 0

    
    if not result.head:
      result.head = Node(to_sum)
      tmp = result.head
    else:
      tmp.next = Node(to_sum)
      tmp = tmp.next
      
  if carry:
    tmp.next = Node(carry)

  return result


print("Adding linked list:\n{0}\nto linked list\n{1}\n".format(linked_list_a, linked_list_b))
result = add_two(linked_list_a, linked_list_b)
print("Result should be: 9 -> 5 -> 1 ->\nFunction returned:\n{0}".format(result))
