# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist2[0]
print(item)

item2 = mylist2[-2]     # secound last item
print(item2)

for i in mylist:
    print(i)

    if i in mylist:
        print("yes")
    else:
        print("No")

print(len(mylist))

mylist.append("lemon")
print(mylist)

# to insert an item at specific position
mylist.insert(1, "blueberry")  # adding to index 1 i.e adds an extra element
print(mylist)

# remove item
mylist.pop()    # if not specified removes the last item only
mylist2.remove("apple")
mylist2.clear() # to remove all elements
print(mylist2)

# to reverse the order
mylist3 = mylist.reverse()

# to sort list
mylist4 = [4, 5, -1, 0, 9, 3, -3, -2]
mylist4.sort()  # always puts in ascending order, replaces the original one
print("sorted list", mylist4)
# sorting but keeping the original list the same
mylist5 = sorted(mylist4)

# create a list with same elements repetitively
mylist6 = [0] * 5
print(mylist6)

# adding to lists
mylist7 = mylist5 + mylist6
print(mylist7)

# slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[2:5]  # index not included
print(a)
a = mylist[2:]  # until end
print(a)

a = mylist[::2]  # step 2
print(a)

a = mylist[::-1]  # trick to reverse the list
print(a)

list_org = ["banana", "cherry", "apple"]