# https://adventofcode.com/2021/day/2
with open("day3_input.txt","r") as f:
    gamma = 0   # most
    epsilon = 0 # lest
    
    col0_0 = 0
    col0_1 = 0
    col1_0 = 0
    col1_1 = 0
    col2_0 = 0
    col2_1 = 0
    col3_0 = 0
    col3_1 = 0
    col4_0 = 0
    col4_1 = 0
    col5_0 = 0
    col5_1 = 0
    col6_0 = 0
    col6_1 = 0
    col7_0 = 0
    col7_1 = 0
    col8_0 = 0
    col8_1 = 0
    col9_0 = 0
    col9_1 = 0
    col10_0 = 0
    col10_1 = 0
    col11_0 = 0
    col11_1 = 0
    col12_0 = 0
    col12_1 = 0
    
    for line in f:
        if line[0] == "0":
            col0_0 += 1
        else:
            col0_1 += 1
        
        if line[1] == "0":
            col1_0 += 1
        else:
            col1_1 += 1
            
        if line[2] == "0":
            col2_0 += 1
        else:
            col2_1 += 1
            
        if line[3] == "0":
            col3_0 += 1
        else:
            col3_1 += 1
            
        if line[4] == "0":
            col4_0 += 1
        else:
            col4_1 += 1
            
        if line[5] == "0":
            col5_0 += 1
        else:
            col5_1 += 1
            
        if line[6] == "0":
            col6_0 += 1
        else:
            col6_1 += 1
            
        if line[7] == "0":
            col7_0 += 1
        else:
            col7_1 += 1
            
        if line[8] == "0":
            col8_0 += 1
        else:
            col8_1 += 1
            
        if line[9] == "0":
            col9_0 += 1
        else:
            col9_1 += 1
            
        if line[10] == "0":
            col10_0 += 1
        else:
            col10_1 += 1
            
        if line[11] == "0":
            col11_0 += 1
        else:
            col11_1 += 1
            
            
    if col0_0 > col0_1:
        gamma_fin = str(0)
        epsilon_fin = str(1)
    else:
        gamma_fin = str(1)
        epsilon_fin = str(0)
    if col1_0 > col1_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col2_0 > col2_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col3_0 > col3_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col4_0 > col4_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col5_0 > col5_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col6_0 > col6_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col7_0 > col7_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col8_0 > col8_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col9_0 > col9_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col10_0 > col10_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
    if col11_0 > col11_1:
        gamma_fin = gamma_fin+str(0)
        epsilon_fin = epsilon_fin+str(1)
    else:
        gamma_fin = gamma_fin+str(1)
        epsilon_fin = epsilon_fin+str(0)
            

gamma_fin = int(gamma_fin,2)
epsilon_fin = int(epsilon_fin,2)
print("gamma: " + str(gamma_fin))
print("epsilon: " + str(epsilon_fin))
print("power " + str(gamma_fin*epsilon_fin))
