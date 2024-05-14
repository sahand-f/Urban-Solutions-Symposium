import pandas as pd
import matplotlib.pyplot as plt 

train_interval = 1
miss_cost = 100
total_min = 400

data = pd.read_csv('data_sahand.csv')
data = data.drop('Unnamed: 0', axis=1)

def distance(entered_station, exited_station):
    time = [0,5,4,3]
    return sum(time[entered_station : exited_station])

def metro(interval):
    total_wait = 0
    arrival_time = []
    inc_wait = []
    for i in range(len(data)):
        temp = data['time entered'][i] %  interval
        if data['time entered'][i] < (total_min - interval):
            wait =interval - temp
        else:
            wait = miss_cost
        metro_travel_time = distance(data['station entered'][i],data['station exited'][i])
        arrival_time.append(data['time entered'][i] + metro_travel_time)
        inc_wait.append(wait+metro_travel_time)
    total_wait = sum(inc_wait)
    return total_wait
    

interval = list(range(1,15))

time= []
for x in interval:
    time.append(metro(x))



plt.plot(interval, time, color ='maroon',)
 
plt.xlabel("interval")
plt.ylabel("Time")
plt.title("Time spent on commute")
plt.show()