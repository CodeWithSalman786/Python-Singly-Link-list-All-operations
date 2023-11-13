# CREATING NODE CLASS.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# CREATING LINKED LIST CLASS.
class LinkedList:
    def __init__(self):
        self.head = None
    # ADDING DATA AT THE START USING PREPEND FUNCTION.
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ADDING DATA AT THE END USING APPEND FUNCTION.
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    # DISPLAYING NODES LIST.
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    # INSERTING NODE AT SPECIFIC POSITION.
    def insert_At_Position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node
    # UPDATING NODE VALUE.
    def update(self, old, new):
        current = self.head
        while current:
            if current.data == old:
                current.data = new
                return
            current = current.next
    # SEARCHING FOR A VALUE.
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Value Found")
                return
            else:
                print("No Found")
                current = current.next
    # DELETING DATA.
    def delete(self, data):
       if self.head is None:
           return
       if self.head.data == data:
           self.head = self.head.next
           return
       current = self.head
       while current.next:
           if current.next.data == data:
               current.next = current.next.next
               return
           current = current.next

# MAIN CODE OR DRIVER CODE.
LinkedList = LinkedList()
while True:
    print("1 = Add Node at the End")
    print("2 = Add Node at the Start")
    print("3 = Display Nodes")
    print("4 = Insert Node at Position")
    print("5 = Update Node Value")
    print("6 = Search Node Value")
    print("7 = Delete Node")
    print("8 = Exit")
    # NOW LET'S ASK FOR USER SELECTION.
    selection = int(input("Make any One Selection from Above: "))
    # INSERTING NODE AT THE END.
    if selection == 1:
        data = int(input("Enter the Number: "))
        LinkedList.append(data)
        LinkedList.display()
    # INSERTING NODE AT THE START.
    elif selection == 2:
        data = int(input("Enter the Number: "))
        LinkedList.prepend(data)
        LinkedList.display()
    # DISPLAY NODES LIST.
    elif selection == 3:
        LinkedList.display()
    # INSERTING NODE AT SPECIFIC POSITION.
    elif selection == 4:
        data = int(input("Enter the Number: "))
        position = int(input("Enter the Position"))
        LinkedList.insert_At_Position(data, position - 1)
        LinkedList.display()
    # UPDATING DATA.
    elif selection == 5:
        LinkedList.display()
        old = int(input("Enter the Old Value: "))
        new = int(input("Enter the New Value: "))
        LinkedList.update(old, new)
    # SEARCHING DATA.
    elif selection == 6:
        LinkedList.display()
        value = int(input("Enter the Value to Search: "))
        LinkedList.search(value)
    # SEARCHING DATA.
    elif selection == 7:
        LinkedList.display()
        data = int(input("Enter the Value to Search: "))
        LinkedList.delete(data)
    # EXIT.
    elif selection == 8:
        exit()