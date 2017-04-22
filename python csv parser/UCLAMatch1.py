import csv
import pandas as pd
import numpy as np
f = open('ucla.csv')

maxDiff = 20

def percentSimilar(x):
    return (maxDiff - x)/maxDiff


dfbase = pd.read_csv(f)

dfbase = dfbase.iloc[:,1:]




dfans = dfbase.iloc[:,3:9]


#prepping the dfcum dataframe
dfcum = pd.DataFrame(0,index = dfbase.iloc[:,0],columns=dfbase.iloc[:,0])
del dfcum.index.name
del dfcum.columns.name

ary = dfans.as_matrix()



for i in range(0,len(ary)):
    for j in range(0,len(ary[0])):
        for k in range(0,len(ary)):
            difference = abs(ary[i][j] - ary[k][j])

            dfcum.iloc[i,k] += difference


dfscore = dfcum.applymap(percentSimilar)

dfbase.index = dfscore.index

dfscore = pd.concat([dfbase['Gender'], dfscore],axis=1)


dfscore.to_csv('export.csv')
dfscore.to_html('export.html')


f.close()
