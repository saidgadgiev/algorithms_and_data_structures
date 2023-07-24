class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):  # добавление элемента в конец списка
        new_node = Node(data)
        if not self.head:  # если список пустой
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:  # идем до конца списка
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node

    def reverse(self):  # разворот списка
        global temp
        curr_node = self.head
        while curr_node:
            temp = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = temp
            curr_node = curr_node.prev  # переходим к следующему узлу
        if temp:  # обновление головы списка
            self.head = temp.prev

    def display(self):  # вывод списка
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


# Пример использования:
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

print("Исходный список:")
dllist.display()

print("Список после разворота:")
dllist.reverse()
dllist.display()
