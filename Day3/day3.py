import numpy

run_totals = []

# part 1 arguments
# slope = [[3, 1]]

# part 2 arguments
slope = [[1,1], [3,1], [5,1], [7,1], [1,2]]


def get_data():
    with open("input.txt", "r") as f:
        ski_slope = f.read().strip().split()
    return ski_slope


def Sonny_Bono(slope = []):
    right_move = 0
    down_move = 1
    ski_slope = get_data()
    down = slope[0][down_move]
    right = slope[0][right_move]
    num_trees = 0

    for _ in range (0, len(ski_slope) - 1, down):
        num_trees +=1 if ski_slope[down][right] == '#' else 0

        right += slope[0][right_move]
        down += slope[0][down_move]
        
        if (right >= len(ski_slope[0])):
            right = (right - (len(ski_slope[0])))

    return num_trees


# Don't hit these trees!
print(numpy.prod([Sonny_Bono([x]) for x in slope]))
