    def insert(self,head,data): 
        node = Node(data)
        if head == None:
            head = node  
        else:
            current = head
            while(current.next != None):
                current = current.next
            current.next = node 
        return head 
            
    #Complete this method
    
