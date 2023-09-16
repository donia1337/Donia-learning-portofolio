#targetURL = ("https://services.swpc.noaa.gov/text/aurora-nowcast-hemi-power.txt")

import urllib.request

data = urllib.request.urlopen("https://services.swpc.noaa.gov/text/aurora-nowcast-hemi-power.txt")
for line in data:
    print (line)



#data = urllib.request.urlopen("https://services.swpc.noaa.gov/json/ovation_aurora_latest.json")
#for line in data:
#    print (line)



