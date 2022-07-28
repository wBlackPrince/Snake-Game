from ursina import *
from game_classes import *

app = Ursina()
window.fullscreen = True
window.color = color.black

def update():
    if Apple.count != 4:
        Apple()
    
    if snake.game_over:
        print_on_screen('Game over',position = (-.1,0))
        destroy(snake)
        for i in snake.bodies:
            destroy(i)
    score.value = snake.size

snake = Snake()
score = Inst_button()

app.run()