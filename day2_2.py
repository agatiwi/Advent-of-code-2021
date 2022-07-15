# https://adventofcode.com/2021/day/2#part2
with open("day2_input.txt","r") as f:
    horizontal = 0
    depth = 0
    aim = 0
    
    for line in f:
        word = line.split(' ')
        if word[0] == "forward":
            horizontal = horizontal + int(word[1])
            depth = depth + (aim * int(word[1]))
        elif word[0] == "up":
            aim = aim - int(word[1])
        elif word[0] == "down":
            aim = aim + int(word[1])
            
print("Horizontal: " + str(horizontal))
print("Depth: " + str(depth))
print("multi " + str(horizontal*depth))
