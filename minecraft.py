from panda3d.core import loadPrcFileData
loadPrcFileData('', 'gl-version 2 1')

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

player.cursor.scale = False       
player.cursor.color = color.pink  

Sky()

bs = []

for i in range(20):
    for j in range(20):
        b = Button(
            model='cube',
            position=(j, 0, i),
            texture='grass.png',
            parent=scene,
            origin_y=0.5,
            color=color.white  
        )
        b.hovered_color = Vec4(0.7, 0.7, 0.7, 1)
        b.pressed_color = Vec4(0.5, 0.5, 0.5, 1)
        bs.append(b)

def input(key):
    global bs
    for b in bs[:]:
        if b.hovered:
            if key == 'left mouse down':
                offset = mouse.normal if mouse.normal else Vec3(0,1,0)
                new = Button(
                    model='cube',
                    position=b.position + offset,
                    color=color.white, 
                    texture='grass.png',
                    parent=scene,
                    origin_y=0.5
                )
                new.hovered_color = Vec4(0.7, 0.7, 0.7, 1)
                new.pressed_color = Vec4(0.5, 0.5, 0.5, 1)
                bs.append(new)
            if key == 'right mouse down':
                bs.remove(b)
                destroy(b)

app.run()
