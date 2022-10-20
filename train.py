from __future__ import division
import pandas as pd
import datetime as datetime



from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import svm


from sklearn.model_selection import KFold
from sklearn.externals import joblib


from scipy.signal import find_peaks
from collections import OrderedDict
import operator
import numpy 
import scipy


import matplotlib.pyplot as plt
from scipy.fftpack import fft


CARB_COLUMN = "BWZ Carb Input (grams)"
CGM = "Sensor Glucose (mg/dL)"


FILE1 = "CGMData.csv"
FILE2 = "CGM_patient2.csv"
FILE3 = "InsulinData.csv"
FILE4 = "Insulin_patient2.csv"

col_list = ["Date","Time",CARB_COLUMN]
insulin_data1 = pd.read_csv(FILE3,  usecols=col_list,low_memory=False)
insulin_data1["datetime"] = pd.to_datetime(insulin_data1['Date'] + ' ' + insulin_data1['Time']) 
insulin_data1 = insulin_data1.iloc[::-1]

col_list = ["Date","Time",CGM]
cgm_data1 = pd.read_csv(FILE1,  usecols=col_list,low_memory=False)
cgm_data1["datetime"] = pd.to_datetime(cgm_data1['Date'] + ' ' + cgm_data1['Time']) 
cgm_data1 = cgm_data1.iloc[::-1] 
   
col_list = ["Date","Time",CARB_COLUMN]
insulin_data2 = pd.read_csv(FILE4,  usecols=col_list,low_memory=False)
insulin_data2["datetime"] = pd.to_datetime(insulin_data2['Date'] + ' ' + insulin_data2['Time']) 
insulin_data2 = insulin_data2.iloc[::-1]

col_list = ["Date","Time",CGM]
cgm_data2 = pd.read_csv(FILE2,  usecols=col_list,low_memory=False)
cgm_data2["datetime"] = pd.to_datetime(cgm_data2['Date'] + ' ' + cgm_data2['Time']) 
cgm_data2 = cgm_data2.iloc[::-1] 


insulin_data1 = insulin_data1[insulin_data1[CARB_COLUMN].notna()] 
insulin_data1 = insulin_data1[insulin_data1[CARB_COLUMN] != 0.0] 
tms1 = insulin_data1.values.tolist()


insulin_data2 = insulin_data2[insulin_data2[CARB_COLUMN].notna()]
insulin_data2 = insulin_data2[insulin_data2[CARB_COLUMN] != 0.0] 
tms2 = insulin_data2.values.tolist()


df = tms1
length = len(df) - 2
index  = 0
meal_data1 = []
no_meal_data1 = []
while(index <= length):
    tm = df[index][3]
    tm_one = df[index + 1][3]
    difference = tm_one - tm
    if(difference.total_seconds() <= 7200):
        index = index + 1
        continue
    if(difference.total_seconds() <= 1800): 
        index = index + 2
        continue
    else:
        tm_30 = tm - datetime.timedelta(minutes = 30)
        tm_2 = tm + datetime.timedelta(hours = 2)
        meal_data1.append([tm_30, tm_2])
        tm_2 = tm_2 + datetime.timedelta(hours = 2)
        count = 0
        while(tm_2 + datetime.timedelta(hours = 2) < tm_one and count < 4) :
            no_meal_data1.append([tm_2,  tm_2 + datetime.timedelta(hours = 2)])
            tm_2 = tm_2 + datetime.timedelta(hours = 2)
            count = count + 1
        index = index + 2

df = tms2
length = len(df) - 2
index  = 0
meal_data2 = []
no_meal_data2 = []
while(index <= length):
    tm = df[index][3]
    tm_one = df[index + 1][3]
    difference = tm_one - tm
    if(difference.total_seconds() <= 7200):
        index = index + 1
        continue
    if(difference.total_seconds() <= 1800): 
        index = index + 2
        continue
    else:
        tm_30 = tm - datetime.timedelta(minutes = 30)
        tm_2 = tm + datetime.timedelta(hours = 2)
        meal_data2.append([tm_30, tm_2])
        tm_2 = tm_2 + datetime.timedelta(hours = 2)
        count = 0
        while(tm_2 + datetime.timedelta(hours = 2) < tm_one and count < 4) :
            no_meal_data2.append([tm_2,  tm_2 + datetime.timedelta(hours = 2)])
            tm_2 = tm_2 + datetime.timedelta(hours = 2)
            count = count + 1
        index = index + 2

def f1(glucose):
    return max(glucose) - min(glucose)

def f3(glucose):
    max_index = glucose.index(max(glucose))
    min_index = glucose.index(min(glucose))
    return (max_index - min_index)

def f2(glucose):
    index1 = 0
    cgm_dot = []
    while(index1 < len(glucose) - 2):
        g1 = glucose[index1]
        g2 = glucose[index1+1] 
        g3 = glucose[index1+2]
        val = (g1 + g3 - (2 * g2))/2
        cgm_dot.append(round(val,2))
        index1 = index1 + 1

    peaks_positives, ph = scipy.signal.find_peaks(cgm_dot, height = .1)
    cgm_dot_neg = [ -x for x in cgm_dot]
    peaks_negatives, nh = scipy.signal.find_peaks(cgm_dot_neg, height = .1)
    dict1 = {}
    pos_heights = ph['peak_heights'].tolist()
    neg_heights = nh['peak_heights'].tolist()
    index2 = 0
    while(index2 < len(peaks_positives)):
        dict1[peaks_positives[index2]] = pos_heights[index2]
        index2 = index2 + 1
    index3 = 0
    while(index3 < len(peaks_negatives)):
        dict1[peaks_negatives[index3]] = neg_heights[index3]
        index3 = index3 + 1
    od = OrderedDict(sorted(dict1.items()))
    list1 = []
    list2 = []
    for key in od:
        list1.append(key)
        list2.append(od[key])
    dict2 = {}
    index = 0
    distance  = 0
    while(index < len(list1) - 1):
        distance =  (list1[index] + list1[index+1])/2
        dict2[distance] = list2[index] + list2[index+1]
        index = index + 1
    result = []
    sorted_x = OrderedDict(sorted(dict2.items(), key=operator.itemgetter(1), reverse=True))
    count = 0
    for key in (sorted_x):
        if(count == 3):
            break
        result.append((sorted_x)[key])
        result.append(key)
        count = count + 1
    return result

def f4(g):
    fft_vales_imaginary = fft(g)
    magnitures = []
    for x in fft_vales_imaginary:
        magnitures.append(round(abs(x),2))
    a = list(set(magnitures))
    a.sort()
    a = a[::-1][1:4]
    return a

def extract_feature_for_meal_data(time_stamps , cgm_data):
  m = []
  for x in time_stamps:
    start_time = x[0]
    end_time = x[1]
    mask = (cgm_data['datetime'] > start_time) & (cgm_data['datetime'] <= end_time)
    in_range_df = cgm_data.loc[mask]
    in_range_df = cgm_data.loc[mask]
    in_range_df.reset_index(drop=True, inplace=True)
    index = 0
    glucose = []
    while(index < len(in_range_df)):
        glucose.append(in_range_df['Sensor Glucose (mg/dL)'].iloc[index])
        index = index + 1
    if(in_range_df['Sensor Glucose (mg/dL)'].isna().sum() > 0):
        continue
    if(len(glucose) < 30):
        continue
    f = f2(glucose)
    if(len(f) < 6):
        continue
    result = [f1(glucose)] + f + [f3(glucose)] + f4(glucose) + [1]
    m.append(result)
  return m


def extract_feature_for_no_meal_data(time_stamps , cgm_data):
  m = []
  for x in time_stamps:
    start_time = x[0]
    end_time = x[1]
    mask = (cgm_data['datetime'] > start_time) & (cgm_data['datetime'] <= end_time)
    in_range_df = cgm_data.loc[mask]
    in_range_df = cgm_data.loc[mask]
    in_range_df.reset_index(drop=True, inplace=True)
    index = 0
    glucose= []
    while(index < len(in_range_df)):
        glucose.append(in_range_df['Sensor Glucose (mg/dL)'].iloc[index])
        index = index + 1
    if(in_range_df['Sensor Glucose (mg/dL)'].isna().sum() > 0):
        continue
    if(len(glucose) < 24):
        continue
    f = f2(glucose)
    if(len(f) < 6):
        continue
    result = [f1(glucose)] + f + [f3(glucose)] + f4(glucose) + [0]
    m.append(result)
  return m

f_m_m1 = extract_feature_for_meal_data(meal_data1, cgm_data1)
f_m_n1 = extract_feature_for_no_meal_data(no_meal_data1,cgm_data1)

f_m_m2 = extract_feature_for_meal_data(meal_data2, cgm_data2)
f_m_n2 = extract_feature_for_no_meal_data(no_meal_data2,cgm_data2)

df1 = pd.DataFrame(numpy.concatenate((f_m_m1,f_m_n1), axis=0))
df2 = pd.DataFrame(numpy.concatenate((f_m_m2,f_m_n2), axis=0))
main_feature_matrix_dataframe1 = df1.loc[1:len(f_m_m1)*2]
main_feature_matrix_dataframe2 = df2.loc[1:len(f_m_m2)*2]


main_dataframe = pd.concat([df1, df2])
main_dataframe_without_label = main_dataframe.iloc[: , :-1]

scalar = StandardScaler()
scalar.fit(main_dataframe_without_label)
data = scalar.transform(main_dataframe_without_label)

pca = PCA(n_components = 4)
pca.fit(data)
x = pca.transform(data)

y = main_dataframe.iloc[:,-1:].values.ravel()


scores = []
algo = KFold(n_splits=10,shuffle=True)
for train_index, test_index in algo.split(x):
    X_train, X_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model = svm.SVC(gamma='scale')
    model.fit(X_train,y_train)
    score = model.score(X_test,y_test)
    scores.append(score)
joblib.dump(model, 'model.pkl') 