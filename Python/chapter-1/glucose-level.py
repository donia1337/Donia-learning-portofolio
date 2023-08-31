#small glucose level check code:
# Glucose level is an input for this software
print ('Please write down your glucose level.')
glucose_level = int(input())

# Display message if glucose level is lower than 70
if glucose_level < 70:
    print("Low Glucose Level")

# Display message if Glucose level is higher than 170

elif glucose_level > 170:
    print("High Glucose Level")

#Display message if none of the above conditions are met

else:
    print("Normal Glucose Level")