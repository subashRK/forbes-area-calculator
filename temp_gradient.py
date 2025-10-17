import csv
from matplotlib import pyplot
from scipy.interpolate import make_interp_spline
import numpy

temp_gradients_x = []
temp_gradients_y = []

with open("./temp_gradient.csv", "r") as temp_g_f:
  reader = csv.reader(temp_g_f, skipinitialspace=True)

  for row in reader:
    temp_gradients_x.append(float(row[0]))
    temp_gradients_y.append(float(row[1]))
    
spline = make_interp_spline(temp_gradients_x, temp_gradients_y, k = 2) # returns a function which gives the interpolated values for the array passed
temp_gradients_x = numpy.linspace(temp_gradients_x[0], temp_gradients_x[-1], endpoint=True)
temp_gradients_y = spline(temp_gradients_x)

# print(spline(30))

if __name__ == "__main__":
  pyplot.plot(temp_gradients_x, temp_gradients_y)
  pyplot.show()
