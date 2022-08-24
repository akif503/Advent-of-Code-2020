from classes import Block, Board

def main():
    inp = "364289715"
    #inp = "389125467"

    nums, mx, mn = find_range(inp)

    # Create the board
    board = Board()
    for num in inp:
        board.push(num)

    # Run simulation
    for t in range(100):
        #print(f"Move {t + 1}:", board)
        cur = board.head

        take = []
        for _ in range(3):
            take.append(board.remove())

        dest = find_dest(int(cur), take, nums, mx, mn)
        dest = board.find(dest)

        for i in range(-1, -4, -1):
            board.append_after(dest, take[i])

        board.set_head(cur.right)
    
    print_result(board)

def find_range(inp):
    nums = list(map(int, inp))
    mx = max(nums)
    mn = min(nums)

    return nums, mx, mn


def find_dest(cur, take, nums, mx, mn):
    d = cur - 1
    while d in take or d not in nums:
        if d < mn:
            d = mx

        else:
            d = d - 1
        
    return d


def print_result(board):
    f = board.find(1)
    board.set_head(f)

    print(str(board)[1:])

main()