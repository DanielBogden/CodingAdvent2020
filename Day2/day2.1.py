import re

valid_passwords = 0

with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        
        min, max = re.search('^\d.*\d', line).group().split("-")
        target = re.search(" \S", line).group().strip()
        password = re.search("\: (.*)", line).group(1)
        
        if (password.count(target) >= int(min) and password.count(target) <= int(max)):
            valid_passwords += 1

    print(valid_passwords)
            