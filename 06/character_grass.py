from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
while (True):
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 4
        delay(0.005)
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 4
        delay(0.005)
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 4
        delay(0.005)
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 4
        delay(0.005)
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 4
        delay(0.005)
    gakdo = -90
    while (gakdo < 270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + 255 * math.cos(gakdo / 360 * 2 * math.pi),345 + 255 * math.sin(gakdo/ 360*2 *math.pi))
        gakdo += 1
        delay(0.005)

    
close_canvas()
