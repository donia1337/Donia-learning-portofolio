# Lambda 
# The first input is the price, while the second input is the percentage we need to calculate: 10% of 50 is 5.0.

price = int(input())
perc = int(input())

res = (lambda x,y:x*y/100)(price, perc)

print(res)


# Using lambda syntax multiply number on the list by 2.

nums = [11, 22, 33]
a = list(map(lambda x: x*2, nums))

print(a)


