def solve(N,A):
        #code here
       mxscore = - 1e18
       for k in range(1,N+1):
           score=0
           for i in range(k-1,N,k):
               score+=A[i]
           if(score > mxscore):
               mxscore = score
               ans = k
       return ans

n = 5
a = [1, 222, 3, 14, -5]
print(solve(n,a))