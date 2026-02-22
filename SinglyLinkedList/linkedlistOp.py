class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if (self.head !=None):
            temp1 = self.head
            while (temp1.next!=None):
                temp1 = temp1.next
            temp1.next = temp
        else:
            self.head = temp

    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    
    def insertAtPos(self,value,pos):
        temp=Node(value)
        temp1=self.head

        while(temp1.next!=None) :
            if(temp1.data==pos):
                temp.next=temp1.next
                temp1.next=temp

            temp1=temp1.next

    def deleteLL(self,value):
        temp1=self.head
        prev=temp1
        if(temp1.data==value):
            self.head==temp1.next
        while(temp1.next!=None):
            if(temp1.data==value):
                prev.next=temp1.next
                break
            else:
                prev=temp1
                temp1=temp1.next

    def printLL(self):
     temp1 = self.head
     while ( temp1 != None):
        print(temp1.data, end=" ")
        temp1 = temp1.next
    
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(5)
obj.deleteLL(20)
obj.insertAtPos(20,10)
obj.printLL()
