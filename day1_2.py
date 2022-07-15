# https://adventofcode.com/2021/day/1

with open("day1_input.txt","r") as f:
    increasing = 0

    first = int(f.readline())
    second = int(f.readline())
    third = int(f.readline())

    sum_1 = first + second + third

    for line in f:
        first = second 
        second = third 
        third = int(line)
        
        sum_2 = first + second + third
        
        if sum_1 < sum_2:
            increasing+=1
        
        help = sum_2
        sum_2 = sum_1
        sum_1 = help
        
    print(increasing)
