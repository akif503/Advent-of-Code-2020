class Block:
    def __init__(self, num):
        self.num = int(num)
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.num)

    def __int__(self):
        return self.num

class Board:
    def __init__(self):
        # Generally the head will the left most element of the board
        self.head = None
        self.last = None
        self.size = 0
        
        self.reference = {}
    
    def __str__(self):
        cur = self.head
        nums = ""
        while True:
            nums += str(cur)
            cur = cur.right

            if cur == self.head:
                break
        
        return nums

    def __len__(self):
        return self.size

    def push(self, element):
        if not isinstance(element, Block):
            element = Block(element)

        if self.head is None:
            self.head = element

        if self.last is None:
            self.last = element
        
        element.right = self.head
        self.last.right = element

        self.last = element
        self.size += 1

        self.reference[int(element)] = element
    
    def append_after(self, target, value):
        new_element = Block(value)

        new_element.right = target.right
        target.right = new_element

        self.reference[value] = new_element

    def remove(self):
        # Only elements adjacent to head or tail can be removed
        # We will focus element right of the head for now
        rem_elem = self.head.right
        self.head.right= rem_elem.right

        self.reference.pop(int(rem_elem))

        return int(rem_elem)
    
    def find(self, value):
        return self.reference[value]
    
    def set_head(self, element):
        self.head = element