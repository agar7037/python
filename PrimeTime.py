import time 

def find_prime(number):
    n = number
    i = 1
    if n <= 1: 
      
        return False
    while i < n-1:
        modulus = n % (n-i)
        if modulus == 0:
            
            return False 
        else:
            i += 1 
    
    return True 

def generate_prime(n):
   # prime_list = []
    i = 2
    j = 0 
    if n == 0 : 
        print(f"cannot generate 0th prime")
        exit()
    while j < n:
        is_prime = find_prime(i)
        
        if is_prime: 
            prime = i 
            i += 1
            j += 1
        else: 
            i += 1
    

    return prime
   

t = time.localtime()
mins = t.tm_min
hour = t.tm_hour
print(f"This program started at {hour}:{mins}\n")
print(f"The {mins}th prime number is {generate_prime(mins)}")





