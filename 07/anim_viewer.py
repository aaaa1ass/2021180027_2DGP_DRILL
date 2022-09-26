from pico2d import *

open_canvas(1200,800)
grass = load_image('grass.png')
character = load_image('penguin.png')

def background():
       clear_canvas()
       grass.draw(400, 30)
       grass.draw(1200, 30)

def fixed_rope():
       character.clip_draw(13 * 128, 6 * 128, 128, 128, 600, 610)
       for rope_cnt in range(0, 2, 1):
              character.clip_draw(0, 3 * 128, 128, 128, 600, 610 - 128 * (rope_cnt + 1))
       character.clip_draw(5 * 128, 3 * 128, 128, 128, 600, 610 - 128 * 3)

def throw_rope():
       t = 0
       for t in range(0,10,1):
              background()
              character.clip_draw(12 * 128,6 * 128,128,128, 600,-10 * t * t + 150 * t + 110)
              character.clip_draw(0 * 128,9 * 128,128,128,600,110)
              update_canvas()
              delay(0.05)
              get_events()

def go_straight():
       x = 0
       frame = 0
       for x in range(100,600+1,10):
              background()
              character.clip_draw(frame * 128,1900,128,128,x,90)
              update_canvas()
              frame = (frame + 1) % 9
              delay(0.05)
              get_events()

def spread_rope():
       y = 0
       len = 0
       for len in range(0,12,1):
              background()
              character.clip_draw(13 * 128, 6 * 128, 128, 128, 600, 610)
              character.clip_draw( (len % 4 + 1) * 128, 3 * 128, 128,128,600, 610 - (y + 1) * 128)
              character.clip_draw(0 * 128,9 * 128,128,128,600,110)
              for rope_cnt in range(0,y,1):
                     character.clip_draw(0,3 * 128, 128,128,600,610 - (rope_cnt + 1) * 128)
              update_canvas()
              y = (len + 1) // 4
              delay(0.02)
              get_events()

def go_up():
       y = 0
       frame = 0
       for y in range(110,600  + 1, 10):
              background()
              fixed_rope()
              character.clip_draw(frame * 128, 9 * 128, 128, 128, 600,y)
              update_canvas()
              frame = (frame + 1) % 6
              delay(0.05)
              get_events()

def jump():
       x = 600
       t = 0
       frame = 0
       for t in range(0, 26, 1):
              background()
              fixed_rope()
              character.clip_draw(frame * 128, 6 * 128, 128, 128, x, -3 * t * t + 55 * t + 600)
              x += 20
              frame = t // 3
              update_canvas()
              delay(0.05)
              get_events()
       background()
       fixed_rope()
       character.clip_draw(9 * 128, 15 * 128, 128, 128, x, -3 * t * t + 55 * t + 600)
       update_canvas()
       delay(2)



while True:
       go_straight()
       throw_rope()
       spread_rope()
       go_up()
       jump()

