import pandas as pd

train_interval = 10
miss_cost = 100
total_min = 400

data = pd.read_csv('data_sahand.csv')
data = data.drop('Unnamed: 0', axis=1)

s=1
def distance(entered_station, exited_station, speed):
    time = [0,5,4,3]
    newtime=[]
    for timechange in time:
        newtime.append(timechange/speed)
        
    return sum(newtime[entered_station : exited_station])
  
    

inc_wait = []
time = []
for i in range(len(data)):
    temp = data['time entered'][i] %  train_interval
    if data['time entered'][i] < (total_min - train_interval):
        wait = train_interval - temp
    else:
        wait = miss_cost
    metro_travel_time = distance(data['station entered'][i],data['station exited'][i], s)
    inc_wait.append(wait+metro_travel_time)
    time.append(metro_travel_time)
    
    

data.insert(3, "include wait time", inc_wait, True)
data.insert(3, "metro travel time", time, True)

people = list (range(1,len (data)+1))
data.insert(3, "people", people, True)




data.plot(x="people", 
          y=["include wait time", "metro travel time"], 
          kind="bar",
          figsize=(20, 8)) 

'''
plt.bar(people, time, color ='maroon', 
        width = 0.4, )
        #bottom = data['time entered'])
 
plt.xlabel("People")
plt.ylabel("Time")
plt.title("Time spent on commute")
plt.show()
'''