def move_disk(pegs,disk,source,destination):
        pegs[destination].append(pegs[source].pop())


def move_tower(pegs,disk,source,destination):

##ここを埋めてください

def hanoi(n):
    pegs = [[] for i in range(3)]
    pegs[0] = list(reversed(range(n)))
    print(pegs)
    move_tower(pegs,n-1,0,1)
    print(pegs)


if __name__ == "__main__":
    n = int(input("n = "))
    hanoi(n)