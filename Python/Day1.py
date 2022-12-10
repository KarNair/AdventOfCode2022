with open('/home/karthik/AdventOfCode2022/Data/Day1a_input.txt', 'r') as ElfCalData:
    elves = ElfCalData.readlines()
    calories = [food.strip() for food in elves]


CalPerElf = []
cal_sum = 0



for elves in calories:
    if elves != "":
        cal_sum += int(elves)
    
    elif elves == "":
        CalPerElf.append(cal_sum)
        cal_sum = 0
CalPerElf.append(cal_sum)


print(max(CalPerElf))

#Part Two
SortedCal = sorted(CalPerElf, reverse=True)
print(sum(SortedCal[0:3]))
