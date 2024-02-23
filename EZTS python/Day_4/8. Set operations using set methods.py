#set operations using methods like union(),intersection(),instersection_update(),difference(), difference_update,symmetric_difference,symmetric_difference_update,isdisjoint(),issubset(),isupperset()
a={1,2,3,4}
b={2,3,5,6}
print(a.union(b))
print(a|b)

a={1,2,3,4}
b={2,3,5,6}
print(a.intersection(b))
print(a&b)

a={1,2,3,4}
b={1,2,3,4,5}
print(a.intersection_update(b))
print(a)

a={1,2,3,4}
b={2,3,5,6}
print(a.difference(b))


a={1,2,3,4}
b={2,3,5,6}
print(a.difference_update(b))


a={1,2,3,4}
b={2,3,5,6}
print(a.symmetric_difference(b))


a={1,2,3,4}
b={2,3,5,6}
print(a.symmetric_difference_update(b))


a={1,2,3,4}
b={2,3,5,6}
print(a.isdisjoint(b))


a={1,2,3,4}
b={2,3,5,6}
print(a.issubset(b))


a={1,2,3,4}
b={2,3,5,6}
print(a.isupperset(b))

