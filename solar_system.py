## add moons
from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle
from pyglet.graphics import Batch
from pyglet import clock
import math

def hex_to_rgb(hex_color):
    return int(hex_color[1:3],16), int(hex_color[3:5],16),int(hex_color[5:7],16), 255

class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Solar System Simulation")
        self.batch = Batch()
        self.sun = Circle(320,320,25, color=hex_to_rgb('#F9F871'),
        batch=self.batch)
        self.planets=[
            (70,0.4,Circle(390,320,7, color=hex_to_rgb('#FACCFF'),batch=self.batch),[]), # venus
            (100,0.3,Circle(420,320,10, color=hex_to_rgb('#00D2FC'),batch=self.batch),[
                (15,1.5,Circle(0,0,3, color=hex_to_rgb('#999999'), batch=self.batch)),
            ]), # earth
            (140,0.2,Circle(460,320,6, color=hex_to_rgb('#C34A36'),batch=self.batch),[
                (12,1.5,Circle(0,0,2, color=hex_to_rgb('#999999'), batch=self.batch)),
                (14,1.2,Circle(0,0,2, color=hex_to_rgb('#999999'), batch=self.batch)),
            ]), # mars
            (280,0.1,Circle(600,320,16, color=hex_to_rgb('#FFc75F'),batch=self.batch),[
                (24,1.5,Circle(0,0,4, color=hex_to_rgb('#999999'), batch=self.batch)),
                (30,1.2,Circle(0,0,3, color=hex_to_rgb('#999999'), batch=self.batch)),
                (35,0.9,Circle(0,0,2, color=hex_to_rgb('#999999'), batch=self.batch)),
                (42,0.8,Circle(0,0,5, color=hex_to_rgb('#999999'), batch=self.batch)),
            ]) # jupiter
        ]
        self.angle = 0

    def on_update(self, deltatime):
        self.angle += deltatime
        for distance, speed, planet_circle, moons in self.planets:
            planet_circle.x = 320 + distance * math.cos(self.angle * speed)
            planet_circle.y = 320 + distance * math.sin(self.angle * speed)
        for distance, speed, moon_circle in moons:
            moon_circle.x = planet_circle.x + distance * math.cos(self.angle *speed)
            moon_circle.y = planet_circle.y + distance * math.sin(self.angle *speed)

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1/60)
run()