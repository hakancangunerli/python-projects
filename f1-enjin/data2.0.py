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


mer= str(mer_avg).replace('.', '')
hon = str(hon_avg).replace('.','')
ren = str(ren_avg).replace('.','')
fer = str(fer_avg).replace('.','')

def test(x):
    result = ''
    while x:
        result += x[:2]
        if len(x) > 3:
            result += ':'
        x = x[2:]
    print(result)

test(mer)
test(hon)
test(ren)
test(fer)