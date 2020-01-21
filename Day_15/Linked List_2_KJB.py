def insert(self,head,data): 
        #Complete this method
        newNode = Node(data)
        if head is None:
            return newNode
        node = head
        while node.next is not None:
            node = node.next
        node.next = newNode
        return head
