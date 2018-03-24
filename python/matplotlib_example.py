import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))

plt.plot(x, np.cos(x))

plt.show()

# squares = [1, 4, 9, 16, 25]
# plt.plot(squares)


x_values = list(range(1,1001))

y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=20)

plt.axis([0,1100,0,1100000])
plt.show()

from random import choice
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

class RondomWalk():

    def __init__(self, num_points=50000):

        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values)  < self.num_points:
            
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step


            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw = RondomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues, edgecolor='none', s=1)
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)

plt.show()


from random import randint
import pygal

class Die():

    def __init__(self,num_sides=6):

        self.num_sides = num_sides

    def roll(self):

        return randint(1,self.num_sides)


die = Die()
results = []

for roll_num in range(10000):
    result = die.roll()
    results.append(result)

frequencies = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title = 'results of rollling one d6 1000 times'
hist.x_labels = [1,2,3,4,5,6]
hist.x_title = 'results'
hist.y_title = 'frequency of result'

hist.add('D6',frequencies)
hist.render_to_file('die2.svg')
