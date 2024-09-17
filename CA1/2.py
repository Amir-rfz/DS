input1 = list(input())
input2 = list(input())
flag = False
for i in range(len(input1)):
    for j in range(len(input2)):
        if (input1[i] == input2[j]):
            if ((i % 2) == (j % 2)):
                flag = True
                input2[j]='#'
                break
    if not flag:
        break
    if(i==len(input1)-1):
        break
    flag = False

if flag:
    print('yes')
else:
    print('no')
