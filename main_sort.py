from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle, Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import math

def hex_to_rgb(hex_color):
    return int(hex_color[1:3],16), int(hex_color[3:5],16),int(hex_color[5:7],16), 255

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Solar System Simulation")
        self.batch = Batch()
        self.x=[3,4,2,1,5]
        self.bars=[]
        for e,i in enumerate(self.x):
            self.bars.append(Rectangle(100+e*100,100,80,i*100, batch=self.batch))

    def on_update(self, deltatime):
        n = len(self.x)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.x[j] > self.x[j+1]:
                    self.x[j], self.x[j+1] = self.x[j+1], self.x[j]
                    self.bars=[]
                    for e,i in enumerate(self.x):
                        self.bars.append(Rectangle(100+e*100,100,80,i*100, batch=self.batch))
                    return
        

    def on_draw(self):
        self.clear()
        self.batch.draw()


renderer = Renderer()
clock.schedule_interval(renderer.on_update, 3)
run()