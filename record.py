import datetime as dt
from datetime import datetime 


import pickle
def save_obj(obj, name ):
    with open('./'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('./' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
print("date and time =", dt_string)

weight_dict = load_obj("weight_dict")
record_time = dt.datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')
weight_dict[record_time]=49.0 # Modify here and run once to record a new weight

save_obj(weight_dict, "weight_dict")
