def mergeTwoLists(list1, list2):
    if (list1) and (list2):
        new_list = list1 + list2
    else:
        return []
    prev, curr = None, new_list

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
print(mergeTwoLists(list1, list2))
