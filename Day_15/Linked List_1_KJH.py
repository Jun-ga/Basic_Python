    def insert(self,head,data): 
        node = Node(data)
        if not head:
            head = node
        else:
            current = head
            while(current.next):
                current = current.next
            current.next = node
        return head
