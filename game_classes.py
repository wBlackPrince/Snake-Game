from ursina import *
from random import randint

#? класс игрока
class Snake(Entity):
    def __init__(self,**kwargs):
        super().__init__(**kwargs,model = 'quad',color = color.green,scale = .5,collider = 'box')
        #? список из частей тела 
        self.bodies = []
        #? направление движения
        self.flag = 'd'
        #? размер змейки
        self.size = 1
        self.count = 1
        #? поражение
        self.game_over = False

    #? ограничение роста змейки
    def board(self):
        if self.size == self.count:
            destroy(self.bodies[0])
            self.bodies.pop(0)
        else:
            self.count += 1

    #? движение змеи
    def move_d(self):
        self.x += .05
        self.bodies.append(Entity(model = 'quad',scale = .5,x= self.x,y = self.y,color = color.green,collider = 'box'))
        self.board()

    def move_a(self):
        self.x -= .05
        self.bodies.append(Entity(model = 'quad',scale = .5,x= self.x,y = self.y,color = color.green,collider = 'box'))
        self.board()
    
    def move_w(self):
        self.y += .05
        self.bodies.append(Entity(model = 'quad',scale = .5,x= self.x,y = self.y,color = color.green,collider = 'box'))
        self.board()

    def move_s(self):
        self.y -= .05
        self.bodies.append(Entity(model = 'quad',scale = .5,x= self.x,y = self.y,color = color.green,collider = 'box'))
        self.board()


    def input(self,key):
        if key == 'd':
            if self.flag == 'a':
                self.game_over = True
            self.flag = 'd'
        
        elif key == 'a':
            if self.flag == 'd':
                self.game_over = True
            self.move_a()
            self.flag = 'a'
        
        elif key == 'w':
            if self.flag == 's':
                self.game_over = True
            self.move_w
            self.flag = 'w'
            
        elif key == 's':
            if self.flag == 'w':
                self.game_over = True
            self.move_s
            self.flag = 's'
    
    def update(self):
        if self.flag == 'd':
            self.move_d()
        elif self.flag == 'a':
            self.move_a()
        elif self.flag == 'w':
            self.move_w()
        elif self.flag == 's':
            self.move_s()

        #? проверка местоположения змеи
        if abs(self.x) > 8 or 50 > abs(self.y) > 5:
            self.game_over = True

class Apple(Entity):
    count = 0
    apples = []
    def __init__(self):
        super().__init__(model = 'quad',color = color.red,scale = .5,x = randint(-3,3),y = randint(-3,3),collider = 'box')
        Apple.apples.append(self)
        Apple.count += 1

    #? проверка на столкновение со змееей
    def update(self):
        hit_inf = self.intersects()
        if hit_inf.hit and type(hit_inf.entity) == Snake:
            destroy(self)
            hit_inf.entity.size += 1
            hit_inf.entity.count = 1
            Apple.count -= 1

class Inst_button(Button):
    def __init__(self):
        super().__init__(scale = .05,x = 0,y = .45)
        self.value = 1
        self.text = f'SCORE: {self.value}'
    
    def update(self):
        self.text = f'SCORE: {self.value}'
