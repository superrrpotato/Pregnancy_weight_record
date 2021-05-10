import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

import numpy as np
init_weight = 47.0
first_recording_date_after_pregnant = 37
fluctuation_factor = 0.3


list_of_datetimes = list(weight_dict.keys())
rank = np.argsort(list_of_datetimes)
x = [list(weight_dict.keys())[i] for i in rank]
y = [list(weight_dict.values())[i] for i in rank]
estimate_weight = []
for index,i in enumerate(x):
    if float((i-x[0]).days+37) < 84:
        estimate_weight += [47 + float((i-x[0]).days+37)/(7*12)*2]
    else:
        estimate_weight += [(49 + float((i-x[0]).days+37-7*12)/(7*5)*2)]
estimate_weight = np.array(estimate_weight)
y1 = estimate_weight+0.3*(estimate_weight-47)
y2 = estimate_weight-0.3*(estimate_weight-47)
xx = mdates.date2num([datetime(2021, 1, 11, 12, 10, 28)]+x)
yy = [47.2]+y

coef = np.polyfit(xx, yy, 3)
y_fit = np.polyval(coef, xx)[1:]
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(x, y,marker='+',c='r',label='True weight')
plt.plot(x,estimate_weight, c='black', label='Recommend')
plt.plot(x,y_fit,marker='+',label='X^2 poly fit')
plt.legend(fontsize=fontsize)
plt.plot(x, y1,'--',c='gray')
plt.plot(x, y2,'--',c='gray')
plt.fill_between(x, y1, y2,alpha=.2,color='gray')
plt.xlabel('datetime',fontsize=fontsize)
plt.ylabel('weight/kg',fontsize=fontsize)
plt.xticks(rotation=90,fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.title('GYS weight record',fontsize=fontsize)
plt.subplot(1,2,2)
plt.title('Weight gap',fontsize=fontsize)
plt.plot(x,y_fit-estimate_weight, marker='+',label='X^2 poly fit gap')
plt.plot(x,y-estimate_weight,marker='+',c='r',label='True weight gap')
plt.plot(x,estimate_weight-estimate_weight, c='black', label='Recommend')
plt.plot(x, y1-estimate_weight,'--',c='gray')
plt.plot(x, y2-estimate_weight,'--',c='gray')
plt.fill_between(x, y1-estimate_weight, y2-estimate_weight,alpha=.2,color='gray')
plt.xlabel('datetime',fontsize=fontsize)
plt.ylabel('weight difference/kg',fontsize=fontsize)
plt.xticks(rotation=90,fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.legend(fontsize=fontsize)
