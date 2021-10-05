import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
handx, handy = KPU_WIDTH // 2, KPU_HEIGHT // 2
seedir = 1      # 캐릭터가 보는 방향. -1이면 왼쪽, +1이면 오른쪽
frame = 0
# hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if x==handx and y==handy:       # 손가락과 캐릭터의 위치가 동일하다면 손가락을 랜덤한 위치로 보내버린다
        handx = random.randint(0, KPU_WIDTH // 4) * 4
        handy = random.randint(0, KPU_HEIGHT // 4) * 4
        if x>handx:
            seedir = -1
        else:
            seedir = 1
    else:
        if x>handx:
            x -= 4
        elif x<handx:
            x += 4
        if y>handy:
            y -= 4
        elif y<handy:
            y += 4

    if seedir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    hand.draw(handx, handy)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()