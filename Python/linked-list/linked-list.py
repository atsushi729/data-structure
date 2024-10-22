class Node:
    def __init__(self, data: None) -> None:
        self.data = data
        self.next_value = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data: None) -> None:
        new_node = Node(data)

        # If the linked list is empty, then make the new node the head.
        if self.head is None:
            self.head = new_node
            return

        # Traverse the linked list to the last node.
        last_node = self.head
        while last_node.next_value:
            last_node = last_node.next_value
        last_node.next_value = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_value


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.append("D")
    linked_list.append("E")
    print(linked_list.head)
    print(linked_list.head.next_value)
    print(linked_list.head.next_value.next_value)
    print(linked_list.head.next_value.next_value.next_value)
    print(linked_list.head.next_value.next_value.next_value.next_value)
    print(linked_list.head.next_value.next_value.next_value.next_value.next_value)
    linked_list.display()
