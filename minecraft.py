from panda3d.core import loadPrcFileData
loadPrcFileData('', 'gl-version 2 1')

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

player.cursor.scale = False       
player.cursor.color = color.pink  

Sky()

# Генерация земли
for i in range(20):
    for j in range(20):
        Button(
            model='cube',
            position=(j, 0, i),
            texture='grass.png',
            parent=scene,
            origin_y=0.5
        )

app.run()
