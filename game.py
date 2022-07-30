from ursina import *
from game_classes import *

app = Ursina()
window.fullscreen = True
window.color = color.black

def update():
    global apples
    score.value = s.length
    hit_inf = s.intersects()

    if hit_inf.hit and hit_inf.entity in apples:
        apples.remove(hit_inf.entity)
        destroy(hit_inf.entity)
        s.length += 1
    
    elif hit_inf and s.length > 10 and hit_inf.entity in s.bodies[:s.length//2]:
        s.game_over = True
    
    if s.game_over:
        print_on_screen('GAME OVER',position = (-.1,0))
        destroy(s)
        for i in range(len(s.bodies)):
            destroy(s.bodies[i])

    if len(apples) == 0:
        apples = [Apple() for i in range(4)]

s = Snake()
apples = [Apple() for i in range(4)]
score = Inst_button()


app.run()