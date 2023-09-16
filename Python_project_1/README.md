# Python_project_1

This project pulls in a url link of data, to convert it to it's original state (a json file)

Thereafter the data will be analyzed and shown in either a picture, graph or text in the README.md file.

A trigger will be set for when the project should be run automatically - either hourly, daily, weekly etc.

When a set limit is hit a mail should be sent to my personal email.

# Example used

For this project I wanted to set up an alarm whenever there would be a high outburst of aurora. I am using the link: https://www.swpc.noaa.gov/products/aurora-30-minute-forecast
Here I want to read the data, and whenever it hits a high level of "HPI" meaning there is a lot of aurora, I want to send myself an alarm.

Since I am completely in love with photography and northern lights, that way I can know when I should drive to the nearest beach and take pictures of the beautiful aurora!

# Step-by-step

1. Trigger: either hourly, daily or weekly
2. Starts read_website.py which find the url of the data and stores it in a textfile
3. Starts pull_in_json_file.py which uses the url, pulls in the data and converts it to a readable json file.
4. Starts data_analysing.py which uses the json file and analyses the data to show it in some way.
5. Push the new analysed data into the README to show itin some way. If a limit is hit send a email to my personal mail.