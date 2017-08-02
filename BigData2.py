import os.path

#find the first occurence of a given symbol in a given string
#returns the index where found, or -1 if not found
def findFirst(string, symbol):
    localString = str(string)
    for i in range(len(localString)):
        if localString[i:i+1] == symbol:
            return i
    return -1
        
# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))  

#initialize times and months list
times=[]
months=[]

#load the csv file in read mode
filename = os.path.join(directory, "LAPD_Calls_for_Service_2016.csv")
datafile = open(filename,'r')

# Go through all the calls that year
for line in datafile:
    #split the csv data into variables per line
    num, district, area, date, time, callType, desc = line.split(',')
    # change the time format in csv file to a string and obtain the hour
    middle = str(time[0:findFirst(time, ":")])
    #cast the string hour into an int for future graphing
    middleNum = int(middle)
    #add the int hour time to the times array for histogram
    times.append(middleNum)
    
    #change the date format in csv file to a string and obtain the month
    month = str(date[0:findFirst(date, "/")])
    #cast the string month into an int for future graphing
    int_month = int(month)
    #add the int month to the months array for histogram
    months.append(int_month)
                   
#Close that year's file
datafile.close()
    
# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax  = plt.subplots(1, 1)
#setup histogram: give data, choose color, choose bins
a = ax.hist(times, color='red', bins=range(0,24,3)) 
ax.set_title('Los Angeles Police Dispatch Call Times 2016')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Frequency (# of calls)')
fig.show()

fig2, ax  = plt.subplots(1, 1)
#setup histogram: give data, choose color, choose bins
a = ax.hist(months, color='blue', bins=range(1,12,1)) 
ax.set_title('Los Angeles Police Dispatch Calls 2016')
ax.set_xlabel('Month')
ax.set_ylabel('Frequency (# of calls)')
fig2.show()
