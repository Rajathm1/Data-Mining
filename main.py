from __future__ import division

import pandas as pd

import datetime

insulin_data = pd.read_csv('InsulinData.csv')
insulin_data = insulin_data[['Date','Time','Alarm']]
insulin_data = insulin_data.loc[insulin_data['Alarm'] == 'AUTO MODE ACTIVE PLGM OFF']


auto_mode_start_date = insulin_data.iat[0,0]
auto_mode_start_time = insulin_data.iat[0,1]



cgm_data = pd.read_csv('CGMData.csv')
cgm_data = cgm_data[['Date','Time', 'Sensor Glucose (mg/dL)']]




cgm_data[['month','day','year']] = cgm_data.Date.str.split('/',expand=True)
cgm_data[['hour','minute','seconds']] = cgm_data.Time.str.split(':',expand=True)



month = auto_mode_start_date.split('/')[0]
day = auto_mode_start_date.split('/')[1]
year = auto_mode_start_date.split('/')[2]
hour = auto_mode_start_time.split(':')[0]
minute = auto_mode_start_time.split(':')[1]
seconds = auto_mode_start_time.split(':')[2]
autom_mode_date_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(seconds))




auto_mode_count = 0
manual_mode_count = 0
overnight_count = 0
daytime_count = 0
wholeday_count = 0
prev_day = cgm_data['Date'].iloc[0]
cur_day = None
six_hours = datetime.datetime(2000, 1, 1, 6, 0, 0).time()
twelve_hours = datetime.datetime(2000, 1, 1, 0, 0, 0).time()
twenty_four_hours = datetime.datetime(2000, 1, 1, 23, 59, 59).time()
count = 0
daytime_auto_mode_sum_sum4 = overnight_auto_mode_sum1 = 0
overnight_auto_mode_sum2 = 0
overnight_auto_mode_sum3 = 0
overnight_auto_mode_sum4 = 0
overnight_auto_mode_sum5 = 0
overnight_auto_mode_sum6 = 0
overnight_auto_mode_sum_sum1 = 0
overnight_auto_mode_sum_sum2 = 0
overnight_auto_mode_sum_sum3 = 0
overnight_auto_mode_sum_sum4 = 0
overnight_auto_mode_sum_sum5 = 0
overnight_auto_mode_sum_sum6 = 0

#change overnight to day time 
daytime_auto_mode_sum1 = 0
daytime_auto_mode_sum2 = 0
daytime_auto_mode_sum3 = 0
daytime_auto_mode_sum4 = 0
daytime_auto_mode_sum5 = 0
daytime_auto_mode_sum6 = 0
daytime_auto_mode_sum_sum1 = 0
daytime_auto_mode_sum_sum2 = 0
daytime_auto_mode_sum_sum3 = 0
daytime_auto_mode_sum_sum5 = 0
daytime_auto_mode_sum_sum6 = 0

wholeday_auto_mode_sum1 = 0
wholeday_auto_mode_sum2 = 0
wholeday_auto_mode_sum3 = 0
wholeday_auto_mode_sum4 = 0
wholeday_auto_mode_sum5 = 0
wholeday_auto_mode_sum6 = 0
wholeday_auto_mode_sum_sum1 = 0
wholeday_auto_mode_sum_sum2 = 0
wholeday_auto_mode_sum_sum3 = 0
wholeday_auto_mode_sum_sum4 = 0
wholeday_auto_mode_sum_sum5 = 0
wholeday_auto_mode_sum_sum6 = 0

overnight_manual_mode_sum1 = 0
overnight_manual_mode_sum2 = 0
overnight_manual_mode_sum3 = 0
overnight_manual_mode_sum4 = 0
overnight_manual_mode_sum5 = 0
overnight_manual_mode_sum6 = 0
overnight_manual_mode_sum_sum1 = 0
overnight_manual_mode_sum_sum2 = 0
overnight_manual_mode_sum_sum3 = 0
overnight_manual_mode_sum_sum4 = 0
overnight_manual_mode_sum_sum5 = 0
overnight_manual_mode_sum_sum6 = 0

#change overnight to day time 
daytime_manual_mode_sum1 = 0
daytime_manual_mode_sum2 = 0
daytime_manual_mode_sum3 = 0
daytime_manual_mode_sum4 = 0
daytime_manual_mode_sum5 = 0
daytime_manual_mode_sum6 = 0
daytime_manual_mode_sum_sum1 = 0
daytime_manual_mode_sum_sum2 = 0
daytime_manual_mode_sum_sum3 = 0
daytime_manual_mode_sum_sum4 = 0
daytime_manual_mode_sum_sum5 = 0
daytime_manual_mode_sum_sum6 = 0

wholeday_manual_mode_sum1 = 0
wholeday_manual_mode_sum2 = 0
wholeday_manual_mode_sum3 = 0
wholeday_manual_mode_sum4 = 0
wholeday_manual_mode_sum5 = 0
wholeday_manual_mode_sum6 = 0
wholeday_manual_mode_sum_sum1 = 0
wholeday_manual_mode_sum_sum2 = 0
wholeday_manual_mode_sum_sum3 = 0
wholeday_manual_mode_sum_sum4 = 0
wholeday_manual_mode_sum_sum5 = 0
wholeday_manual_mode_sum_sum6 = 0


count = 0
for index, row in cgm_data.iterrows():
    date_time = datetime.datetime(int(row['year']), int(row['month']), int(row['day']), int(row['hour']), int(row['minute']), int(row['seconds']))
    cur_day = row['Date']
    glucose = row['Sensor Glucose (mg/dL)']
    if(date_time > autom_mode_date_time):
        #auto_mode code
     if(prev_day == cur_day):
      #wholeday
      wholeday_count+=1
      if(glucose > 180) :
       wholeday_auto_mode_sum1 += 1
      if(glucose > 250) :
       wholeday_auto_mode_sum2 += 1
      if(glucose >= 70 and glucose <= 180) :
       wholeday_auto_mode_sum3 += 1
      if(glucose >= 70 and glucose <= 150) :
       wholeday_auto_mode_sum4 += 1
      if(glucose < 70) :
       wholeday_auto_mode_sum5 += 1
      if(glucose < 54) :
       wholeday_auto_mode_sum6 += 1
            
      if(date_time.time() > twelve_hours and date_time.time() <= six_hours):
      #overnight    
       if(glucose > 180) :
            overnight_auto_mode_sum1 += 1
       if(glucose > 250) :
            overnight_auto_mode_sum2 += 1
       if(glucose >= 70 and glucose <= 180) :
           overnight_auto_mode_sum3 += 1
       if(glucose >= 70 and glucose <= 150) :
           overnight_auto_mode_sum4 += 1
       if(glucose < 70) :
           overnight_auto_mode_sum5 += 1
       if(glucose < 54) :
           overnight_auto_mode_sum6 += 1
       overnight_count += 1
      if(date_time.time() > six_hours and date_time.time() <= twenty_four_hours):
      #daytime
       if(glucose > 180) :
            daytime_auto_mode_sum1 += 1
       if(glucose > 250) :
            daytime_auto_mode_sum2 += 1
       if(glucose >= 70 and glucose <= 180) :
           daytime_auto_mode_sum3 += 1
       if(glucose >= 70 and glucose <= 150) :
           daytime_auto_mode_sum4 += 1
       if(glucose < 70) :
           daytime_auto_mode_sum5 += 1
       if(glucose < 54) :
           daytime_auto_mode_sum6 += 1
       daytime_count +=1
     else:
      count+=1
      overnight_auto_mode_sum_sum1 += overnight_auto_mode_sum1/288
      overnight_auto_mode_sum_sum2 += overnight_auto_mode_sum2/288
      overnight_auto_mode_sum_sum3 += overnight_auto_mode_sum3/288
      overnight_auto_mode_sum_sum4 += overnight_auto_mode_sum4/288
      overnight_auto_mode_sum_sum5 += overnight_auto_mode_sum5/288
      overnight_auto_mode_sum_sum6 += overnight_auto_mode_sum6/288
      overnight_auto_mode_sum1 = 0
      overnight_auto_mode_sum2 = 0
      overnight_auto_mode_sum3 = 0
      overnight_auto_mode_sum4 = 0
      overnight_auto_mode_sum5 = 0
      overnight_auto_mode_sum6 = 0
    
      daytime_auto_mode_sum_sum1 += daytime_auto_mode_sum1/288
      daytime_auto_mode_sum_sum2 += daytime_auto_mode_sum2/288
      daytime_auto_mode_sum_sum3 += daytime_auto_mode_sum3/288
      daytime_auto_mode_sum_sum4 += daytime_auto_mode_sum4/288
      daytime_auto_mode_sum_sum5 += daytime_auto_mode_sum5/288
      daytime_auto_mode_sum_sum6 += daytime_auto_mode_sum6/288
      daytime_auto_mode_sum1 = 0
      daytime_auto_mode_sum2 = 0
      daytime_auto_mode_sum3 = 0
      daytime_auto_mode_sum4 = 0
      daytime_auto_mode_sum5 = 0
      daytime_auto_mode_sum6 = 0
    
      wholeday_auto_mode_sum_sum1 += wholeday_auto_mode_sum1/288
      wholeday_auto_mode_sum_sum2 += wholeday_auto_mode_sum2/288
      wholeday_auto_mode_sum_sum3 += wholeday_auto_mode_sum3/288
      wholeday_auto_mode_sum_sum4 += wholeday_auto_mode_sum4/288
      wholeday_auto_mode_sum_sum5 += wholeday_auto_mode_sum5/288
      wholeday_auto_mode_sum_sum6 += wholeday_auto_mode_sum6/288
      wholeday_auto_mode_sum1 = 0
      wholeday_auto_mode_sum2 = 0
      wholeday_auto_mode_sum3 = 0
      wholeday_auto_mode_sum4 = 0
      wholeday_auto_mode_sum5 = 0
      wholeday_auto_mode_sum6 = 0
      
     auto_mode_count+=1    
    else:
        #manual_mode code
     if(prev_day == cur_day):
      #wholeday
      wholeday_count+=1
      if(date_time.time() > twelve_hours and date_time.time() <= six_hours):
      #overnight
       overnight_count += 1
      if(date_time.time() > six_hours and date_time.time() <= twenty_four_hours):
      #daytime
       daytime_count +=1
     else:
      count+=1
     manual_mode_count+=1
     #manual_mode code
     if(prev_day == cur_day):
      #wholeday
      wholeday_count+=1
      if(glucose > 180) :
       wholeday_manual_mode_sum1 += 1
      if(glucose > 250) :
       wholeday_manual_mode_sum2 += 1
      if(glucose >= 70 and glucose <= 180) :
       wholeday_manual_mode_sum3 += 1
      if(glucose >= 70 and glucose <= 150) :
       wholeday_manual_mode_sum4 += 1
      if(glucose < 70) :
       wholeday_manual_mode_sum5 += 1
      if(glucose < 54) :
       wholeday_manual_mode_sum6 += 1
            
      if(date_time.time() > twelve_hours and date_time.time() <= six_hours):
      #overnight    
       if(glucose > 180) :
            overnight_manual_mode_sum1 += 1
       if(glucose > 250) :
            overnight_manual_mode_sum2 += 1
       if(glucose >= 70 and glucose <= 180) :
           overnight_manual_mode_sum3 += 1
       if(glucose >= 70 and glucose <= 150) :
           overnight_manual_mode_sum4 += 1
       if(glucose < 70) :
           overnight_manual_mode_sum5 += 1
       if(glucose < 54) :
           overnight_manual_mode_sum6 += 1
       overnight_count += 1
      if(date_time.time() > six_hours and date_time.time() <= twenty_four_hours):
      #daytime
       if(glucose > 180) :
            daytime_manual_mode_sum1 += 1
       if(glucose > 250) :
            daytime_manual_mode_sum2 += 1
       if(glucose >= 70 and glucose <= 180) :
           daytime_manual_mode_sum3 += 1
       if(glucose >= 70 and glucose <= 150) :
           daytime_manual_mode_sum4 += 1
       if(glucose < 70) :
           daytime_manual_mode_sum5 += 1
       if(glucose < 54) :
           daytime_manual_mode_sum6 += 1
       daytime_count +=1
     else:
      count+=1
      overnight_manual_mode_sum_sum1 += overnight_manual_mode_sum1/288
      overnight_manual_mode_sum_sum2 += overnight_manual_mode_sum2/288
      overnight_manual_mode_sum_sum3 += overnight_manual_mode_sum3/288
      overnight_manual_mode_sum_sum4 += overnight_manual_mode_sum4/288
      overnight_manual_mode_sum_sum5 += overnight_manual_mode_sum5/288
      overnight_manual_mode_sum_sum6 += overnight_manual_mode_sum6/288
      overnight_manual_mode_sum1 = 0
      overnight_manual_mode_sum2 = 0
      overnight_manual_mode_sum3 = 0
      overnight_manual_mode_sum4 = 0
      overnight_manual_mode_sum5 = 0
      overnight_manual_mode_sum6 = 0
    
      daytime_manual_mode_sum_sum1 += daytime_manual_mode_sum1/288
      daytime_manual_mode_sum_sum2 += daytime_manual_mode_sum2/288
      daytime_manual_mode_sum_sum3 += daytime_manual_mode_sum3/288
      daytime_manual_mode_sum_sum4 += daytime_manual_mode_sum4/288
      daytime_manual_mode_sum_sum5 += daytime_manual_mode_sum5/288
      daytime_manual_mode_sum_sum6 += daytime_manual_mode_sum6/288
      daytime_manual_mode_sum1 = 0
      daytime_manual_mode_sum2 = 0
      daytime_manual_mode_sum3 = 0
      daytime_manual_mode_sum4 = 0
      daytime_manual_mode_sum5 = 0
      daytime_manual_mode_sum6 = 0
    
      wholeday_manual_mode_sum_sum1 += wholeday_manual_mode_sum1/288
      wholeday_manual_mode_sum_sum2 += wholeday_manual_mode_sum2/288
      wholeday_manual_mode_sum_sum3 += wholeday_manual_mode_sum3/288
      wholeday_manual_mode_sum_sum4 += wholeday_manual_mode_sum4/288
      wholeday_manual_mode_sum_sum5 += wholeday_manual_mode_sum5/288
      wholeday_manual_mode_sum_sum6 += wholeday_manual_mode_sum6/288
      wholeday_manual_mode_sum1 = 0
      wholeday_manual_mode_sum2 = 0
      wholeday_manual_mode_sum3 = 0
      wholeday_manual_mode_sum4 = 0
      wholeday_manual_mode_sum5 = 0
      wholeday_manual_mode_sum6 = 0
    #TODO
    prev_day = cur_day
    

totaldays = len(cgm_data)/288
overnight_auto_mode_sum_sum1 = overnight_auto_mode_sum_sum1/totaldays*100
overnight_auto_mode_sum_sum2 = overnight_auto_mode_sum_sum2/totaldays*100
overnight_auto_mode_sum_sum3 = overnight_auto_mode_sum_sum3/totaldays*100
overnight_auto_mode_sum_sum4 = overnight_auto_mode_sum_sum4/totaldays*100
overnight_auto_mode_sum_sum5 = overnight_auto_mode_sum_sum5/totaldays*100
overnight_auto_mode_sum_sum6 = overnight_auto_mode_sum_sum6/totaldays*100
#print(overnight_auto_mode_sum_sum1, overnight_auto_mode_sum_sum2,overnight_auto_mode_sum_sum3,overnight_auto_mode_sum_sum4,overnight_auto_mode_sum_sum5,overnight_auto_mode_sum_sum6)


daytime_auto_mode_sum_sum1 = daytime_auto_mode_sum_sum1/totaldays*100
daytime_auto_mode_sum_sum2 = daytime_auto_mode_sum_sum2/totaldays*100
daytime_auto_mode_sum_sum3 = daytime_auto_mode_sum_sum3/totaldays*100
daytime_auto_mode_sum_sum4 = daytime_auto_mode_sum_sum4/totaldays*100
daytime_auto_mode_sum_sum5 = daytime_auto_mode_sum_sum5/totaldays*100
daytime_auto_mode_sum_sum6 = daytime_auto_mode_sum_sum6/totaldays*100
#print(daytime_auto_mode_sum_sum1, daytime_auto_mode_sum_sum2,daytime_auto_mode_sum_sum3,daytime_auto_mode_sum_sum4,daytime_auto_mode_sum_sum5,daytime_auto_mode_sum_sum6)


wholeday_auto_mode_sum_sum1 = wholeday_auto_mode_sum_sum1/totaldays*100
wholeday_auto_mode_sum_sum2 = wholeday_auto_mode_sum_sum2/totaldays*100
wholeday_auto_mode_sum_sum3 = wholeday_auto_mode_sum_sum3/totaldays*100
wholeday_auto_mode_sum_sum4 = wholeday_auto_mode_sum_sum4/totaldays*100
wholeday_auto_mode_sum_sum5 = wholeday_auto_mode_sum_sum5/totaldays*100
wholeday_auto_mode_sum_sum6 = wholeday_auto_mode_sum_sum6/totaldays*100
#print(wholeday_auto_mode_sum_sum1, wholeday_auto_mode_sum_sum2,wholeday_auto_mode_sum_sum3,wholeday_auto_mode_sum_sum4,wholeday_auto_mode_sum_sum5,wholeday_auto_mode_sum_sum6)

overnight_manual_mode_sum_sum1 = overnight_manual_mode_sum_sum1/totaldays*100
overnight_manual_mode_sum_sum2 = overnight_manual_mode_sum_sum2/totaldays*100
overnight_manual_mode_sum_sum3 = overnight_manual_mode_sum_sum3/totaldays*100
overnight_manual_mode_sum_sum4 = overnight_manual_mode_sum_sum4/totaldays*100
overnight_manual_mode_sum_sum5 = overnight_manual_mode_sum_sum5/totaldays*100
overnight_manual_mode_sum_sum6 = overnight_manual_mode_sum_sum6/totaldays*100
#print(overnight_manual_mode_sum_sum1, overnight_manual_mode_sum_sum2,overnight_manual_mode_sum_sum3,overnight_manual_mode_sum_sum4,overnight_manual_mode_sum_sum5,overnight_manual_mode_sum_sum6)


daytime_manual_mode_sum_sum1 = daytime_manual_mode_sum_sum1/totaldays*100
daytime_manual_mode_sum_sum2 = daytime_manual_mode_sum_sum2/totaldays*100
daytime_manual_mode_sum_sum3 = daytime_manual_mode_sum_sum3/totaldays*100
daytime_manual_mode_sum_sum4 = daytime_manual_mode_sum_sum4/totaldays*100
daytime_manual_mode_sum_sum5 = daytime_manual_mode_sum_sum5/totaldays*100
daytime_manual_mode_sum_sum6 = daytime_manual_mode_sum_sum6/totaldays*100
#print(daytime_manual_mode_sum_sum1, daytime_manual_mode_sum_sum2,daytime_manual_mode_sum_sum3,daytime_manual_mode_sum_sum4,daytime_manual_mode_sum_sum5,daytime_manual_mode_sum_sum6)


wholeday_manual_mode_sum_sum1 = wholeday_manual_mode_sum_sum1/totaldays*100
wholeday_manual_mode_sum_sum2 = wholeday_manual_mode_sum_sum2/totaldays*100
wholeday_manual_mode_sum_sum3 = wholeday_manual_mode_sum_sum3/totaldays*100
wholeday_manual_mode_sum_sum4 = wholeday_manual_mode_sum_sum4/totaldays*100
wholeday_manual_mode_sum_sum5 = wholeday_manual_mode_sum_sum5/totaldays*100
wholeday_manual_mode_sum_sum6 = wholeday_manual_mode_sum_sum6/totaldays*100
#print(wholeday_manual_mode_sum_sum1, wholeday_manual_mode_sum_sum2,wholeday_manual_mode_sum_sum3,wholeday_manual_mode_sum_sum4,wholeday_manual_mode_sum_sum5,wholeday_manual_mode_sum_sum6)


line1 = [overnight_manual_mode_sum_sum1, overnight_manual_mode_sum_sum2,overnight_manual_mode_sum_sum3,overnight_manual_mode_sum_sum4,overnight_manual_mode_sum_sum5,overnight_manual_mode_sum_sum6,
daytime_manual_mode_sum_sum1, daytime_manual_mode_sum_sum2,daytime_manual_mode_sum_sum3,daytime_manual_mode_sum_sum4,daytime_manual_mode_sum_sum5,daytime_manual_mode_sum_sum6,
wholeday_manual_mode_sum_sum1, wholeday_manual_mode_sum_sum2,wholeday_manual_mode_sum_sum3,wholeday_manual_mode_sum_sum4,wholeday_manual_mode_sum_sum5,wholeday_manual_mode_sum_sum6,1.1]

line2 = [overnight_auto_mode_sum_sum1, overnight_auto_mode_sum_sum2,overnight_auto_mode_sum_sum3,overnight_auto_mode_sum_sum4,overnight_auto_mode_sum_sum5,overnight_auto_mode_sum_sum6,
daytime_auto_mode_sum_sum1, daytime_auto_mode_sum_sum2,daytime_auto_mode_sum_sum3,daytime_auto_mode_sum_sum4,daytime_auto_mode_sum_sum5,daytime_auto_mode_sum_sum6,
wholeday_auto_mode_sum_sum1, wholeday_auto_mode_sum_sum2,wholeday_auto_mode_sum_sum3,wholeday_auto_mode_sum_sum4,wholeday_auto_mode_sum_sum5,wholeday_auto_mode_sum_sum6,1.1]



lines = []
lines.append(line1)
lines.append(line2)

lines = pd.DataFrame(lines)

lines.to_csv("Results.csv", index=False, header = False)
