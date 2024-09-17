ducksPlacement = input()
numOfCheck = int(input())
checkSubStr = []
for _ in range(numOfCheck):
    checkStr = input()
    checkTerm = checkStr.split()
    checkSubStr.append([int(checkTerm[0])-1 , int(checkTerm[1])-1])


def isValid(subStr ,ducksPlacement):
    stack = []
    for i in range(subStr[0] , subStr[1] + 1):
        if(len(stack) == 0):
            if(ducksPlacement[i].islower()):
                return False
            else:
                stack.append(ducksPlacement[i])
                continue
        stackTop = stack.pop()
        if(stackTop.lower() == ducksPlacement[i]):
            continue
        else:
            stack.append(stackTop)
            stack.append(ducksPlacement[i])
    
    return len(stack) == 0

    
for subStr in checkSubStr:
    if(isValid(subStr ,ducksPlacement)):
        print("1",end="")
    else:
        print("0", end="")