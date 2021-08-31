

import bpy
import os
import math
import threading
import time
from math import radians

bpy.data.objects['Cube'].select_set(True) # Blender 2.8x

bpy.ops.object.delete()
context = bpy.context

models_path = "C:/Users/willi/OneDrive/Documents/CAD Files/Simple Rocket"
render_path = "C:/Users/willi/OneDrive/Documents/CAD Files/Simple Rocket"
os.path.isdir(models_path)

models = "Full.obj"

class AnimationThread(threading.Thread):
    def __init__(self, function_that_animates):
        threading.Thread.__init__(self)
        self.runnable = function_that_animates
    def run(self):
        self.runnable()

def UpdateAngle(a,b,c):
    bpy.data.objects[models.split('.')[0]].rotation_euler = (a,b,c)

def simpleAnimation():
    for x in range(100):
        UpdateAngle(x/2, 0, 0)
        time.sleep(0.05)

#create a scene

scene = bpy.context.view_layer
camera_data = bpy.data.cameras.new("Camera")


# do the same for lights etc
scene.update()
path = os.path.join(models_path, models)
rocket = bpy.ops.import_scene.obj(filepath=path, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl")
thread = AnimationThread(simpleAnimation)
thread.start()
