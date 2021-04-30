import matplotlib.pyplot as plt
import matplotlib
import numpy as np

import pickle
def save_obj(obj, name ):
    with open('./'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('./' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
      
weight_dict = load_obj("weight_dict")

init_weight = 47.0
first_recording_date_after_pregnant = 37
fluctuation_factor = 0.3
list_of_datetimes = list(weight_dict.keys())
rank = np.argsort(list_of_datetimes)
x = [list(weight_dict.keys())[i] for i in rank]
y = [list(weight_dict.values())[i] for i in rank]
estimate_weight = []
for index,i in enumerate(x):
    if float((i-x[0]).days+first_recording_date_after_pregnant) < 12*7:
        estimate_weight += [init_weight + float((i-x[0]).days+37)/(7*12)*2]
    else:
        estimate_weight += [(init_weight+2 + float((i-x[0]).days+37-7*12)/(7*5)*2)]
estimate_weight = np.array(estimate_weight)
y1 = estimate_weight+fluctuation_factor*(estimate_weight-init_weight)
y2 = estimate_weight-fluctuation_factor*(estimate_weight-init_weight)
plt.plot(x, y,marker='+',c='r',label='True weight')
plt.plot(x,estimate_weight, c='black', label='Recommend')
plt.legend(fontsize=fontsize)
plt.plot(x, y1,'--',c='gray')
plt.plot(x, y2,'--',c='gray')
plt.fill_between(x, y1, y2,alpha=.2,color='gray')
plt.xlabel('datetime',fontsize=fontsize)
plt.ylabel('weight/(kg)',fontsize=fontsize)
plt.xticks(rotation=90,fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.title('GYS weight record',fontsize=fontsize)
