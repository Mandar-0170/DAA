'''
A Dynamic Programming based Python program
for 0-1 Knapsack problem returns the maximum
value that can be put in a knapsack of capacity W

'''
def knapSack(W, wt, val):
  n = len(val)
  dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

  for i in range(n + 1):
    dp[i][0] = 0

  for j in range(W + 1):
      dp[0][j] = 0

  for i in range(1,n+1):
    for j in range(1,W+1):
      v = val[i - 1] # ith item val
      w = wt[i - 1] # ith item wt
      if w<=j:
        includedProfit = v + dp[i-1][j-w]
        excludedProfit = dp[i-1][j]
        dp[i][j] = max(includedProfit, excludedProfit)
      else:
        excludedProfit = dp[i-1][j]
        dp[i][j] = excludedProfit

  return dp[n][W]


# Driver code
val = [10, 20, 30]
wt = [100, 200, 300]
W = 250

print(f'Maximum value we can obtain = {knapSack(W, wt, val)}')
