import csv
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import mpld3


df = pd.read_csv('../csv/INFY.BO.csv', index_col = 0)
#print(df.iat[0,0])


a0=df.iat[0,0]
b0=df.iat[1,0]


a1=df.iat[0,1]
b1=df.iat[1,1]

a2=df.iat[0,2]
b2=df.iat[1,2]


a3=df.iat[0,3]
b3=df.iat[1,3]

a4=df.iat[0,4]
b4=df.iat[1,4]

a5=df.iat[0,5]
b5=df.iat[1,5]


length=len(df)
count=0
valop=[]
valclose=[]
print("3_Day_Open_Simple_MOV,3_Day_High_Simple_MOV,3_Day_Low_Simple_MOV,3_Day_Adj_Close_Simple_MOV,3_Day__Close,3_Day_Volume_Simple_MOV")

for i in range(2,length):
    c0=df.iat[i,0]
    c1=df.iat[i,1]
    c2=df.iat[i,2]
    c3=df.iat[i,3]
    c4=df.iat[i,4]
    c5=df.iat[i,5]
	
    val0=(a0+b0+c0)/3
    val1=(a1+b1+c1)/3
    val2=(a2+b2+c2)/3
    val3=(a3+b3+c3)/3
    val4=(a4+b4+c4)/3
    val5=(a5+b5+c5)/3
	
	
    a0=b0
    b0=c0

    a1=b1
    b1=c1
	
    a2=b2
    b2=c2

    a3=b3
    b3=c3

    a4=b4
    b4=c4

    a5=b5
    b5=c5
    valop.append(val0);valclose.append(val3);print(str(val0)+","+str(val1)+","+str(val2)+","+str(val3)+","+str(val4)+","+str(val5))

# fields = ['opening','closing','Volume']
# rows=[]
# volume=[]
# volume = df.Volume.values
# for i in range(len(valop)):
#     rows.append([valop[i],valclose[i],volume[i]])

# with open('Infosys', 'w') as f: 
      
#     # using csv.writer method from CSV package 
#     write = csv.writer(f) 
#     write.writerow(fields) 
#     write.writerows(rows) 

fig=plt.figure(figsize=(24, 13))
plt.subplot(1,2,1)
plt.plot(df.Open.values, color='red', label='open')
plt.plot(df.Close.values, color='green', label='close')
plt.plot(df.Low.values, color='pink', label='low')
plt.plot(df.High.values, color='orange', label='high')
plt.plot(valclose, color='blue', label='movavg_close')

plt.title('stock prices')
plt.xlabel('time [days]')
plt.ylabel('price')
plt.legend(loc='best')
#plt.show()

plt.subplot(1,2,2)
plt.plot(df.Volume.values, color='black', label='volume')
plt.title('stock volume')
plt.xlabel('time [days]')
plt.ylabel('volume')
plt.legend(loc='best')

html_str = mpld3.fig_to_html(fig)
Html_file= open("infosys.html","w")
Html_file.write(html_str)
Html_file.close()

