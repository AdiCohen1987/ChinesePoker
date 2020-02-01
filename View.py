from const import SUITS
from graphics import *


class GameView:
    def view(self):
        window = GraphWin("Chinese Poker ACO", 1000, 1000)
        window.setBackground('green')

        for x in range(1, 11):
            txtRow = Text(Point(25, 80 * x), x)
            txtRow.setTextColor('white')
            txtRow.draw(window)
            txtCol = Text(Point(75 * x, 25), x)
            txtCol.setTextColor('white')
            txtCol.draw(window)

        row_counter = 1
        for i in range(2, 15):
            for j in SUITS:
                img = img = Image(Point(250 + (25 * i - 2), 250 + (25 * row_counter)),
                                  'resources/' + str(i) + str(j) + '.gif')
                if (i - 2) % 5 == 0:
                    row_counter = row_counter + 1
                img.draw(window)

        window.getMouse()
        window.close()


if __name__ == '__main__':
    v = GameView()
    v.view()
