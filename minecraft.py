from panda3d.core import loadPrcFileData
loadPrcFileData('', 'gl-version 2 1')

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

# Настраиваем курсор через один кадр после создания
invoke(lambda: setattr(player.cursor, 'scale', 0.01), delay=0)
invoke(lambda: setattr(player.cursor, 'color', color.black66), delay=0)

Sky()

for i in range(20):
    for j in range(20):
        Button(
            color=color.white,
            model='cube',
            position=(j, 0, i),
            texture='white_cube',
            parent=scene,
            origin_y=0.5
        )

app.run()
