import game_framework
from pico2d import *
import random
import game_world

import server

class Ball:

    def __init__(self, index):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(0,1800)
        self.y = random.randint(0,1100)
        self.index = str(index)

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - server.background.window_left,self.y - server.background.window_bottom)

    def handle_collision(self,other,group):
        if group == 'boy : ball' + self.index:
            game_world.remove_object(self)
