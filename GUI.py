from curses import *
from curses import textpad


def chrxp(stdscr):
    curs_set(0)
    init_pair(1, COLOR_RED, COLOR_BLUE)
    init_pair(2, COLOR_BLACK, COLOR_WHITE)
    mousemask(1)
    while 1:
        stdscr.clear()
        t = "Hello World"
        h, w = stdscr.getmaxyx()
        x = w//2 - len(t)//2
        y = h//2
        k = h-4
        l = (w-3)//2

        textpad.rectangle(stdscr, 3, 3, h-3, w-3)
        stdscr.attron(color_pair(2))
        stdscr.addstr(k, l, "Exit")
        stdscr.attroff(color_pair(2))


        stdscr.attron(color_pair(1))
        stdscr.addstr(y, x, t)
        stdscr.attroff(color_pair(1))

        stdscr.refresh()

        ky = stdscr.getch()
        if ky == KEY_MOUSE:
            _, a, b, _, _ = getmouse()
            stdscr.addstr(0, 0,str(a)+' '+str(b))
            stdscr.refresh()
            if a>l-1 and a<(l+4) and b == k:
                break
                
def txtbox(stdscr, y=0, xl=0, wl=20):
    wl += xl + 2
    s = ''
    textpad.rectangle(stdscr, y, xl, y + 2, wl)
    stdscr.addstr(y + 1, xl + 1, '')
    cp = 0
    while True:
        k = stdscr.getch()
        if k == KEY_ENTER or k in [10, 13]:
            break
        elif k == KEY_UP or k == KEY_DOWN or len(s) == (wl - 2):
            pass
        elif k == KEY_BACKSPACE or k == 8:
            stdscr.addstr(y + 1, xl + 1, " " * len(s))
            s = s[:-1]
            stdscr.addstr(y + 1, xl + 1, s)
            if cp > 0: cp -= 1
        elif k == KEY_LEFT or k == 27:
            if not cp: pass
            else:
                cp -= 1
                stdscr.addstr(y + 1, xl + 1 + len(s[:cp]), s[cp:])
                stdscr.addstr(y + 1, xl + 1, s[:cp])
        elif k == KEY_RIGHT or k == 26:
            if cp == len(s):pass
            else:
                cp += 1
                stdscr.addstr(y + 1, xl + 1 + len(s[:cp]), s[cp:])
                stdscr.addstr(y + 1, xl + 1, s[:cp])
        else:
            if cp <= wl - 2:
                if cp == len(s):
                    s += str(chr(k))
                    cp += 1
                    stdscr.addstr(y + 1, xl + 1, s)
                else:
                    s = s[:cp] + str(chr(k)) + s[cp:]
                    stdscr.addstr(y + 3, 0, s)
                    stdscr.refresh()
                    stdscr.addstr(y + 1, xl + 1 + len(s[:cp+1]), s[cp+1:])
                    stdscr.addstr(y + 1, xl + 1, s[:cp+1])
                    cp += 1

        
wrapper(chrxp)
