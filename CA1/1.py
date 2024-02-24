def is_misagi(string):
    num_of_repeat=0
    for i in range(len(string)):
        if(i!=len(string)-1):
            if(string[i]==string[i+1]):
                num_of_repeat+=1
    if(num_of_repeat<2):
        return True
    else: 
        return False
    
input_string=input()
lenghs=[]

for i in range(len(input_string)):
    for j in range(i,len(input_string)):
        if(is_misagi(input_string[i:j+1])):
            lenghs.append(j-i+1)
            
print(max(lenghs))