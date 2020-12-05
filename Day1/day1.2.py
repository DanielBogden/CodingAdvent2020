target = 2020


def find_three_entries():
    with open("input.txt", "r") as f:
        input_values = [int(x.strip("\n")) for x in f]
        input_values.sort()
    
    for i in range(0, len(input_values)):
        left = i + 1
        right = len(input_values) - 1
        
        while (left < right):
            if ((input_values[i] + input_values[left] + input_values[right]) == target):
                return input_values[i] * input_values[left] * input_values[right]
            elif ((input_values[i] + input_values[left] + input_values[right]) < target):
                left += 1
            else:
                right -= 1
    
    
if __name__ == "__main__":
    print("Day One Pt2: %d" % find_three_entries())
    