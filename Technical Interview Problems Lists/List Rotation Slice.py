
# rotate list
# no time/space requirements
# return "rotated" version of input list

def rotate(l, k):
  for i in range(k):
    l.insert(0, l.pop())
  return l

def rotate_alternative(lst, degree):
  rotation = degree % len(lst)
  return lst[-rotation:] + lst[:-rotation]

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c', 'd']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['c', 'd', 'e', 'f', 'a', 'b']))
