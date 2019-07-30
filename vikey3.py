import math
def isPerfectSquare(x): 
  
      
     
    sr = math.sqrt(x) 
   
    
    return ((sr - math.floor(sr)) == 0) 
  
 
  
x = 2500
if (isPerfectSquare(x)): 
    print("Yes") 
else: 
    print("No") 
