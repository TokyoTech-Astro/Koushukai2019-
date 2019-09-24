i = 2
tf = 0
PerfectNumberList = [2]
while len(PerfectNumberList) < 100:

    for j in range(len(PerfectNumberList)):
        if i % PerfectNumberList[j] == 0:
            tf += 1
    if tf == 0:
        PerfectNumberList.append(i)
    i += 1
    tf = 0

print(PerfectNumberList[99])