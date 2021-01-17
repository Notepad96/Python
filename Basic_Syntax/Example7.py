mySet = {1, 2, 2, 4, 4, 3}
mySet2 = {3, 4, 5, 6}


print("\n=================세 트================")
print(mySet)
mySet.add(5)
mySet.remove(1)
print(mySet)


print("\n=================합집합================")
print(mySet & mySet2)
print(mySet.intersection(mySet2))


print("\n=================교집합================")
print(mySet | mySet2)
print(mySet.union(mySet2))


print("\n=================차집합================")
print(mySet - mySet2)
print(mySet.difference(mySet2))


