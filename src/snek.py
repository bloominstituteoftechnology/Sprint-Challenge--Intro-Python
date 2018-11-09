import random
import curses
import math

# initialize the screen
s = curses.initscr()

# turn off the cursor
curses.curs_set(0)

# set the width and height of the screen
s_height, s_width = s.getmaxyx()

# create the window
w = curses.newwin(s_height, s_width, 0, 0)

# accept keypad input
w.keypad(1)

# refresh the screen every 200 ms
w.timeout(200)

snek_x = s_width / 4

snek_y = s_height / 2

snek = [
    [snek_y, snek_x],
    [snek_y, snek_x - 1],
    [snek_y, snek_x - 2],
]

food = [math.floor(s_height / 2), math.floor(s_width / 2)]
w.addch(food[0], food[1], curses.ACS_CKBOARD)

key = curses.KEY_RIGHT

running = True

while running:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snek[0][0] in [0, s_height] or snek[0][1] in [0, s_width
                                                     ] or snek[0] in snek[1:]:
        running = False
        curses.endwin()
        quit()

    new_head = [snek[0][0], snek[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1

    if key == curses.KEY_UP:
        new_head[0] -= 1

    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snek.insert(0, new_head)

    if snek[0] == food:
        food = None

        while food is None:
            new_food = [
                random.randint(1, s_height - 1),
                random.randint(1, s_width - 1)
            ]

            food = new_food if new_food not in snek else None
        w.addch(math.floor(food[0]), math.floor(food[1]), curses.ACS_CKBOARD)
    else:
        tail = snek.pop()
        w.addch(math.floor(tail[0]), math.floor(tail[1]), ' ')

    w.addch(math.floor(snek[0][0]), math.floor(snek[0][1]), curses.ACS_CKBOARD)
