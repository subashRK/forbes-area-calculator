import csv
from matplotlib import pyplot
from scipy.interpolate import make_interp_spline
import numpy

temp_times_x = []
temp_times_y = []

with open("./temp_time.csv", "r") as temp_t_f:
  reader = csv.reader(temp_t_f, skipinitialspace=True)

  for row in reader:
    temp_times_x.append(float(row[0]))
    temp_times_y.append(float(row[1]))


old_temp_times_x = temp_times_x
old_temp_times_y = temp_times_y

spline = make_interp_spline(temp_times_x, temp_times_y, k = 2) # returns a function which gives the interpolated values for the array passed
temp_times_x = numpy.linspace(temp_times_x[0], temp_times_x[-1], endpoint=True)
temp_times_y = spline(temp_times_x)

# print(spline(30))

if __name__ == "__main__":
  pyplot.plot(temp_times_x, temp_times_y)
  pyplot.show()
