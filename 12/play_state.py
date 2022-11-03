from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy


boy = None
back_grass = None
front_grass = None
ball = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, back_grass, front_grass
    boy = Boy()
    back_grass = Grass(400,30)
    front_grass = Grass(400,10)
    game_world.add_object(boy, 1)
    game_world.add_object(back_grass, 0)
    game_world.add_object(front_grass, 2)


# 종료
def exit():
    game_world.clear()
    # global boy, grass
    # del boy
    # del grass

def update():

    for game_object in game_world.all_objects():
        game_object.update()
    # boy.update()
    # if ball:
    #     ball.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
    # grass.draw()
    # boy.draw()
    # if ball:
    #     ball.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
