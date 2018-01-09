"""
This program uses a CSV file downloaded from Google Trends in order to compare the frequency of searches between two terms. The graph shown displays the two terms search frequencies as percentages(which are independent of one another). Comments indicate areas that may need to be changed in order to display the graph properly. 
"""

import csv
import matplotlib.pyplot as plt
import re
from collections import defaultdict

def file(): 
   #opens the file
    master = []
    file1 = open("multiTimeline.csv", 'r') #Change me if you renamed the file
    final = csv.reader(file1)
    for i in final: 
        master.append(i)
    return master

def clean(dirty):
    #starting the process of cleaning the data
    dirtyvar1 = defaultdict(list)
    dirtyvar2 = defaultdict(list)
    count = False
    for i in dirty:
        if count == True:
            regex = re.compile("(\d\d\d\d)-(\d\d)-(\d\d)")
            regexsearch = regex.search(i[0])
            regexres = regexsearch.group(2)
            dirtyvar1[regexres].append(i[1])
            dirtyvar2[regexres].append(i[2])
        count = True
    
    var1 = []
    var2 = []
    time = []
    
    for k,v in dirtyvar1.items():
        #Averages the data of var1 over a year
        vsum = 0
        count = 0
        for i in v:
            vsum += int(i)
            count += 1
        result = vsum / count 
        var1.append(result)

    for k,v in dirtyvar2.items():
        #Averages the data of var2 over a year
        vsum = 0
        count = 0
        for i in v: 
            vsum += int(i)
            count += 1
        result = vsum / count
        var2.append(result)
        time.append(int(k))

    #sorting the data in chronological order
    var2zip = zip(time, var2)
    var1zip = zip(time, var1)
    var1zip.sort()
    var2zip.sort()

    time = []
    var1 = []
    var2 = []

    for k,v in var1zip:
        #reappending var1's data to a list (in order this time)
        var1.append(v) 
    for k,v in var2zip: 
        #reappending var2's data to a list (in order this time)
        time.append(k)
        var2.append(v)

    #Getting the mins and maxes of the variables for min-max normalization  
    minvar1 = min(var1)
    maxvar1 = max(var1)
    minvar2 = min(var2)
    maxvar2 = max(var2)

    normalvar1 = []
    normalvar2 = []

    for i in var1: 
        #Min-Max Normalization for var1
        z = ((i - float(minvar1))/(float(maxvar1)-float(minvar1)))
        normalvar1.append(z)
    for i in var2:
        #Min-Max Normalization for var2
        z = ((i - float(minvar2))/(float(maxvar2)-float(minvar2)))
        normalvar2.append(z)

    #Plot settings
    plt.plot(time, normalvar1, 'g', label = "Gym & Fitness",) #Change me!
    plt.plot(time, normalvar2, 'r', label = "Weight Loss",) #Change me!
    months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept", "Oct", "Nov", "Dec"]
    plt.xticks(range(1,13), months)
    plt.xlabel("Months")
    plt.ylabel("Relative Frequency of Search Term")
    plt.legend()
    plt.show()

def main():
    
    dirty = file() 
    data = clean(dirty)

main()