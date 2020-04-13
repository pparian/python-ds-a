class Empty(Exception):
    """
    Error attemptng to access an element from an empty container.
    """
    pass

class ArrayStack:
    """
    LIFO Stack implementation using a Python list as underlying storage.
    """
    def __init__(self):
        """
        Create an empty stack.
        """
        self._data = []

    def __len__(self):
        """
        Return the number of elements in the stack.
        """

    def is_empty(self):
        """
        Return True if the stack is empty.
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Add element e to the top of the stack.
        """
        self._data.append(e)

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

def reverse_file(filename):
        """
        Overwrite given file with its contents line-by-line reversed.
        """
        S = ArrayStack()
        original = open(filename)
        for line in original:
            S.push(line.rstrip("\n"))
        original.close()

        output = open(filename, "w")
        while not S.is_empty():
            output.write(S.pop() + "\n")
        output.close()

def is_matched(expr):
    """
    Return True if all delimiters are properly matched; False otherwise.
    """
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

def is_matched_html(raw):
    """
    Return True if all HTML tags are properly matched; False otherwise.
    """
    S = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find(">", j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith("/"):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k+1)
    return S.is_empty()

class ArrayQueue:
    """
    FIFO queue implementation using a Python list as underlying storage.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """
        Create an empty queue
        """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Return the number of elements in the queue.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the queue is empty.
        """
        return self._size == 0

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO)

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """
        Add an element to the back of queue.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """
        Resize to a new list of capacity >= len(self).
        """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

class ArrayDeque:
    """
    Double-ended queue implementation using a Python list as underlying storage.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """
        Create an empty deque
        """
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Return number of elements in the deque
        """
        return self._size

    def is_empty(self):
        """
        Return True if deque is empty
        """
        return self._size == 0

    def first(self):
        """
        Return (but not remove) the first element of deque D;
        an error occurs if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._front]

    def last(self):
        """
        Return (but not remove) the last element of deque D;
        an error occurs if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        """
        Add element e to the front of deque D.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        

    def add_last(self, e):
        """
        Add element e to the end of deque D.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self, e):
        """
        Remove and return the first element from deque D;
        an error occurs if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self, e):
        """
        Remove and return the last element from deque D;
        an error occurs if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def _resize(self, capacity):
        """
        Resize to a new list of capacity >= len(self) or capacity <= len(self).
        """
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

if __name__ == "__main__":
    print("Chapter 6")

    expr = "[(5+x)-(y+z)]"
    print(is_matched(expr))
    """
    Stack
    push(5) => [5]
    push(3) => [5,3]
    pop() => [5]; 3
    push(2) => [5,2]
    push(8) => [5,2,8]
    pop() => [5,2]; 8
    pop() => [5]; 2
    push(9) => [5,9]
    push(1) => [5,9,1]
    pop() => [5,9]; 1
    push(7) => [5,9,7]
    push(6) => [5,9,7,6]
    pop() => [5,9,7]; 6
    pop() => [5,9]; 7
    push(4) => [5,9,4]
    pop() => [5,9]; 4
    pop() => [5]; 9
    """