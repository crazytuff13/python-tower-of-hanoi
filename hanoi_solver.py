def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = [str(rods[0]) + ' [] []']

    def hanoi(num_disks, source, target, auxiliary):
        if num_disks == 0:
            return
        hanoi(num_disks - 1, source, auxiliary, target)
        disk = rods[source].pop()
        rods[target].append(disk)
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
        hanoi(num_disks - 1, auxiliary, target, source)

    hanoi(n, 0, 2, 1)
    return '\n'.join(moves)