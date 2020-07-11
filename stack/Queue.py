class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def enQueue(self,data):
        while(len(self.s1)!=0):
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(data)
        
        while(len(self.s2)!=0):
            self.s1.append(self.s2[-1])
            self.s2.pop()
            
    def deQueue(self):
        
        if len(self.s1)==0:
            print("Q is empty")
        data = self.s1.pop()
        return data
    
    def printQueue(self):
        print(self.s1)
if __name__ == '__main__':
    q=Queue()
    
    q.enQueue(1)
    q.printQueue()

    q.enQueue(2)
    q.printQueue()

    q.enQueue(3)
    q.printQueue()

    print(q.deQueue())
    q.printQueue()
    q.enQueue(4)
    q.printQueue()
    print(q.deQueue())
    q.printQueue()
        
    

    
