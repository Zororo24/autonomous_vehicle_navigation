# Self Driving Car

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# Importing the Kivy packages
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

# Importing the Dqn object from our AI in ai.py
from ai import Dqn
from ai1 import Dqn1

# Adding this line if we don't want the right click to put a red point
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Introducing last_x and last_y, used to keep the last point in memory when we draw the sand on the map
last_x = 0
last_y = 0
n_points = 0
length = 0

# Getting our AI, which we call "brain", and that contains our neural network that represents our Q-function
brain = Dqn(5,3,0.9)
brain1 = Dqn1(5,3,0.85)
action2rotation = [0,20,-20]
last_reward = 0
last_reward1 = 0
scores = []
scores1 = []

# Initializing the map
first_update = True
def init():
    global sand
    global goal_x
    global goal_y
    global first_update
    sand = np.zeros((longueur,largeur))
    goal_x = 20
    goal_y = largeur - 20
    first_update = False

first_update1 = True
def init1():
    global sand
    global goal_x1
    global goal_y1
    global first_update1
    sand = np.zeros((longueur,largeur))
    goal_x1 = 20
    goal_y1 = 20
    first_update1 = False

# Initializing the last distance
last_distance = 0
last_distance1 = 0

# Creating the car class

class Car(Widget):
    
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)

    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos
        self.rotation = rotation
        self.angle = self.angle + self.rotation
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
            self.signal1 = 1.
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            self.signal2 = 1.
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3 = 1.

class Car1(Widget):
    
    angle = NumericProperty(0)
    rotation1 = NumericProperty(0)
    velocity_x1 = NumericProperty(0)
    velocity_y1 = NumericProperty(0)
    velocity1 = ReferenceListProperty(velocity_x1, velocity_y1)
    sensor1_x1 = NumericProperty(0)
    sensor1_y1 = NumericProperty(0)
    sensor11 = ReferenceListProperty(sensor1_x1, sensor1_y1)
    sensor2_x1 = NumericProperty(0)
    sensor2_y1 = NumericProperty(0)
    sensor21 = ReferenceListProperty(sensor2_x1, sensor2_y1)
    sensor3_x1 = NumericProperty(0)
    sensor3_y1 = NumericProperty(0)
    sensor31 = ReferenceListProperty(sensor3_x1, sensor3_y1)
    signal11 = NumericProperty(0)
    signal21 = NumericProperty(0)
    signal31 = NumericProperty(0)

    def move1(self, rotation1):
        self.pos = Vector(*self.velocity1) + self.pos
        self.rotation1 = rotation1
        self.angle = self.angle + self.rotation1
        self.sensor11 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor21 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor31 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal11 = int(np.sum(sand[int(self.sensor1_x1)-10:int(self.sensor1_x1)+10, int(self.sensor1_y1)-10:int(self.sensor1_y1)+10]))/400.
        self.signal21 = int(np.sum(sand[int(self.sensor2_x1)-10:int(self.sensor2_x1)+10, int(self.sensor2_y1)-10:int(self.sensor2_y1)+10]))/400.
        self.signal31 = int(np.sum(sand[int(self.sensor3_x1)-10:int(self.sensor3_x1)+10, int(self.sensor3_y1)-10:int(self.sensor3_y1)+10]))/400.
        if self.sensor1_x1>longueur-10 or self.sensor1_x1<10 or self.sensor1_y1>largeur-10 or self.sensor1_y1<10:
            self.signal11 = 1.
        if self.sensor2_x1>longueur-10 or self.sensor2_x1<10 or self.sensor2_y1>largeur-10 or self.sensor2_y1<10:
            self.signal21 = 1.
        if self.sensor3_x1>longueur-10 or self.sensor3_x1<10 or self.sensor3_y1>largeur-10 or self.sensor3_y1<10:
            self.signal31 = 1.

class Ball1(Widget):
    pass
class Ball2(Widget):
    pass
class Ball3(Widget):
    pass

class Ball11(Widget):
    pass
class Ball12(Widget):
    pass
class Ball13(Widget):
    pass

# Creating the game class

class Game(Widget):

    car = ObjectProperty(None)
    car1 = ObjectProperty(None)
    ball1 = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    ball3 = ObjectProperty(None)
    ball11 = ObjectProperty(None)
    ball12 = ObjectProperty(None)
    ball13 = ObjectProperty(None)

    def serve_car(self):
        self.car.center = self.center
        self.car.velocity = Vector(6, 0)
    def serve_car1(self):
        self.car1.center = self.center
        self.car1.velocity = Vector(6, 0)

    def update(self, dt):

        global brain
        global last_reward
        global scores
        global last_distance
        global goal_x
        global goal_y
        global brain1
        global last_reward1
        global scores1
        global last_distance1
        global goal_x1
        global goal_y1
        global longueur
        global largeur

        longueur = self.width
        largeur = self.height
        if first_update:
            init()

        xx = goal_x - self.car.x
        yy = goal_y - self.car.y
        orientation = Vector(*self.car.velocity).angle((xx,yy))/180.
        last_signal = [self.car.signal1, self.car.signal2, self.car.signal3, orientation, -orientation]
        action = brain.update(last_reward, last_signal)
        scores.append(brain.score())
        rotation = action2rotation[action]
        self.car.move(rotation)
        distance = np.sqrt((self.car.x - goal_x)**2 + (self.car.y - goal_y)**2)
        self.ball1.pos = self.car.sensor1
        self.ball2.pos = self.car.sensor2
        self.ball3.pos = self.car.sensor3

        if sand[int(self.car.x),int(self.car.y)] > 0:
            self.car.velocity = Vector(1, 0).rotate(self.car.angle)
            last_reward = -1
        else: # otherwise
            self.car.velocity = Vector(6, 0).rotate(self.car.angle)
            last_reward = -0.2
            if distance < last_distance:
                last_reward = 0.1

        if self.car.x < 10:
            self.car.x = 10
            last_reward = -1
        if self.car.x > self.width - 10:
            self.car.x = self.width - 10
            last_reward = -1
        if self.car.y < 10:
            self.car.y = 10
            last_reward = -1
        if self.car.y > self.height - 10:
            self.car.y = self.height - 10
            last_reward = -1

        if distance < 100:
            goal_x = self.width-goal_x
            goal_y = self.height-goal_y
        last_distance = distance
        
        if first_update1:
            init1()
        
        xx1 = goal_x1 - self.car1.x
        yy1 = goal_y1 - self.car1.y
        orientation1 = Vector(*self.car1.velocity1).angle((xx1,yy1))/180.
        last_signal1 = [self.car1.signal11, self.car1.signal21, self.car1.signal31, orientation1, -orientation1]
        action1 = brain1.update(last_reward1, last_signal1)
        scores1.append(brain1.score())
        rotation1 = action2rotation[action1]
        self.car1.move1(rotation1)
        distance1 = np.sqrt((self.car1.x - goal_x1)**2 + (self.car1.y - goal_y1)**2)
        self.ball11.pos = self.car1.sensor11
        self.ball12.pos = self.car1.sensor21
        self.ball13.pos = self.car1.sensor31

        if sand[int(self.car1.x),int(self.car1.y)] > 0:
            self.car1.velocity1 = Vector(1, 0).rotate(self.car1.angle)
            last_reward1 = -1
        else: # otherwise
            self.car1.velocity1 = Vector(6, 0).rotate(self.car1.angle)
            last_reward1 = -0.2
            if distance1 < last_distance1:
                last_reward1 = 0.1

        if self.car1.x < 10:
            self.car1.x = 10
            last_reward1 = -1
        if self.car1.x > self.width - 10:
            self.car1.x = self.width - 10
            last_reward1 = -1
        if self.car1.y < 10:
            self.car1.y = 10
            last_reward1 = -1
        if self.car1.y > self.height - 10:
            self.car1.y = self.height - 10
            last_reward1 = -1

        if distance < 100:
            goal_x1 = self.width-goal_x1
            goal_y1 = self.height-goal_y1
        last_distance1 = distance1

# Adding the painting tools

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        global length, n_points, last_x, last_y
        with self.canvas:
            Color(0.8,0.7,0)
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
            last_x = int(touch.x)
            last_y = int(touch.y)
            n_points = 0
            length = 0
            sand[int(touch.x),int(touch.y)] = 1

    def on_touch_move(self, touch):
        global length, n_points, last_x, last_y
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
            x = int(touch.x)
            y = int(touch.y)
            length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
            n_points += 1.
            density = n_points/(length)
            touch.ud['line'].width = int(20 * density + 1)
            sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1
            last_x = x
            last_y = y

# Adding the API Buttons (clear, save and load)

class CarApp(App):

    def build(self):
        parent = Game()
        parent.serve_car()
        parent.serve_car1()
        Clock.schedule_interval(parent.update, 1.0/60.0)
        self.painter = MyPaintWidget()
        clearbtn = Button(text = 'clear', size=(50,35))
        savebtn = Button(text = 'save', pos = (51, 0), size=(50,35))
        loadbtn = Button(text = 'load', pos = (102, 0), size=(50,35))
        #erasebtn = Button(text = 'erase', pos = (153, 0), size=(50,35))
        #drawbtn = Button(text = 'draw', pos = (204, 0), size=(50,35))
        clearbtn.bind(on_release = self.clear_canvas)
        savebtn.bind(on_release = self.save)
        loadbtn.bind(on_release = self.load)
        #erasebtn.bind(on_release=self.erase_canvas)
        #drawbtn.bind(on_release=self.draw_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(savebtn)
        parent.add_widget(loadbtn)
        #parent.add_widget(erasebtn)
        return parent

    def clear_canvas(self, obj):
        global sand
        self.painter.canvas.clear()
        sand = np.zeros((longueur,largeur))

    def save(self, obj):
        print("saving brain...")
        brain.save()
        brain1.save()
        plt.plot(scores)
        plt.plot(scores1)
        plt.show()

    def load(self, obj):
        print("loading last saved brain...")
        brain.load()
        brain1.load()
        
    def erase_canvas(self, obj):
        global sand
        self.painter.canvas.erase()
        sand = np.zeros((longueur,largeur))

# Running the whole thing
if __name__ == '__main__':
    CarApp().run()
    
