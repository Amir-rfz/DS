input1=input()
input2=input()
flag=False
for i in range(len(input1)):
    for j in range(len(input2)):
        if(input1[i]==input2[j]):
            if((i%2)==(j%2)):
                flag=True
    if(flag==False):
        break
    flag=False
    
if(flag):
    print('yes')
else:
    print('no')