import random
import pandas as pd
import matplotlib.pyplot as plt

data = {'station entered':[],
        'station exited':[],
        'time entered': [],
        }

station_entered = list(range(1,4))
station_exited = list(range(2,5))
time_entered = list(range(1,400))

n_people = 500

for _ in range(n_people):
    en = random.choice(station_entered)
    data['station entered'].append(en)
    data['station exited'].append(random.randint(en+1,4))
    x=random.gauss(90,80)
    while 0 > x or x > 400:
        x=random.gauss(90,100)
    data['time entered'].append(x)
       
train_freq = 10

data = pd.DataFrame(data)
data.to_csv('data_sahand.csv')

# Plotting
plt.figure(figsize=(10, 6))
plt.hist(data['time entered'], bins=40, color='blue', alpha=0.7)
plt.title('Histogram of Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()