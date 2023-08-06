# Cost per kg is 5.
# Complete the shipping_cost() function to take the weight as an argument, calculate the shipping cost based on the weight, and display it in the given format.

print("Shipping cost depends on the weight. Cost per kg is 5dkk.")
print("Please enter weight of the package")

#taking the weight as input
weight = int(input())

#complete the function
def shipping_cost(weight):
  print(weight*5)   

#function call


print("Your shipping cost is:") 
shipping_cost(weight)

