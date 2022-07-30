from ursina import *
from random import randint

class Snake(Entity):
    def __init__(self):
        snake = super().__init__(model = 'quad',scale = .4,color = color.green,collider = 'box')
        #? компоненты змеи
        self.bodies = []
        #? направление движения змеи по осям x и y
        self.delta = (.06,0)
        #? длина змеи
        self.length = 1
        #? проигрыш
        self.game_over = False


    def add_body(self):
        if self.delta == (.06,0):
            self.bodies.append(Entity(model = 'quad',scale = self.scale,color = color.green,collider = 'box',x = self.x - .06,y = self.y))
        elif self.delta == (0,.06):
            self.bodies.append(Entity(model = 'quad',scale = self.scale,color = color.green,collider = 'box',y = self.y - .06,x = self.x))
        elif self.delta == (-.06,0):
            self.bodies.append(Entity(model = 'quad',scale = self.scale,color = color.green,collider = 'box',x = self.x + .06,y = self.y))
        elif self.delta == (0,-.06):
            self.bodies.append(Entity(model = 'quad',scale = self.scale,color = color.green,collider = 'box',y = self.y + .06,x = self.x))
    
    #? ограничитель размеров змеи
    def bord_snake(self):
        for i in range(len(self.bodies[:-self.length])):
            destroy(self.bodies[i])
        self.bodies = self.bodies[-self.length:]

    def update(self):
        #? движение змеи
        self.x += self.delta[0]
        self.y += self.delta[1]
        self.add_body()
        self.bord_snake()

        #? проверка местоположения змеи
        if abs(self.x) > 8 or  abs(self.y) > 4.5:
            self.game_over = True

    def input(self,key):
        if key == 'd' and self.delta != (-.06,0):
            self.delta = (.06,0)
        elif key == 'a' and self.delta != (.06,0):
            self.delta = (-.06,0)
        elif key == 'w' and self.delta != (0,-.06):
            self.delta = (0,.06)
        elif key == 's' and self.delta != (0,.06):
            self.delta = (0,-.06)
        elif key == 'a' or key == 'd' or key == 'w' or key == 's':
            self.game_over = True


class Apple(Entity):
    def __init__(self):
        super().__init__(model = 'quad',scale = .4,x = randint(-3,3),y = randint(-3,3),color = color.red,collider = 'box')

class Inst_button(Button):
    def __init__(self):
        super().__init__(scale = .05,x = 0,y = .45)
        self.value = 1
        self.text = f'SCORE: {self.value}'
    
    def update(self):
        self.text = f'SCORE: {self.value}'