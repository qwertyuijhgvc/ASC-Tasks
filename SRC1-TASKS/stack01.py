class Stack:
    def __init__(self,size):
        self.maxSize = size
        self.data = ["" for _ in range(size)]
        self.sp = -1
    #end contructor
    def size(self):
        return self.sp + 1
    #end function
    def isFull(self):
        return self.size() == self.maxSize
    #end function
    def isEmpty(self):
        return self.sp == -1 
    #end function
    def push(self,item):
        if self.isFull():
            print("Stack is full")
        else:
            self.sp = self.sp + 1
            self.data[self.sp] = item
        #end if
    #end procedure
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.sp -= 1
            return self.data[self.sp + 1]
        #end if
    #end function
#end class
reverseString = ""
myString = input ("Please enter a word or phrase to be tested: ")
numChars = len(myString)
s = Stack(numChars)
for c in myString:
    s.push(c)
#next c
print(s.data)
while not s.isEmpty():
    reverseString += s.pop()
#end while
if reverseString == myString:
    print("Palindrome")
else:
    print("not palindrome")
#end if