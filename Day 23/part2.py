from classes import Block, Board

def main():
    inp = "364289715"
    #inp = "389125467"

    nums = list(map(int, inp))
    mx = max(nums)

    d = {}
    for _ in range(int(1e6 - len(nums))):
        d[mx + 1] = True
        nums.append(mx + 1)
        mx += 1
    
    mn, mx = 1, int(1e6)

    # Create the board
    board = Board()
    for num in nums:
        board.push(num)

    # Run simulation
    iterations = int(1e7)
    for t in range(iterations):
        if t % (int(1e6)) == 0:
            print(f"Move {t + 1}")

        cur = board.head

        take = {}
        taken = []
        for _ in range(3):
            removed = board.remove()
            take[removed] = True
            taken.append(removed)

        dest = find_dest(int(cur), take, nums, mx, mn)
        dest = board.find(dest)

        for value in reversed(taken):
            board.append_after(dest, value)

        board.set_head(cur.right)
    
    print(result(board))


def find_dest(cur, take, nums, mx, mn):
    time = 0
    d = cur
    while True:
        d = d - 1
        if d < mn:
            d = mx
        
        if not take.get(d, False):
            return d
        
        
def result(board):
    f = board.find(1)
    a, b = f.right, f.right.right

    return int(a) * int(b)


main()