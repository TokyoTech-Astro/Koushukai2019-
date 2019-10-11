def move_disk(pegs,disk,source,destination):
        pegs[destination].append(pegs[source].pop())
        print(disk, source,destination)


def move_tower(pegs,disk,source,destination):
    spare = 3 - source - destination
    if disk == 0:
        move_disk(pegs,disk,source,destination)
    else:
        move_tower(pegs,disk-1,source,spare)
        move_disk(pegs,disk,source,destination)
        move_tower(pegs,disk-1,spare,destination)

def hanoi(n):
    pegs = [[] for i in range(3)]
    pegs[0] = list(reversed(range(n)))
    print(pegs)
    move_tower(pegs,n-1,0,1)
    print(pegs)


if __name__ == "__main__":
    n = int(input("n = "))
    hanoi(n)