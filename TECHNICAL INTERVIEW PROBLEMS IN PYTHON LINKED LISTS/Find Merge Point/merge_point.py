from linked_list import LinkedList, Node, set_up_test_case

linked_list_1, linked_list_2 = set_up_test_case()
print(linked_list_1)
print(linked_list_2)

def merge_point(linked_list_a, linked_list_b):
  size_of_a = linked_list_a.size()
  size_of_b = linked_list_b.size()
  
  diff = abs(size_of_a - size_of_b)
    
  if size_of_a > size_of_b:
    bigger = linked_list_a.head
    smaller = linked_list_b.head
  else:
    bigger = linked_list_b.head
    smaller = linked_list_a.head
  
  for i in range(diff):
    bigger = bigger.next

  while bigger and smaller:
    if bigger == smaller:
      return bigger
    bigger = bigger.next
    smaller = smaller.next

  return None

test_result = merge_point(linked_list_1, linked_list_2)

print("Function should return merge point node holding 'q': {0}".format(test_result.val))
