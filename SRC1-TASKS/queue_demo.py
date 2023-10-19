#initialise Queue variable

MAX_SIZE = 5
q1 = [0 for _ in range(MAX_SIZE)]
q1_size = 0
q1_fp = 0
q1_rp = -1


def isEmpty():
    global q1_size
    return q1_size == 0
#end function

def isFull():
    global MAX_SIZE
    global q1_size
    return MAX_SIZE == q1_size
#end function

def enqueue(item):
    if not isFull():
        q1_rp = (q1_rp + 1) % MAX_SIZE
        q1_size += 1
        q1[q1_rp] = item
    #end if
#end procedure

def dequeue():
    if not isEmpty():
        item_p = q1_fp
        q1_fp = (q1_fp + 1) % MAX_SIZE
        q1_size -= 1
        return q1[item_p]
    #end if
#end function
        
           