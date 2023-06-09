class Node:
    def __init__(self, data: None) -> None:
        self.data = data
        self.next_value = None


class LinkedList:
    def __init__(self) -> None:
        self.haed_value = None


list1 = LinkedList()
list1.haed_value = Node("mon")
element2 = Node("tue")
element3 = Node("wed")
list1.haed_value.next_value = element2
element2.next_value = element3
