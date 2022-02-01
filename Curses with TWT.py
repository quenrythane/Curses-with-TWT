import curses
from curses import wrapper
import time


def main(stdscr):
    # adding colors
    """
    Z dodwaniem koloru jest tak, że najpierw trzeba zainicjować parę:
    curses.init_pair(id_zestawu, KOLOR_NAPISU, KOLOR_TŁA)
    pod spodem odpowiednie kolory mają po prostu odpowiednie int-y.
    Tak więc jak można zobaczyć na dole, cyfra 1 oznacza moje id cyfra 1 kolor zielony, cyfar 0 kolor czarny

    Następnie by użyć koloru należy użyć koemndy:
    curses.color_pair(color_id) wewwnątrz komendy stdscr.addstr(rows, columns, 'str', komenda_coloru)
    Ja stworzyłem funkcje, która po uprzednim zainicjowaniu par kolorów wraz z id, można użyć prostego zwrotu
    color(id_coloru_który chcemy użyć)
    """

    # pary kolorów
    # (id, kolor_napisu, kolor_tła)
    curses.init_pair(1, 2, 0)  # napis: zielony, tło: czarne
    curses.init_pair(2, 1, 7)  # napis: niebieski, tło: czarne

    def color(color_id):
        my_color = curses.color_pair(color_id)
        return my_color

    stdscr.clear()  # czyści terminal do czysta
    stdscr.addstr(10, 10, 'hello world', color(2))  # addstr(y, x, str)
    stdscr.addstr(10, 16, 'hello world', curses.A_UNDERLINE)  # Można nadpisywać addstr
    # w tym przypadku nadpiszemy 'world' z 1szego addstr całą frazą z 2giego addstr
    stdscr.addstr(11, 16, 'hello world', curses.A_BOLD | color(1))  # Żeby połączyć A i color używamy znauk |
    stdscr.refresh()  # to w sumie nie wiem co robi. Chyba klatkuje okno terminalu (FPSy)
    # już wiem. Wszystko to co robi program jest niewidoczne, dopóki tego nie zrefreshujemy.
    # coś jak w html. Możemy robić zmiany, ale dopóki nie odświezymy strony nie zoabczym naszych zmian
    # stdscr.getch()  # czeka na character który wpisze użytkownik

    time. sleep(2)
    for i in range(100):
        stdscr.clear()
        x_color = color(1)

        if i % 3 == 0:
            x_color = color(2)

        stdscr.addstr(f'Count: {i}', x_color)
        stdscr.refresh()
        time.sleep(0.1)

    stdscr.getch()  # czeka na character który wpisze użytkownik


wrapper(main)  # odpala to co wyżej zrobiliśmy
