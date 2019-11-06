import random
rundom_value = random.randint(0,1000)
exponent_result = (rundom_value ** 2)
value_is_more_then = bool (rundom_value > 10)
exp_result_is_more_then = bool (exponent_result > 500)
print ('The number:', rundom_value)
print ('The number to the power of exponent:', exponent_result)
print ('The number is more then 10:', value_is_more_then)
print ('The number to the power of exponent is more then 500:', exp_result_is_more_then)