# This python script should handle the data analysing of the JSON file with all of our retrieved data.
# Look at https://www.geeksforgeeks.org/read-json-file-using-python/ to figure out how!
# https://stackoverflow.com/questions/16129652/accessing-json-elements might also be good!

# We want to be able to read the elements in the JSON file, and handle the data. Thereafter show it with either a picture or a graph.
# An example could be to use to numerical values of a matrix and convert them into a picture, turning the numerical values into color values.

# Open file created by pull_in_text_file.py

with open("Python_project_1/data.txt") as line:
    data = line.readlines()

# Transform data to the output: [forecasted time, northern hemespihere hpi value]

transformed_data = []
for line in data:
    line = line.split()
    transformed_data.append([line[0], line[2]])
    
import matplotlib.pyplot as plt
import numpy as np

# Save only forecasted time values in X and save HPI values in Y.
# Save only time values in x and remove date
x = [(transformed_data[0])[11:] for transformed_data in transformed_data]
y = [int(transformed_data[1]) for transformed_data in transformed_data]

# Print values from above.
# for i in range(len(x)):
#     print(x[i],y[i])

# Create graph based on values above.

plt.plot(x,y, color="purple")
plt.xlabel('date and time')
plt.ylabel('hpi value')
plt.xticks([])
plt.title("Current aurora forecast from " + x[0] + " to " + x[len(x)-1])

# Save plot in image file
plt.savefig('AuroraForecast.jpg')
#plt.show()


