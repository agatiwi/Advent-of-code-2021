# https://adventofcode.com/2021/day/1

with open('day1_input.txt', 'r') as f:
    increasing = 0
    last = int(f.readline())
    for line in f:
        new = int(line)
        if(new > last):
            increasing+=1
        last = new
    print(increasing)
