from __future__ import division
import pandas as pd
import datetime as datetime



from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


from sklearn.externals import joblib


from scipy.signal import find_peaks
from collections import OrderedDict
import operator
import scipy


import matplotlib.pyplot as plt
from scipy.fftpack import fft


def f1(glucose):
    return max(glucose) - min(glucose)

def f3(glucose):
    min1= glucose.index(min(glucose))
    max1 = glucose.index(max(glucose))
    return (max1 - min1)

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

df = pd.read_csv("test.csv", header=None)

df_list = df.values.tolist()
matrix = []
for innerlist in df_list:
   matrix.append([f1(innerlist)] + f2(innerlist) + [f3(innerlist)] + f4(innerlist))

scalar = StandardScaler()
scalar.fit(matrix)
data = scalar.transform(matrix)

pca = PCA(n_components = 4)
pca.fit(data)
x = pca.transform(data)



model = joblib.load('model.pkl')
predictions = model.predict(x)

df = pd.DataFrame(predictions)
df.to_csv('Results.csv', header=False, index=False)



