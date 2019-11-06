import math
ask_number = input ('Please enter any number:')
ask_exponent = input ('Please enter exponent:')
result1 = int (ask_number) ** int (ask_exponent)
type_of_result1 = type (result1)
result2 = math.pow (int (ask_number), int (ask_exponent))
type_of_result2 = type (result2)
print ('The Result by the first way:', result1, 'Type of result:', type_of_result1) 
print ('The Result  by the second way:', result2, 'Type of result:', type_of_result2)
