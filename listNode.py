class listNode:
    def __init__(self, data):
      self.dataval = data
      self.nextval = None

    def insertEnd(self, data):
        newNode = listNode(data)
        last = self
        while(last.nextval):
            last = last.nextval
        last.nextval = newNode
        