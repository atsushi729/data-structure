def reverseList(head: []) -> list:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


head = [int(i) for i in input().split()]
print(reverseList(head))
