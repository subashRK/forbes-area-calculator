from temp_time import old_temp_times_x, old_temp_times_y, spline as _spline
from temp_gradient import temp_gradients_x, temp_gradients_y
from matplotlib import pyplot
from scipy.interpolate import make_interp_spline
import numpy

INTERVALS = 500

def closest_index(target, array):
  diff_arr = [abs(target - i) for i in array]
  return diff_arr.index(min(diff_arr))

derivatives_spline = _spline.derivative(1)

# X and Y values before Interpolation
x_values = [temp_gradients_x[closest_index(y, temp_gradients_y)] for y in old_temp_times_y]
y_values = [derivatives_spline(old_temp_times_x[i]) * -1 for i in range(0, len(old_temp_times_x))]

spline = make_interp_spline(x_values, y_values, k=2)

# X and Y values after Interpolation
x_values = numpy.linspace(x_values[0], x_values[-1], endpoint=True, num=INTERVALS)
y_values = spline(x_values)

area = sum(y_values) * (x_values[1] - x_values[0])

pyplot.plot(x_values, y_values)
pyplot.bar(x_values, y_values)
pyplot.show()

print("The Area is: ", area)
