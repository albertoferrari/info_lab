'''
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 torre di Hanoi
'''

def print_towers(towers: list):
    for t in towers:
        print('|-', end='')
        for d in t:
            print(d, end='')
        print()
    print()


def move_towers(towers: list, n: int, src: int, tmp: int, dst: int):
    # if there are discs above, move n-1 away
    if n > 1:
        move_towers(towers, n - 1, src, dst, tmp);

    # now move the largest disc (of n) to its dest
    top_disc = towers[src].pop()
    towers[dst].append(top_disc)
    print_towers(towers)

    # if there were discs above, move those on top
    if n > 1:
        move_towers(towers, n - 1, tmp, src, dst)


def main():
    discs = int(input('Discs? '))
    POLES = 3
    towers = [[] for p in range(POLES)]
    for d in reversed(range(discs)):
        towers[0].append(d + 1)
    print_towers(towers)

    # move all discs from pole 0 to pole 2
    move_towers(towers, discs, 0, 1, 2)

if __name__ == '__main__':
    main()




