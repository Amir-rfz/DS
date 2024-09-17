n, m = input().split()
n = int(n)
m = int(m)
mountain = []
for i in range(n):
    mountain.append(input())
    mountain[i] = list(mountain[i])

r = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if(mountain[i][j]=='#'):
            r[i][j] = -1
        elif (j==0):
            r[i][j] = 0
        else:
            r[i][j] = r[i][j-1] + 1

l = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m-1, -1, -1):
        if(mountain[i][j]=='#'):
            l[i][j] = -1
        elif (j==m-1):
            l[i][j] = 0
        else:
            l[i][j] = l[i][j+1] + 1

d = [[0 for j in range(m)] for i in range(n)]
for j in range(m):
    for i in range(n):
        if(mountain[i][j]=='#'):
            d[i][j] = -1
        elif (i==0):
            d[i][j] = 0
        else:
            d[i][j] = d[i-1][j] + 1
            
u = [[0 for j in range(m)] for i in range(n)]
for j in range(m):
    for i in range(n-1, -1, -1):
        if(mountain[i][j]=='#'):
            u[i][j] = -1
        elif (i==n-1):
            u[i][j] = 0
        else:
            u[i][j] = u[i+1][j] + 1
            
                    
max_count=0
for i in range(n):
    for j in range(m):
        count = r[i][j] + l[i][j] + u[i][j] + d[i][j] + 1
        if count>max_count:
            max_count = count

print(max_count)

