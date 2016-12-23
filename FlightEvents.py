# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import dateutil
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

#with open("C:/Users/VeluswamyS/Documents/GitHub/DATASET/AviationDataUP.csv", "r") as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=",")
 #   my_list = [row for row in csvreader]
 #   np_list = np.array(my_list, dtype=object)
 #   data = np_list[2:]
 
# read the the raw CSV using pandas

df = pd.read_csv( "C:/Users/VeluswamyS/Documents/GitHub/DATASET/AviationDataUP.csv") 
df_master=df[['Investigation.Type','Event.Date','Country','Aircraft.Category','Make']]
#write new CVS file with the dataframe created above
#df_master.to_csv("newfile.csv")
# check the total count of the events recorded
EventCount=df_master['Investigation.Type'].count()
print("the Total number of events recorded is = "+str(EventCount))
pd.options.mode.chained_assignment = None #disabling the warning in the next step
df_master['Event.Date']=pd.to_datetime(df_master['Event.Date'],errors='coerce')
df_master['Year'] = df_master['Event.Date'].dt.year #splitting the  Year from the date
df_master['Month']=df_master['Event.Date'].dt.month # splitting the  month from the date
df_master['Day']=df_master['Event.Date'].dt.day #splitting the Day from the date
# check if the date has got split correctly
# df_master.to_csv("newfileXX21.csv")#

# steps to clean the blank cell - identify the blank cell and delete the rows
#replace the blank values NaN
df_master['Make'].replace('', np.nan, inplace=True)
df_master['Make'].replace('', np.nan, inplace=True)
df_master['Country'].replace('', np.nan, inplace=True)

#remove rows with NaN to get clean file 
df_master.dropna(subset=['Make'],inplace=True)
df_master.dropna(subset=['Aircraft.Category'],inplace=True)
df_master.dropna(subset=['Country'],inplace=True)

#remove rows with NaN to get clean file 
df_master.to_csv("CleanFile1.csv")

#check frequecy of occurance of events
#this gves the details of the frequecy of an aircraft catergory involved in an event
aircategory=pd.crosstab(index=df_master["Aircraft.Category"],columns="count")
#print (("Details of the frequecy of an aircraft catergory involved in an event = \n"+str(aircategory)))
print ("the top 3 aircrafts involved in an Event is as follow : \n " +str(aircategory.nlargest(3,"count")))
print ("The bottom 3 aircrafts involved in an Event is as follow : \n " +str(aircategory.nsmallest(3,"count")))
aircategory.plot.bar(color=('r','g','b','c'))

#Years where max and min number of events occured
EventYR=pd.crosstab(index=df_master["Year"],columns="count")
print ("Top 3 years when Max number of events recorded is : \n " +str(EventYR.nlargest(3,"count")))
print ("Top 3 years when Min number of events recorded is : \n " +str(EventYR.nsmallest(3,"count")))
EventYR.plot.bar(color=('r','g','b','c'))

# Month where max and min number of events occured
EventMonth=pd.crosstab(index=df_master["Month"],columns="count")
print ("Top 3 Months when Max number of events recorded is : \n " +str(EventMonth.nlargest(3,"count")))
print ("Top 3 Months when Min number of events recorded is : \n " +str(EventMonth.nsmallest(3,"count")))
EventMonth.plot.bar(color=('r','g','b','c'))

# Month where max and min number of events occured

EventDay=pd.crosstab(index=df_master["Day"],columns="count")
print ("Top 5 Day when Max number of events recorded is : \n " +str(EventDay.nlargest(5,"count")))
print ("Top 5 Day when Min number of events recorded is : \n " +str(EventDay.nsmallest(5,"count")))
EventDay.plot.bar(color=('r','g','b','c'))



