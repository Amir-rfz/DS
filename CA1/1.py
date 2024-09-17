def misagi_index(string):
    indexes=[]
    indexes.append(0)
    for i in range(len(string)):
        if(i!=len(string)-1):
            if(string[i]==string[i+1]):
                indexes.append(i+1)
    indexes.append(len(string))

    return indexes

input_string=input()

# print(misagi_index(input_string))

index=misagi_index(input_string)
max_len=0
for i in range(len(index)):
    if(i<=len(index)-3):
        if(index[i+2]-index[i]>max_len):
            max_len=index[i+2]-index[i]
            
if(len(index)==2 or len(index)==3):
    print(len(input_string))
else:
    print(max_len)