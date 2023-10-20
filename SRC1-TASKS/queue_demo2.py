class Queue_data:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [0 for _ in range(self.max_size)]
        self.size = 0
        self.fp = 0
        self.rp = -1
    def __repr__(self) -> str:
        return_str = ""
        ptr = self.fp
        while ptr != self.rp:
            return_str += str(self.data[ptr])
            ptr = (ptr + 1) % self.max_size
        #end while
        return return_str
    #end functioj=n
    #end construction
#end record

new_q1 = Queue_data(5)
new_q2 = Queue_data(7)


def isEmpty(q):
    return q.size == 0
#end function

def isFull(q):
    return q.max_size == q.size
#end function

def enqueue(item, q):
    if not isFull(q):
        q.rp = (q.rp + 1) % q.max_size
        q.size += 1
        q.data[q.rp] = item
    else:
        print("queue is full")
    #end if
#end function

def dequeue(q):
    if not isEmpty:
        item_p = q.fp
        q.fp = (q.fp + 1) % q.max_size
        q.size -= 1
        return q.data[item_p]
    else:
        print("queue is empty")
    #end if
#end 

for num in range(11,16):
    enqueue(num, new_q1)
#next num
for num in range(101,106):
    enqueue(num, new_q2)
#next num
print(new_q1.data)
enqueue(16, new_q1)
print(new_q1.data)
for _ in range(6):
    print(dequeue(new_q1))
#next _
print(new_q1.data)
enqueue(20, new_q1)
print(new_q1.data)