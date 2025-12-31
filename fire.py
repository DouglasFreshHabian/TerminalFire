#!/usr/bin/env python3
import curses
import random
import time

CHARS = " .:^*xsS#$"

def run(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    for i, c in enumerate((0, 1, 3, 4), start=1):
        curses.init_pair(i, c, -1)

    h, w = stdscr.getmaxyx()
    size = w * h
    buf = [0] * (size + w + 1)

    stdscr.nodelay(True)

    while True:
        h, w = stdscr.getmaxyx()
        size = w * h

        for _ in range(w // 8):
            buf[random.randrange(w) + w * (h - 1)] = 65

        for i in range(size):
            v = (buf[i] + buf[i + 1] + buf[i + w] + buf[i + w + 1]) >> 2
            buf[i] = v

            if i < size - 1:
                y, x = divmod(i, w)
                c = CHARS[9 if v > 9 else v]
                color = 4 if v > 15 else 3 if v > 9 else 2 if v > 4 else 1
                stdscr.addch(y, x, c, curses.color_pair(color) | curses.A_BOLD)

        stdscr.refresh()
        time.sleep(0.03)

        if stdscr.getch() != -1:
            break

def main():
    curses.wrapper(run)

if __name__ == "__main__":
    main()
