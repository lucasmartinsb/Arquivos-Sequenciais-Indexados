from listNode import listNode

class treeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.quantity = 1
        self.list = None
        
    def insertTreeNode(self, data):
            if self.data:
                if data[1] < self.data[1]:
                    if self.left is None:
                        self.left = treeNode(data)
                    else:
                        self.left.insertTreeNode(data)
                elif data[1] > self.data[1]:
                    if self.right is None:
                        self.right = treeNode(data)
                    else:
                        self.right.insertTreeNode(data)
                elif data[1] == self.data[1]:
                    if(self.quantity == 1):
                        self.list = listNode(data)
                    else:
                        self.list.insertEnd(data)
                    self.quantity += 1
            else:
                self.data[1] = data[1]
                
                
                
    def findval(self, customer):
        if customer < self.data[1]:
            if self.left is None:
                return None
            return self.left.findval(customer)
        elif customer > self.data[1]:
            if self.right is None:
                return None
            return self.right.findval(customer)
        else:
            return self