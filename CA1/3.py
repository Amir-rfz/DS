import itertools
n=int(input())
all_permutation=list(itertools.permutations(range(1,n+1)))
def is_ziba(x,i):
    if(i==n+1):
        return True
    if(x[0]>i and x[0]%i!=0):
        return False
    if(x[0]<i and i%x[0]!=0):
        return False    
    if(is_ziba(x[1:len(x)],i+1)):
        return True
    return False

count=0
for array in all_permutation:
    if(is_ziba(array,1)):
        count+=1
        
print(count)

# print(is_ziba([3,1,2],1))