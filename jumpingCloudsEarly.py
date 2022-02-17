def jumpingClouds(c=[0,0,1,0,1,0,1,0]):
    cJ = 0
    i = 0
    while i < len(c) - 2:
        if c[i+2] == 1:
            i +=1
        else:
            i += 2
        cJ +=1

    if i == len(c) - 2:
        cJ += 1
    
    return cJ

print(jumpingClouds())