from tkinter import *
from time import sleep, time
from random import randint
from math import sqrt

height = 500
width = 800
window = Tk()
window.title('Bubble Blastr')
c = Canvas(window, width=width, height=height, bg='darkblue')
c.pack()

ship = list()
ship.append(c.create_polygon(5, 5, 5, 25, 30, 15, fill='red'))
ship.append(c.create_line(30, 15, 65, 15, fill='red', width=3))
ship.append(c.create_rectangle(-20, 5, 5, 25, fill='red'))
ship.append(c.create_oval(0, 0, 120, 40,  fill='red'))
ship.append(c.create_oval(70, -10, 20, 20,  fill='blue'))

SHIP_R = 15
MID_X = width / 2
MID_Y = height / 2
SHIP_SPD = 10
BUB_CHANCE = 10

for ship_part in ship:
    c.move(ship_part, MID_X, MID_Y)

def move_ship(event):
    delta_x = 0
    delta_y = 0
    if event.keysym == 'Up':
        delta_y = -SHIP_SPD
    elif event.keysym == 'Down':
        delta_y = SHIP_SPD
    elif event.keysym == 'Left':
        delta_x = -SHIP_SPD
    elif event.keysym == 'Right':
        delta_x = SHIP_SPD
    for ship_part in ship:
        c.move(ship_part, delta_x, delta_y)


c.bind_all('<Key>', move_ship)

bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BNB_R = 30
MAX_BNB_SPD = 10
GAP = 100


def create_bubble():
    x = width + GAP
    y = randint(0, height)
    r = randint(MIN_BUB_R, MAX_BNB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BNB_SPD))


def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)


def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y


def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]


def clean_up_bubs():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords((bub_id[i]))
        if x < -GAP:
            del_bubble(i)


def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1,):
        if distance(ship[3], bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points


def none_function():
    pass

# MAIN GAME LOOP


score = 0
while True:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    print(score)
    window.update()
    sleep(0.01)
