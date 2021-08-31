import numpy
import time
import os
import bpy
import threading


print("hi")

rx=10
ry=10
rz=10

bpy.ops.mesh.primitive_cube_add(location=(10,0,0))

#https://docs.blender.org/api/current/bpy.types.Object.html?highlight=rotation_mode#bpy.types.Object.rotation_mode
bpy.context.active_object.rotation_mode = 'XYZ'


#bpy.context.active_object.rotation_euler = (rx, ry, rz)
#time.sleep(1)

