from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global hei
    global s

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                s = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                s = 0
            elif event.key == SDLK_UP:
                hei += 1
            elif event.key == SDLK_DOWN:
                hei -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                s = 3
            elif event.key == SDLK_LEFT:
                dir += 1
                s = 2
            elif event.key == SDLK_UP:
                hei -= 1
            elif event.key == SDLK_DOWN:
                hei += 1

open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dir = 0
hei = 0
s = 3

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, s * 100 ,100,100,x,y)
    update_canvas()
    frame = (frame + 1) % 8
    if x < TUK_WIDTH and x > 0:
        x += dir * 3
    elif x <= 0:
        x = 0 + 1
    else:
        x = TUK_WIDTH - 1
    if y < TUK_HEIGHT and y > 0:
        y += hei * 3
    elif y <= 0:
        y = 0 + 1
    else:
        y = TUK_HEIGHT - 1


    handle_events()

close_canvas()