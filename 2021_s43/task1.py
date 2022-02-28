# (a)
class node:
    # data: integer(int)
    # nextNode: integer(int)

    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


# (c)
#   (i)
def outputNodes(arr, startpointer):
    currentNode = startpointer
    print(arr[currentNode].data, end=" -> ")
    while arr[currentNode].nextNode != -1:
        currentNode = arr[currentNode].nextNode
        print(arr[currentNode].data, end=" -> ")

# (d)
#   (i)
def addNode(arr, startpointer, endpointer):
    newData = None
    currentNode = startpointer
    while not newData:
        try:
            newData = int(input("\nNew node data: "))
        except Exception as e:
            return False, arr, endpointer
    while arr[currentNode].nextNode != -1:
        currentNode = arr[currentNode].nextNode
    
    arr[currentNode].nextNode = endpointer
    currentNode = arr[currentNode].nextNode
    arr[currentNode].data = newData

    endpointer = arr[currentNode].nextNode
    arr[currentNode].nextNode = -1

    return True, arr, endpointer



    
if __name__ == "__main__":
    # (b)
    linkedlist = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
    startpointer = 0
    endpointer = 5

    # (c)
    #   (ii)
    outputNodes(linkedlist, startpointer)

    # (d)
    #   (ii)
    valid, linkedlist, endpointer = addNode(linkedlist, startpointer, endpointer)
    if valid: 
        outputNodes(linkedlist, startpointer)
    else: 
        print("Error")