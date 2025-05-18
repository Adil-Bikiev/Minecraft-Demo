from panda3d.core import loadPrcFileData
loadPrcFileData('', 'gl-version 2 1')

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

Sky()

# Флаг, чтобы изменить курсор только один раз
cursor_initialized = False

def update():
    global cursor_initialized
    if not cursor_initialized and hasattr(player, 'cursor'):
        player.cursor.scale = 0.01
        player.cursor.color = color.black66
        cursor_initialized = True  # Не повторять

# Генерация земли
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
