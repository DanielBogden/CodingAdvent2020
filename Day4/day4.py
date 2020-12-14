import re

check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def get_data():
    with open("input.txt") as f:
        data = f.read().split("\n\n")
    return data


def verify(data):
    is_valid = 0

    check_this = data
    
    print("CHECKING: ", check_this)
    
    hcl = re.search('(?<=hcl:)[^ \n]*', check_this).group()
    if re.search('^#[a-f0-9]{6}$', hcl):
        is_valid +=1 
    
    byr = re.search('(?<=byr:)[^ \n]*', check_this).group()
    if byr:
        b_year = re.search('[0-9]{4}', byr).group()
        if int(b_year) >= 1920 and int(b_year) <=2002:
            is_valid +=1 
            print("byr is valid")
    
    iyr = re.search('(?<=iyr:)[^ \n]*', check_this).group()
    if iyr:
        issue_year = re.search('[0-9]{4}', iyr).group()
        if int(issue_year) >= 2010 and int(issue_year) <=2020:
            is_valid +=1 
            print("iyr is valid")
            
    eyr = re.search('(?<=eyr:)[^ \n]*', check_this).group()
    if eyr:
        exp_year = re.search('[0-9]{4}', eyr).group()
        if int(exp_year) >= 2020 and int(exp_year) <=2030:
            is_valid +=1
            print("eyr is valid")
    
    hgt = re.search('(?<=hgt:)[^ \n]*', check_this).group()
    if "cm" in hgt or "in" in hgt:
        measuring_system = re.search('[^0-9].*', hgt).group()
        height = int(re.search('[\d]*', hgt).group())

        if measuring_system == "cm":
            if height >= 150 and height <= 190:
                is_valid += 1
                print("hgt is valid")
        elif measuring_system == "in":
            if height >= 59 and height <= 76:
                is_valid += 1
                print("hgt is valid")
    
    
    ecl = re.search('(?<=ecl:)[^ \n]*', check_this).group()
    if ecl in eye_colors:
        is_valid += 1
        print("ecl is valid")
        
    pid = re.search('(?<=pid:)[^ \n]*', check_this).group()
    pid_digits = re.search('[0-9]{9}', pid)
    if pid_digits:
        if len(pid_digits.group()) == 9:
            is_valid +=1
            print("pid is valid")
    
    print(is_valid)
    return is_valid


# byr = four digits; min(1920) max(2002)
# iyr = four digits; min(2010) max(2020)
# eyr = four digits; min(2020) max(2030)
# hgt = a number folowed by cm or in
    # if cm min(150), max(193)
    # if in min(59), max(76)
#hcl = a # followed by exactly 6 characters [0-9 | a-f]
#ecl = exactly one of: amb, blu, brn, gry, gyn, hzl, oth
#pid = nine digits, including leading zeros
#cid = ignored


# First time around
def check_passport_validity(index, passport):
    if index == len(check):
        return 0
    
    if check[index] in passport:
        return 1 + check_passport_validity(index+1, passport)
    
    if check[index] not in passport:
        return 0
    
    
def can_i_see_your_passport_plz():
    valid_passports = 0
    data = get_data()
    
    for x in data:
        if check_passport_validity(0, x) == len(check):
            if verify(x) == len(check):
                valid_passports += 1
            #run other check

    return valid_passports


# Recursion for the win!
# print(can_i_see_your_passport_plz())

print(can_i_see_your_passport_plz())
# verify()