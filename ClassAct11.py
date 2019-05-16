import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("mpg.csv")

data["liters"] = (round(data['displacement'] / 61.024, 1))

usa = data[data.origin == "usa"]
japan = data[data.origin =="japan"]

corr = data.corr()['mpg'][:]
print (corr)
print ('As you can see displacement, wieght and liters have a strong negative correlation with the Miles Per Galon a car has')

print (data)

usa = usa.sort_values(['mpg'])
japan = japan.sort_values(['mpg'])
plt.plot(usa['mpg'], usa['liters'])
plt.plot(japan['mpg'], japan['liters'])
plt.legend(['USA', 'JAPAN'])
plt.xlabel('Miles Per Gallon')
plt.ylabel('Car Liter')
plt.title('JAPAN vs USA in MPG')
plt.show()

#As you can see Japan's cars have lower liter amount and because of that they have higher fuel efficiency towards USA Cars
#Because USA cars have more Liters (Displacement) Than Japan cars

usa = usa.sort_values(['mpg','weight'])
japan = japan.sort_values(['mpg','weight'])
plt.plot(usa['mpg'], usa['weight'])
plt.plot(japan['mpg'], japan['weight'])
plt.legend(['USA', 'JAPAN'])
plt.xlabel('Miles Per Gallon')
plt.ylabel('WEIGHT')
plt.title('JAPAN vs USA in MPG according to weight')
plt.show()

# Here you can see the higher the Cars weight the lower MPG the car gets and Japan's cars weigh lower overall so in return
# their cars have better MPG than USA cars, but there is some outliers.. With the previous graph we also saw the more liters
# a car has the less MPG a car has.. So this show us that car producers want to balance weight and Liters to get better
# MPG than other car makers

