def isMultipleOf3(n): 
  
    odd_count = 0
    even_count = 0
  
   
    
    if(n < 0):  
        n = -n 
    if(n == 0): 
        return 1
    if(n == 1):  
        return 0
  
    while(n): 
          
         
          
        if(n & 1):  
            odd_count += 1
  
         
          
        if(n & 2): 
            even_count += 1
        n = n >> 2
  
    return isMultipleOf3(abs(odd_count - even_count)) 
  
  
num = 3
if (isMultipleOf3(num)):  
    print( 'yes') 
else: 
    print( 'no') 
  
 
