import matplotlib.pyplot as plt
import numpy as np

lines = []
class Perceptron:
  def __init__(self, num_inputs=3, weights=[1,1,0]):
    self.num_inputs = num_inputs
    self.weights = weights
    
  def weighted_sum(self, inputs):
    weighted_sum = 0
    for i in range(self.num_inputs):
      weighted_sum += self.weights[i]*inputs[i]
    return weighted_sum
  
  def activation(self, weighted_sum):
    if weighted_sum >= 0:
      return 1
    if weighted_sum < 0:
      return -1
    
  def training(self, training_set):
    foundLine = False
    while not foundLine:
      total_error = 0
      for inputs in training_set:
        prediction = self.activation(self.weighted_sum(inputs))
        actual = training_set[inputs]
        error = actual - prediction
        total_error += abs(error)
        for i in range(self.num_inputs):
          self.weights[i] += error*inputs[i]
          
      slope = -self.weights[0]/self.weights[1]
      intercept = -self.weights[2]/self.weights[1]
      y1 = (slope * 0) + intercept
      y2 = (slope * 50) + intercept
      lines.append([[0,50], [y1, y2]])
      
      if total_error == 0:
        foundLine = True
      return slope, intercept
      
training_set = {(2,1,0): -1, (3,2,0):-1, (1,3,0): 1, (3,4,0): 1}

x_plus = []
y_plus = []
x_minus = []
y_minus = []

for data in training_set:
    if training_set[data] == 1:
      x_plus.append(data[0])
      y_plus.append(data[1])
    elif training_set[data] == -1:
      x_minus.append(data[0])
      y_minus.append(data[1])
    
perceptron = Perceptron()
for i in range(10):
    perceptron.training(training_set)
    
fig = plt.figure()
ax = plt.axes(xlim=(0, 5), ylim=(0, 5))
line, = ax.plot([], [], lw=2)

plt.scatter(x_plus, y_plus, marker = '+', c = 'green', s = 128, linewidth = 2)
plt.scatter(x_minus, y_minus, marker = '_', c = 'red', s = 128, linewidth = 2)

f = lambda x: lines[0]*x + lines[1]
x = np.array([0,100])
plt.plot(x,f(x),lw=2.5)
plt.show()
