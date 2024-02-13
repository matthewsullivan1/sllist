class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item  # int
            self.next = next_node  # IntNode

    def __init__(self):
        self.first = None  # initialize an empty list
        self.length = 0

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)
        self.length += 1

    '''
    insert at 3 -> 
    need to make new node, iterate to index - 1, return that node. previous.next to new, new.next to previous.next
    
    new node.next = returned.next
    returned.next = new node
    '''

    def _get_index_node(self, index):  # returns index
        temp = self.first
        for i in range(0, index - 1):
            temp = temp.next

        return temp

    def insert(self, entry, index):
        if index < 0:
            raise IndexError("Invalid input")
        elif index > self.length:
            index = self.length  # index greater than the size of the list just inserts at the back
        new = self.IntNode(entry, None)

        jumper = self.first
        for i in range(0, index - 1):
            jumper = jumper.next

        if jumper.next is None:
            jumper.next = new
            self.length += 1
            return
        else:
            temp = jumper.next
            jumper.next = new
            new.next = temp
            self.length += 1
            return

    def reverse(self):
        if self.length == 0:
            raise IndexError
        current = self.first
        previous = None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.first = previous

    def reverseRecursively(self, current, previous=None):
        if current.next is None:
            current.next = previous
            return current

        first = self.reverseRecursively(current.next, current)
        current.next = previous
        return first

    def replicate(self):
        '''
        replaces n with n copies of n
        3 2 1 -> 3 3 3 2 2 1

        1. make new list
        2. get first entry from old list
        3. for i < entry, insert node(entry) at back of list entry times
        4. get next entry
        '''

        newList = SLList()
        temp = self.first
        pos = 0

        while temp is not None:
            for i in range(temp.item):
                if newList.length == 0:
                    newList.addFirst(temp.item)
                    pos += 1
                else:
                    newList.insert(temp.item, pos)
                    pos += 1
            temp = temp.next
        return newList

    def equals(self, a):
        if self.length != a.length:
            #print("Not equal ", str(self.length), " != ", str(a.length))
            return False
        else:
            item1 = self.first
            item2 = a.first
            for i in range(self.length):
                #print("checking  ", str(item1.item), " == ", str(item2.item))
                if item1.item != item2.item:
                    #print("Not equal ", str(item1.item), " != ", str(item2.item))
                    return False
                item1 = item1.next
                item2 = item2.next
            #print("Lists are equal")
            return True


if __name__ == '__main__':

    L = SLList()
    L.addFirst(15)
    L.addFirst(10)
    L.addFirst(5)
    L.reverse()

    L_expect = SLList()
    L_expect.addFirst(5)
    L_expect.addFirst(10)
    L_expect.addFirst(15)

    if L.equals(L_expect):
        print("Two lists are equal, tests passed")
    else:
        print("Two lists are not equal, tests failed")
