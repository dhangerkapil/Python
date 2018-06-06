
import os
import csv


video = input("Show or Movie Name? ")


csvpath = os.path.join("C:\\", "GW Data Science Bootcamp", "Exercises" , "netflix_ratings.csv")



found = False

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            
            found = True

            
              
    if found is False:
        print("Sorry , We dont have show/movie your are looking for!")
