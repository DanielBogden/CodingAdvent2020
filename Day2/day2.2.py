import re

valid_passwords = 0

with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        
        first, second = re.search('^\d.*\d', line).group().split("-")
        
        target = re.search(" \S", line).group().strip()
        password = re.search("\: (.*)", line).group(1)
    
        if ((password[int(first) - 1] == target) != (password[int(second) - 1] == target)):
            valid_passwords += 1

    print(valid_passwords)
