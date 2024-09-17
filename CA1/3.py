
def is_ziba_index(item, index):
    return (item >= index  and item % index  == 0) or (item < index  and index  % item == 0)
    
def find_usable_items(prev_list, n):
    items=list(range(1,n+1))
    for i in prev_list:
        items.remove(i)
    return items
    
def is_ziba(prev_list, index):
    
    items = find_usable_items(prev_list, n)
    if index  == n:
        if is_ziba_index(items[0], index):
            return 1
        else:
            return 0
            
    count=0
    for item in items:
        if not is_ziba_index(item, index):
            continue

        count += is_ziba(prev_list+[item], index+1)
        
    return count



n = int(input())

prev_list=[]
count = is_ziba(prev_list,1)
print(count)