import time
start_time = time.time()

def main(n):
    listA  = [0] * (n + 1)
    return Fibonacci(n,listA)

def Fibonacci(n,listA):
    if n<=2:
        return(1)
    else:

        if listA[n-2]==0:
            listA[n-2]=Fibonacci(n-2,listA)
        if listA[n-1]==0:
            listA[n-1]=Fibonacci(n-1,listA)
        return(listA[n-1]+listA[n-2])     
        



if __name__ == "__main__":
    n = int(input("n = "))
    print(main(n))
        

print("Elapsed Time : %s seconds" % (time.time()-start_time))

