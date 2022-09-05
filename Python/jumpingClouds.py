def jumpingClouds(n, k, c):
    energy = 100 #initial energy
    i = k % n #initial jump from 0
    energy -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    
    return energy

n = 10
k = 3
clouds = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
print(jumpingClouds(n, k, clouds))