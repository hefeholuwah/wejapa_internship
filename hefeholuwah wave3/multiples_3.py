#Multiples of Three
#Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [mul for mul in range(3,61) if mul % 3 == 0] 
print(multiples_3)
