# Cost per kg is 5.
# Complete the shipping_cost() function to take the weight as an argument, calculate the shipping cost based on the weight, and display it in the given format.

#taking the weight as input
weight = int(input())

#complete the function
def shipping_cost(weight):
  print(weight*5)   

#function call
shipping_cost(weight)