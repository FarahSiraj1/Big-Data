# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:05:45 2022

@author: IT
"""
import pandas as pd
import datetime
import numpy

#Assuming input file exhibitA_input.csv is in the same directory where the code .py file is
df = pd.read_csv("exhibitA-input.csv")

df['PLAY_TS']  =df['PLAY_TS'].astype(str)   
# filtered on Date to get only 10th Aug 2016 records
filterdf=df[df["PLAY_TS"].str.startswith("10/08/2016")]
# Apply groupby on CLIENT_ID and SONG_ID to get dintinct songs per client and removed the index
new1=filterdf.groupby(['CLIENT_ID','SONG_ID']).count().reset_index()
#Apply groupby on CLIENT_ID and count as an aggregate function to get number of song played by each client
new2=new1.groupby(['CLIENT_ID']).count()
#Apply groupby on SONG_ID and count as an aggregate function to get count of client per distinct song count then removed index
new3=new2.groupby(['SONG_ID']).count().reset_index()
#Replaced names of columns as given in output
new4=new3[['SONG_ID','PLAY_ID']].rename(columns={'SONG_ID':'DISTINCT_PLAY_COUNT','PLAY_ID':'CLIENT_COUNT'})
#Remove the index
new5=new4.reset_index(drop=True)
#Save the output with name "Output.xlsx" in the same folder where input file is
writer = pd.ExcelWriter('Output.xlsx')
new5.to_excel(writer, 'Output')
writer.save()


print(new5)


