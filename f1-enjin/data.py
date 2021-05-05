import pandas as pd
import re

numbers= pd.read_csv('2020_5_20.csv')

# print (numbers[['time','constructor']])

honda= numbers[numbers.values  == "honda"]
renault= numbers[numbers.values  == "renault"]
ferrari= numbers[numbers.values  == "ferrari"]
mercedes= numbers[numbers.values  == "mercedes"]


hon_csv= honda.to_csv(index=False)
ren_csv= renault.to_csv(index=False)
fer_csv= ferrari.to_csv(index=False)
mer_csv= mercedes.to_csv(index=False)

mer_avg= mercedes['time(sec)'].sum() / (6*84600)
hon_avg= honda['time(sec)'].sum() /(4*84600) 
ren_avg= renault['time(sec)'].sum() /(4*84600)
fer_avg= ferrari['time(sec)'].sum() /(6*84600)



mer_avg= '{0:.6f}'.format(mer_avg)
hon_avg= '{0:.6f}'.format(hon_avg)
ren_avg= '{0:.6f}'.format(ren_avg)
fer_avg= '{0:.6f}'.format(fer_avg)


mer= str(mer_avg).replace('.','')
hon = str(hon_avg).replace('.','')
ren = str(ren_avg).replace('.','')
fer = str(fer_avg).replace('.','')


result = ''
while mer:
    result += mer[:2]
    if len(mer) > 3:
        result += ':'
    mer = mer[2:]

print("average mercedes engine speed  " +result)



result = ''
while fer:
    result += fer[:2]
    if len(fer) > 3:
        result += ':'
    fer = fer[2:]

print("average ferrari engine speed  " +result)


result = ''
while hon:
    result += hon[:2]
    if len(hon) > 3:
        result += ':'
    hon = hon[2:]

print("average honda engine speed " +result)



result = ''
while ren:
    result += ren[:2]
    if len(ren) > 3:
        result += ':'
    ren = ren[2:]

print("average renault engine speed " +result)