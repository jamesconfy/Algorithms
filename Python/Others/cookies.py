def cookies(k, A):
    # Write your code here
    A.sort(reverse=True)
    count = 0
    while True:
        print(A)
        f = A.pop()
        if f >= k:
            return count

        if len(A) == 0:
            return -1

        s = A.pop()
        n = s*2 + f*1
        A.append(n)
        count += 1
        A.sort(reverse=True)
    #print(A)
    #return count if A[0] > k else -1


A = [2, 7, 3, 6, 4, 6]
k = 9
print(cookies(k, A))

# import heapq

# def cookies(k, A):
#     heapq.heapify(A)
    
#     ops = 0
#     while True:
#         f = heapq.heappop(A)
                
#         if f >= k:
#             return ops
        
#         if len(A) == 0:
#             return -1
        
#         s = heapq.heappop(A)
#         n = f + 2*s
#         heapq.heappush(A, n)
        
#         ops += 1