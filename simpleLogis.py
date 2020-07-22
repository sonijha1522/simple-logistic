from scipy.stats import norm
from matplotlib import pyplot
import pandas as pd
import math
import csv
df = pd.read_csv('temp_data.csv')
x = df['Temp']
y = df['Response']
pyplot.scatter(x, y)
len1 = len(x)
sum1 = 0
sum2 = 0
# define distribution parameters
for counter in range(0,len1):
 sum1 = sum1 + x[counter]

mean = sum1/len1
print("mean=", mean)

for counter1 in range(0, len1):
 sum2 = sum2 + (x[counter1] - mean)**2
print("sqar_v=", sum2)

stand_d = math.sqrt(sum2/len1)
print("standard deviation=",stand_d)

#sigma = stand_d = 2.87
# create distribution
dist = norm(mean, stand_d)
# plot pdf
values = [value for value in range(41, 50)]
probabilities = [dist.pdf(value) for value in values]
pyplot.plot(values, probabilities)

# plot cdf
cprobs = [dist.cdf(value) for value in values]
pyplot.plot(values, cprobs)
pyplot.xlabel('x axis in temp')

pyplot.show()




