n,m=input().split()
n=int(n)
m=int(m)
mountain=[]
for i in range(n):
    mountain.append(input())
    mountain[i]=[*mountain[i]]
    
max_col=0
max_row=0
max_count_row=0
for i in range(n):
    count=0
    for j in range(m):
        if(mountain[i][j]=='.'):
            count+=1
        else:
            if(count>max_count_row):
                max_row=i
                max_count_row=count
            count=0
    if(count>max_count_row):
        max_row=i
        max_count_row=count


max_count_col=0
for i in range(m):
    count=0
    for j in range(n):
        if(mountain[j][i]=='.'):
            count+=1
        else: 
            if(count>max_count_col):
                max_col=i
                max_count_col=count
            count=0
            
    if(count>max_count_col):
        max_col=i
        max_count_col=count

print(max_count_col+max_count_row-1)