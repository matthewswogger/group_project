# How to deal with large ass csv files
I set it up so that csv files will not be tracked by git so they will not be pushed to github because they are very large. I zipped the `data` folder with all four csv files together. I will email this zipfile to you. Before running any code you need to place the zipfile in the folder and unzip it. Zip files will also not be tracked by git.

If you save a csv file at some point make sure to let the rest of us know so we get the same data.

# What I looked into on homework 1
For airplane cancellations
- month
- day of the week
- type of cancellations
  - A = carrier
  - B = weather
  - C = NAS 'National Air System'
  - D = security

For airplane delays, both arrival and departing
- month
  - arrival
  - departing

# What I DIDN'T look into on homework 1
For airplane cancellations
- geography

For airplane delays, both arrival and departing
- day of the week
- geography
- type of delay
  - CarrierDelay
  - WeatherDelay
  - NASDelay
  - SecurityDelay
  - LateAircraftDelay

Anything else you can think of to look into.

## What I did to the original data
I joined tabels `2008.csv`, `airports.csv`, and `carriers.csv` together right at the beginning to make table `clean.csv`. I this process I dropped a few columns that I dedided were either redundant or of no use. If either of you think one of those columns HAS A USE please feel free to join it back in, or work with the original data instead of `clean.csv`. You can see this process in file `airplane_functions.py`.
