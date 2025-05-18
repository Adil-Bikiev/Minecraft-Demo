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
        b = Button(
            model='cube',
            position=(j, 0, i),
            texture='grass.png',
            parent=scene,
            origin_y=0.5,
            color=color.white  # чтобы текстура не была затемнена изначально
        )
        # При наведении делаем цвет чуть темнее (умножаем на 0.7)
        b.hovered_color = color.rgb(70, 70, 70)  
        # При отпускании мыши (нажатии) цвет можно оставить таким же, как при наведении
        b.pressed_color = color.rgb(50, 50, 50)  

app.run()
