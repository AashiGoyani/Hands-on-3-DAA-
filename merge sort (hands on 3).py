def merge_sort(list1):
    if len(list1)>1:
        middle_element = len(list1)//2
        left_sublist = list1[:middle_element]
        right_sublist = list1[middle_element:]
        
        merge_sort(left_sublist)
        merge_sort(right_sublist)
        i = j = k = 0
        
        while i<len(left_sublist) and j <len(right_sublist):
            if left_sublist[i]<right_sublist[j]:
                list1[k] = left_sublist[i]
                i+=1
                
            else:
                list1[k] = right_sublist[j]
                j+=1
            k+=1
        
        while i < len(left_sublist):
            list1[k] = left_sublist[i]
            i+=1
            k+=1
        
        while j < len(right_sublist):
            list1[k] = right_sublist[j]
            j+=1
            k+=1
            
list1 = [5,2,4,7,1,3,2,6]
merge_sort(list1)
print(list1)