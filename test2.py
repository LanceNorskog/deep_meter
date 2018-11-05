def sub_lists(list1): 
    # first loop  
    for i in range(len(list1) + 1): 
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
            # slice the subarray  
            sub = list1[i:j] 
            full = [list(sub)]
            x = sub_lists(list(list1[0:i]))
            print(x)
            y = sub_lists(list(list1[j:]))
            print(y)
            if len(full) > 0:
              if len(x) > 0:
                full = list(full.append([x]))
              if len(y) > 0:
                full = list(full.append([y]))
            else:
              full = []
              if len(x) > 0:
                full = list(x)
              if len(y) > 0:
                if len(full) > 0:
                  full = list(full.append([y]))
                else:
                  full = list(y)
             yield full
      

main = [1,1,1]

for x in

print(sub_lists([1,2,3]))
