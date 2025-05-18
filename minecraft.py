from panda3d.core import loadPrcFileData
loadPrcFileData('', 'gl-version 2 1')  # Совместимость с GLSL на macOS

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
player.cursor.scale = 0.02  # Уменьшаем ромб-прицел

Sky()

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(
            color=color.white,
            model='cube',
            position=(j, 0, i),
            texture='white_cube',
            parent=scene,
            origin_y=0.5
        )
        boxes.append(box)

app.run()
