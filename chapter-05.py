import ctypes
class DynamicArray:
    """
    A dynamic array class akin to a simplified Python list.
    """

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """
        Return number of elements stored in the array.
        """
        return self._n

    def __getitem__(self, k):
        """
        Return element at index k.
        """
        if not k < self._n:
            raise IndexError("invalid index")
        return self._A[k % self._n]
    
    def append(self, obj):
        """
        Add object to end of the array.
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity, self._n)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """
        Insert value at index k, shifting subsequen values rightward.
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity, k)
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def _resize(self, c, j):
        """
        Resize internal array to capacity c.
        Item to be inserted at position j. Shift relevant values rightward if required.
        """
        """
        self._n = 7, j = 5
        B[0] = A[0], B[1] = A[1], ... , B[4] = A[4]
        B[6] = A[5], B[7] = A[6], B[8] = A[7]

        self._n = 3, j = 3
        B[0] = A[0], B[1] = A[1], ..., B[3] = A[3]
        """
        B = self._make_array(c)
        for k in range(j):
            B[k] = self._A[k]
        
        if j < self._n:
            for k in range(j, self._n+1):
                B[k+1] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """
        Return new array with capacity c.
        """
        return (c * ctypes.py_object)()

    def __str__(self):
        """
        Return a string representation of the Dynamic Array
        """
        return str(self._A)

class GameEntry:
    """
    Represents one entry of a list of high scores.
    """

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score
    
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class Scoreboard:
    """
    Fixed-length sequence of high scores in nondecreasing order.
    """

    def __init__(self, capacity=10):
        """
        Initialize scoreboard with given maximum capacity.
        All entries are initially None.
        """
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """
        Return entry at index k.
        """
        return self._board[k]
    
    def __str__(self):
        """
        Return string representation of the high score list.
        """
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """
        Consider adding entry to high scores.
        """
        # must include exception handling for non-GameEntry inputs

        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board [-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            
            #shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

def insertion_sort(A):
    """
    Sort list of comparable elements into nondecreasing order.
    """
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

class CaesarCipher:
    """
    Class for doing encryption and decruption using a Caesar cipher.
    """

    def __init__(self, shift):
        """
        Construct Caesar cipher using given integer shift for rotation.

        To allow for other alphabet-based languages:
         - include language parameter (ie. def __init__(self, shift, language)
         - have if statement to define modulo and starting unicode position based on language
        """
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message):
        """
        Return string representing encrypted message.
        """
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """
        Return decrypted message given encrypted secret.
        """
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        """
        Utilisty to perform transformation based on given code string.
        """
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return "".join(msg)

class TicTacToe:
    """
    Management of a Tic-Tac-Toe game(does not do strategy).
    """

    def __init__(self):
        """
        Start a new game.
        """
        self._board = [[" "] * 3 for j in range(3)]
        self._player = "X"

    def mark(self, i, j):
        """
        Put an X or O mark at position(i,j) for next player's turn.
        """
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self._board[i][j] != " ":
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self._board[i][j] = self._player
        if self._player == "X":
            self._player = "O"
        else:
            self._player = "X"

    def _is_win(self, mark):
        """
        Check whether the board configuration is a win for the given player.
        """
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or 
                mark == board[1][0] == board[1][1] == board[1][2] or 
                mark == board[2][0] == board[2][1] == board[2][2] or 
                mark == board[0][0] == board[1][0] == board[2][0] or 
                mark == board[0][1] == board[1][1] == board[2][1] or 
                mark == board[0][2] == board[1][2] == board[2][2] or 
                mark == board[0][0] == board[1][1] == board[2][2] or 
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        """
        Return mark of winner player, or None to indicate a tie.
        """
        for mark in "XO":
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        """
        Return string representation of current game board.
        """
        rows = ["|".join(self._board[r]) for r in range(3)]
        return "\n-----\n".join(rows)

def repeatedIntegers(A):
    """
    Assume that list only contains 1 repeated integer
    Returns a list of integers that are repeated in array A.

    A.append(value) => O(1)
    value in storedList => O(k+1)

    A.sort() => O(nlogn)
    A[i] == A[i-1] => O(n)

    """
    if not isinstance(A, list):
        raise TypeError("input must be of type list")

    ######
    # OPTION 2
    # Returns first repeated integer
    # works if list only contains 1 repeated integer
    ######

    # total time
    # O(nlogn) + O(n) => O(n)

    # sort time 
    # O(nlogn)
    A.sort()

    # for loop time (inclusive of loop body)
    # O(n)
    for i in range(1,len(A)):
        if not isinstance(A[i], int):
            raise TypeError("element must be of type int")
        if A[i] == A[i-1]:
            return A[1]

    ######
    # OPTION 1
    # Returns list of repeated integers
    # works if list contains multiple repeated integers
    ######

    # # total run time of loop (inclusive of loop body)
    # # O(n^2)

    # distinctValues = []
    # repeatedValues = []

    # # run time of loop (not inclusive of loop body)
    # # O(n)
    # for i in range(len(A)):
    #     if not isinstance(A[i], int):
    #         raise TypeError("element must be of type int")

    #     # total per loop
    #     # (2*O(n) + O(1)) + (O(n) + O(1)) => 3*O(n) + O(1)

    #     # store if element has already occured and has not been flagged
    #     # O(k+1) + O(k+1) => 2*O(n) + O(1)
    #     if (A[i] in distinctValues) and (not A[i] in repeatedValues):
    #         repeatedValues.append(A[i])

    #     # store element if not yet occured
    #     # O(k+1) + O(k+1) => O(n) + O(1)
    #     if A[i] not in distinctValues:
    #         distinctValues.append(A[i])

    # return repeatedValues
        

if __name__ == "__main__":
    print("Chapter 5")

    nonRepeatedList = [i for i in range(10)]
    print(repeatedIntegers(nonRepeatedList))
    repeatedList = [1,1,1,2,3,4,4]
    print(repeatedIntegers(repeatedList))

    # test_list = DynamicArray()
    # test_list.append("a")
    # test_list.append("b")
    # test_list.append("c")
    # print("Length: ", len(test_list))
    # print("test_list[-1] = {0}".format(test_list[-1]))
    # print("test_list[2] = {0}".format(test_list[2]))
    # test_list.insert(1,"d")
    # for i in range(len(test_list)):
    #     print("test_list[{0}] = {1}".format(i,test_list[i]))
    


    # print("Caesar Cipher")
    # cipher = CaesarCipher(3)
    # message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    # coded = cipher.encrypt(message)
    # print("Secret: ", coded)
    # answer = cipher.decrypt(coded)
    # print("Message: ", answer)

    # print("Tic-Tac-Toe")
    # game = TicTacToe()
    # game.mark(1,1); game.mark(0,2)
    # game.mark(2,2); game.mark(0,0)
    # game.mark(0,1); game.mark(2,1)
    # game.mark(1,2); game.mark(1,0)
    # game.mark(2,0)

    # print(game)
    # winner = game.winner()
    # if winner is None:
    #     print("Tie")
    # else:
    #     print(winner, "wins")

    # import sys
    # data = []
    # n = 30
    # for k in range(n):
    #     len_pre = len(data)
    #     size_pre = sys.getsizeof(data)
        
    #     data.append(None)
    #     size_post = sys.getsizeof(data)

    #     if size_post != size_pre:
    #         print("Append - length: {0:3d}; Size in bytes: {1:4d}".format(len_pre, size_pre))
    
    # for j in range(n):
    #     len_pre = len(data)
    #     size_pre = sys.getsizeof(data)
        
    #     data.pop()
    #     size_post = sys.getsizeof(data)

    #     if size_post != size_pre:
    #         print("Pop - length: {0:3d}; Size in bytes: {1:4d}".format(len_pre, size_pre))

            
            