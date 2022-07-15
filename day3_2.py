# https://adventofcode.com/2021/day/3
def oxygen_count(bigger_count):
    with open("day3_input.txt", "r") as f:
        oxygen_rate = []
        for line in f:
            if line[0] == str(bigger_count):
                oxygen_rate.append(line.strip())
        print(oxygen_rate)


with open("day3_input.txt", "r") as f:
    col0 = 0
    col1 = 0
    for line in f:
        if line[0] == "0":
            col0 += 1
        else:
            col1 += 1
    # print("col0: "+ str(col0) + "\ncol1: " + str(col1))
    if col1 > col0:
        oxygen_count(1)
    else:
        oxygen_count(1)

                
    