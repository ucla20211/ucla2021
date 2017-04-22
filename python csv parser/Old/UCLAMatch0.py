import csv
import pandas as pd
import numpy as np
f = open('ucla.csv')

maxDiff = 20

def percentSimilar(x):
    return (maxDiff - x)/maxDiff


dfbase = pd.read_csv(f)
dfbase.columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

dfbase = dfbase.ix[:,'b':'k']

#because of that first guyette
dfbase = dfbase.set_value(0,'b', "dudette")
dfbase = dfbase.set_value(0,'c',"Female")

dfans = dfbase.ix[:,'d':'k']


#prepping the dfcum dataframe
dfcum = pd.DataFrame(0,index = dfbase['b'],columns=dfbase['b'])
del dfcum.index.name
del dfcum.columns.name

ary = dfans.as_matrix()



for i in range(0,len(ary)):
    for j in range(0,len(ary[0])):
        #print(ary[i][j])
        for k in range(0,len(ary)):
            difference = abs(ary[i][j] - ary[k][j])

            
            #dfcum.set_value(dfcum.columns[i],dfcum.index[j])
            #dfcum[dfcum.columns[i]][dfcum.index[j]] += difference

            
            #dfcum.set_value(dfcum.index[i],dfcum.columns[k],0)

            #dfcum[dfcum.columns[i]][dfcum.index[j]] += difference

            #dfcum.set_value(dfcum.index[i],dfcum.columns[k],dfcum[dfcum.index[i]][dfcum.columns[k]] + difference)

            dfcum.iloc[i,k] += difference


dfscore = dfcum.applymap(percentSimilar)

print(ary)
print(dfcum)
print(dfscore)
dfscore.to_csv('export.csv')



f.close()
