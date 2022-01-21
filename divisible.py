def list_divisible_by_5 ( my_list ):
    count = 0
    for num in my_list:
        if num == 100:
           return 0
        if num % 5 ==0:
            count =count + 1
        else: 
            count = count + 0
    return count

print (list_divisible_by_5([5, 10, 15, 20, 23, 24, 56]))
print (list_divisible_by_5([50, 60, 70, 80, 100]))

   
        
        
    
