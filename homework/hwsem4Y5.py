import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('BTC_data.csv')
a=list(df['time'])
b=[]
c=list(df['close'])
print(str(a[1])[0:9])
for i in range (len(a)):
    b.append(str(a[i])[0:9])
plt.figure(figsize=(8,5), dpi=100)
plt.plot(b,c)
plt.show()
plt.savefig('BTC.png', dpi=300)
