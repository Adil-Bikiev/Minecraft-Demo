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
# Генерация земли
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

def input(key):
    for b in bs:
        if b.hovered:
            if key == 'left mouse down':
                new = Button(
                    model='cube',
                    position=b.position + mouse.normal,
                    color=color.white, 
                    texture='grass.png',
                    parent=scene,
                    origin_y=0.5
                )
                bs.append(new)
            if key == 'right mouse down':
                bs.remove(b)
                destroy(b)

app.run()
