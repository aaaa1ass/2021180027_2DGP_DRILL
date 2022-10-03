import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



open_canvas(TUK_WIDTH, TUK_HEIGHT)

# fill here
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = sx,sy
ax,ay = x, y
frame = 0
t = 0
dir = 0
hide_cursor()
def reset_world():
    global ax, ay
    global t
    global sx, sy
    ax,ay = random.randint(0,TUK_WIDTH), random.randint(0,TUK_HEIGHT)
    t = 0
    sx, sy = x, y
    pass

def update_world():
    global x,y
    global t
    global dir
    t += 0.005
    x =(1-t)*sx + t*ax
    y = (1-t)*sy + t*ay
    if sx > ax:
        dir = 0
    else:
        dir = 1

    if t >= 1.0:
        reset_world()
    pass

reset_world()

while running:
    update_world()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
    arrow.draw(ax,ay)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()


close_canvas()




