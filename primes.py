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
    prime_list = []
    i = 2
    while len(prime_list) < n:
        is_prime = find_prime(i)
        
        if is_prime: 
            prime_list.append(i)
            i += 1
        else: 
            i += 1
    for x in prime_list:
        print(x)
    
    return 
        

number = input("enter an integer: \n")
number = int(number)
result = find_prime(number)
print(result)

number = input("enter another integer: \n")
number = int(number)
generate_prime(number)


            


