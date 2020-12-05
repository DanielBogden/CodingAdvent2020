target = 2020


def find_two_entries():
    with open("input.txt", "r") as f:
        input_values = [int(x.strip("\n")) for x in f]    
        target_value = [x for x in input_values if ((target - x) in input_values)]

    return target_value[0] * target_value[1]


if __name__ == "__main__":
    print(find_two_entries())
    