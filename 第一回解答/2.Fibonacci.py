FibonacciNumberList = [1,1]
for i in range(2,50):
    FibonacciNumberList.append(FibonacciNumberList[i-1]+FibonacciNumberList[i-2])
print(FibonacciNumberList[-1])
