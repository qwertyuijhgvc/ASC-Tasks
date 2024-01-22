fib_dict = {}
import time
def fib_Recursive(n):
    if n <= 1:
        return n
    else:
        return fib_Recursive(n-1) + fib_Recursive(n-2)
    #end if
#end function
def fib_Iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    #next i
    return a
#end function
def fib_Rec_Dyn(n):
    if n <= 1:
        return n
    elif n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fib_Rec_Dyn(n-1) + fib_Rec_Dyn(n-2)
        return fib_Rec_Dyn(n-1) + fib_Rec_Dyn(n-2)
    #end if
#end function 
startTime1 = time.process_time()
print(fib_Recursive(10))
endTime1 = time.process_time()
print(endTime1)
startTime1 = time.process_time()
print(fib_Iterative(10))
endTime1 = time.process_time()
print(endTime1)
print(fib_Rec_Dyn(20))
print(fib_dict)
