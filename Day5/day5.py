lines_to_process = []

def get_data():
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip("\n")
            
            if not line:
                break
        
            lines_to_process.append(line)
            

upper = 127
lower = 0

def split_halves(upper, lower, letter, index):
    if letter == 'F' or letter == 'L':
        upper = upper/2
    elif letter == 'B' or letter == 'R':
        lower = upper/2
    
    if upper == lower:
        return upper    
    
    split_halves(upper, lower[index+1])
        
            
    pass
    

# F = Lower half (split in half) 0-63
# R = upper half (64-127)\
# 
# L = lower half

    
def get_row_num():
    pass