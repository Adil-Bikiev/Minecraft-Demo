from panda3d.core import loadPrcFileData
loadPrcFileData('', 'gl-version 2 1')  # Совместимость с GLSL на macOS

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
Sky()

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(
            color=color.white,
            model='cube',
            position=(j, 0, i),
            texture='white_cube',  # Используем встроенную текстуру
            parent=scene,
            origin_y=0.5
        )
        boxes.append(box)

app.run()
