class Node:
    def __init__(self, value: str):
        # keep pointer to this nodes next node in the list
        self.next = None
        self.value = value

    def __str__(self) -> str:
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node: Node) -> Node:
        # if no head the list is empty, set head to node
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

        return node

    def insert_at(self, node: Node, insert_index: int) -> Node:
        if insert_index == 0:
            node.next = self.head
            self.head = node
            return node

        current = self.head
        index = 0

        # iterate to element BEFORE the index we want to insert at
        while current and index < insert_index - 1:
            current = current.next
            index += 1

        if current:
            # set current next to inserted nodes next to allow inserting between the two elements
            node.next = current.next
            current.next = node
            return node
        else:
            raise Exception("Insert index out of range")

    def remove_at(self, remove_index: int) -> Node:
        if remove_index == 0:
            deleted_elem = self.head
            self.head = self.head.next
            return deleted_elem

        current = self.head
        index = 0

        # iterate to element BEFORE the index we want to insert at
        while current and index < remove_index - 1:
            current = current.next
            index += 1

        if current:
            # skip the next element by setting the next pointer to the the deleted elements next
            deleted_elem = current.next
            current.next = current.next.next
            return deleted_elem
        else:
            raise Exception("Delete index out of range")

    def __str__(self) -> str:
        """Build list representation of our linked list nodes.

        Returns:
            str: mimics Python's list print for a linked list
        """
        node = self.head
        linked_list_str = ""
        while node:
            linked_list_str += f"{str(node)} "
            node = node.next
        return f"[{linked_list_str.strip()}]"


linked_list = LinkedList()
linked_list.append(Node("A"))
linked_list.append(Node("B"))
linked_list.append(Node("D"))

linked_list.insert_at(Node("C"), 2)
print(linked_list)
linked_list.remove_at(2)
print(linked_list)
