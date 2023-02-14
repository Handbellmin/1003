n = int(input())

ls = []
for _ in range(n):
  ls.append(int(input()))

def dp(n):
  dp_1 = [0]*(n+3)
  dp_1[0],dp_1[1],dp_1[2] = 0,1,1
  dp_0 = [0]*(n+3)
  dp_0[0],dp_0[1],dp_0[2] = 1,0,1
  for i in range(2,n+1):
    dp_0[i] = dp_0[i-1]+dp_0[i-2]
    dp_1[i] = dp_1[i-1]+dp_1[i-2]

  print(dp_0[n], dp_1[n])
  
for l in ls:
  dp(l)

