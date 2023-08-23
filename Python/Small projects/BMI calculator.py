# Starting with input of height and weight values.


height = input("enter your height in metres: ")
weight = input("enter your weight in kilograms: ")

# Making sure that the height and weight values are having proper data types.

height_as_float = float(height)
weight_as_int = int(weight)

# Using the ** operator:

bmi = weight_as_int / height_as_float ** 2

# Or using multiplication or PEMDAS:
# bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)
