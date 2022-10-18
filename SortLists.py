def sortStockCode(memoryIndex):
    n = len(memoryIndex)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):

            # traverse the memoryIndexay from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if memoryIndex[j][1] > memoryIndex[j + 1][1]:
                swapped = True
                memoryIndex[j], memoryIndex[j + 1] = memoryIndex[j + 1], memoryIndex[j]
                print(memoryIndex[j][0])
            
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return memoryIndex 