a= [-2,1,-3,4-1,2,1,-5,4]
max_sum=0
current_sum =0
for i in a:
    current_sum += i
    if current_sum > max_sum:
           max_sum=current_sum
    elif current_sum <0 :
            current_sum=0
print (max_sum)
