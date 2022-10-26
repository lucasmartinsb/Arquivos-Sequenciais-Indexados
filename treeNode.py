class Node:
    def __init__(self, data):
        # left child
        self.left = None
        # right child
        self.right = None
        # node's value
        self.data = data

    # print function
    def PrintTree(self):
        print(self.data)
        
    def insertNode(self, data):
    # Compare the new value with the parent node
            if self.data:
                if data[2] < self.data[2]:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insertNode(data)
                elif data[2] > self.data[2]:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insertNode(data)
            else:
                self.data[2] = data[2]
                
    def findval(self, customer):
        if customer < self.data[2]:
            if self.left is None:
                return None
            return self.left.findval(customer)
        elif customer > self.data[2]:
            if self.right is None:
                return None
            return self.right.findval(customer)
        else:
            return self.data