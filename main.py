
# data - данные, которые хранятся в узле списка
# next - ссылка на следующий узел списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# head - ссылка на первый узел списка
class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        current = self.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


# Создаем связный список
linked_list = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
linked_list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

# Выводим исходный список
current_node = linked_list.head
print("Изначальный список: ")
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next

# Разворачиваем список
linked_list.reverse()

# Выводим развернутый список
current_node = linked_list.head
print("Разворот списка: ")
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
