import math   

def isPSquare(num): 
    n = int(math.sqrt(num)) 
    return(n * n == num) 
  
# Function to check if the number is in Fibonacci or not 
def is_fibonacci(lst):
        count = 0
        n = len(lst)
        for i in range(n): 
                if (isPSquare(5 * lst[i] * lst[i] - 4) or isPSquare(5 * lst[i] * lst[i] + 4)): 
                        print(lst[i], " ",end =""); 
                        count += 1
          
      
        if (count==0): 
                print("None present"); 
  
lst = [4, 2, 8 , 5, 20, 1, 40, 13, 23] 
is_fibonacci(lst)
