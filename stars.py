import curses
import time
import numpy as np

REFRESH_INTERVAL = 0.1
TRUE_CHAR = "*"
FALSE_CHAR = "."
STAR_PROBABILITY = 0.004


def print_buffer(stdscr: curses.window, buffer: np.ndarray) -> None:
    stdscr.clear()

    for line_idx, row in enumerate(buffer):
        for col_idx, val in enumerate(row):
            ch = FALSE_CHAR
            cpair = 1
            if val:
                ch = TRUE_CHAR
                cpair = 2

            stdscr.addstr(line_idx, col_idx, ch, curses.color_pair(cpair))

    stdscr.refresh()


def main(stdscr: curses.window) -> None:
    buffer_shape = (curses.LINES, curses.COLS - 1)

    # hide cursor
    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    # do not wait for input when asking for input
    stdscr.nodelay(True)

    last_refresh = time.time()

    while True:
        c = stdscr.getch()

        curr_time = time.time()

        if c == curses.KEY_RESIZE:
            max_y, max_x = stdscr.getmaxyx()
            curses.resizeterm(max_y, max_x)
            buffer_shape = (max_y, max_x - 1)

            # clear curses.KEY_RESIZE from getch
            stdscr.getch()

        # quit on any character
        elif c != curses.ERR:
            return

        if curr_time - last_refresh >= REFRESH_INTERVAL:
            last_refresh = curr_time
            buffer = np.random.random(buffer_shape) > (1 - STAR_PROBABILITY)
            print_buffer(stdscr, buffer)


if __name__ == "__main__":
    curses.wrapper(main)
