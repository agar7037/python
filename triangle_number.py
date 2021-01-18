def tri_num(number):

    number = number
    current_sum = 0
    i = 1 
    while i <= number:
        current_sum = i + current_sum
        i += 1
        
    return current_sum 

result = tri_num(5)
print(result)

user_num = input("enter number:\n")
user_num = int(user_num)
result = tri_num(user_num)
print(result)
        


