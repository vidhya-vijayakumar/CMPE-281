import pymysql
import csv
conn= pymysql.connect(user="vidhya",password="Bedesirous1*",host="127.0.0.1",db="sensor")
a = conn.cursor()
Station_Repository= 'select * from `Station_Repository`;'
a.execute(Station_Repository)
countrow = a.execute(Station_Repository)
print("Number of records in Station_Repository :",countrow)
#Sensor_Data= 'select * from `Sensor_Data`;'
#a.execute(Sensor_Data)
#countrow1= a.execute(Sensor_Data)
#print("Number of records  in Sensor_Data:",countrow1)
Sensor_Repository= 'select * from `sensor_repo`;'
a.execute(Sensor_Repository)
countrow2 = a.execute(Sensor_Repository)
print("Number of records  in Sensor_Repository:",countrow2)
Sensor_Values= 'select * from `Sensor_Values`;'
a.execute(Sensor_Values)
countrow3= a.execute(Sensor_Values)
print("Number of records  in Sensor_Values:",countrow3)
#To add a 1 year data (csv file) into Sensor_Repository
Add_data=csv.reader(file('/Users/vidhya/Downloads/Sensor5_2013.csv'))
for row in Add_data:
    #print row[1]
    #print row[2]
    a.execute("INSERT INTO Sensor_Values (Sensor_ID,POC,UNITS) VALUES (%s,%s,%s)" %(row[1],row[2],row[3]) )
# To list all the active Sensors
Active_Sensor='select distinct(a.Sensor_ID),a.Base_station_Code,a.Base_Station_Name from sensor_values a, sensor_repo b where a.State=b.Station_Name;'
#To Delete a sensor
Delect_Sensor='delete * from sensor_values where Sensor_ID=60190242'
#To add a sensor
Add_Sensor='insert into sensor_values values (select * from insert_data)'
#To delete a Station
Delete_Station='delete * from sensor_values where Sensor_ID=60190242'
#To add a Station
Add_Sensor='insert into Station values (select * from Station_data)'

#To add user info
Update_User='Insert into User values(Jhon,Basic_User,1);'
#To list Weekly sensor Data
Weekly_Data= 'SELECT WEEK(Date_Recorded),Site_Name AS WEEK from Sensor_Data where WEEK(DATE_Recorded)=16;'
#To list monthly sensor Data
Month_Data='SELECT MONTH(Date_Recorded),Site_Name AS WEEK from Sensor_Data where MONTH(Date_Recorded)=9;'
