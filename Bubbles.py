from tkinter import *
height = 500
width = 800
window = Tk()
window.title('Bubble Blastr')
c = Canvas(window, width = width, height = height, bg = 'darkblue')
c.pack()
ship_id = c.create_polygon (5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = c.create_oval (0, 0, 30, 30, outline='black')
SHIP_R = 15
MID_X = width / 2
MID_Y = height / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
SHIP_SPD = 10
def move_ship(event) :
    if event.keysym == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Right':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
c.bind_all('<Key>', move_ship)
from random import randint
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
    pos = c.coords (id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + [3])/2
    return x, y
from time import sleep, time
BUB_CHANCE = 10
#MAIN GAME LOOP
while True:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    window.update()
    sleep(0.01)
def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]
