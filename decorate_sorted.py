from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock

def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

class Renderer(Window):
    colors = ['#FFFFFF', '#C098C8', '#9361E1', '#3A2C88', '#1C0E59']

    def __init__(self):
        super().__init__(640, 640, "Decorate Sorted Simulation")
        self.batch = Batch()
        self.x = [3, 4, 2, 1, 5]
        self.bars = []

        for e, (value, color) in enumerate(zip(self.x, Renderer.colors)):
            rgb_color = hex_to_rgb(color)
            self.bars.append(Rectangle(100 + e*100, 100, 80, value*100, color=rgb_color, batch=self.batch))

    def on_update(self, deltatime):
        n = len(self.x)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.x[j] > self.x[j+1]:
                    self.x[j], self.x[j+1] = self.x[j+1], self.x[j]
                    self.bars = []
                    for e, (value, color) in enumerate(zip(self.x, Renderer.colors)):
                        rgb_color = hex_to_rgb(color)
                        self.bars.append(Rectangle(100 + e*100, 100, 80, value*100, color=rgb_color, batch=self.batch))
                    return

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 3)
run()
