def sub_lists(list1, length): 
  
    # store all the sublists  
    sublist = [[]] 
      
    # first loop  
    for i in range(len(list1) + 1): 
          
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
              
            # slice the subarray  
            sub = list1[i:j] 
            if len(sub) == length:
              sublist.append(sub) 
              
      
    return sublist 

main = [1,1,1]

print(sub_lists([1,1,1]))
