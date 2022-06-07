# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(repr(temp))
            temp = temp.next
        return '[' + ', '.join(elements) + ']'

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data=data, prev=temp)

    def appendleft(self, data):
        temp = self.head
        temp.prev = Node(data=data, next=temp)
        self.head = temp.prev

    def pop(self):
        if not self.head:
            print('Doubly Linked List is empty')
            return
        temp = self.head
        ctr = 0
        while temp.next:
            temp = temp.next
            ctr += 1
        if not ctr:
            self.head = None
            return
        temp.prev.next = None
        temp = None

    def popleft(self):
        if not self.head:
            print('Doubly linked List is empty')
            return
        temp = self.head
        self.head = temp.next
        if not self.head:
            return
        self.head.prev = None
        temp = None

    def find(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        return temp

    def delete(self, key):
        if not self.head:
            print('Linked list is empty')
            return
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if not curr:
            print('Element not in the linked list')
            return
        if not curr.next:
            return self.pop()
        elif not curr.prev:
            return self.popleft()
        temp = curr.prev
        curr.prev.next = curr.next
        curr.next.prev = temp
        curr = None

    # Reversing the doubly linked list
    def reverse(self):
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        if prev_node:
            self.head = prev_node.prev


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(23)
    dll.append('First Date')
    dll.append('Sm Rosales')
    dll.append('Shakeys')
    dll.append(3.14)
    dll.appendleft('With Engineer')
    print(dll)
    dll.pop()
    print(dll)
    dll.popleft()
    print(dll)
    print(dll.find('W'))
    print(dll.find('Sm Rosales'))
    dll.delete(23)
    dll.delete('Shakeys')
    print(dll)
    dll.reverse()
    print(dll)