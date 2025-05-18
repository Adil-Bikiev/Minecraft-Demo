from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j,0,1),
            texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

app.run()