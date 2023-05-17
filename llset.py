class LLSet:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.num_items = 0

    def insert(self, item):
        trav = self.head
        while trav is not None:
            if item == trav.val:
                return False
            trav = trav.next
        new_node = LLSet.Node(item, self.head)
        self.head = new_node
        self.num_items += 1
        return True

    def contains(self, item):
        trav = self.head
        while trav is not None:
            if item == trav.val:
                return True
            trav = trav.next
        return False

    def delete(self, item):
        prev = None
        trav = self.head

        while trav is not None:
            if item == trav.val:
                if prev is not None:
                    prev.next = trav.next
                else:
                    self.head = trav.next
                return True
            prev = trav
            trav = trav.next

        return False

    def size(self):
        return self.num_items

    def to_list(self):
        lst = []
        trav = self.head
        while trav is not None:
            lst.append(trav.val)
            trav = trav.next
        return lst
