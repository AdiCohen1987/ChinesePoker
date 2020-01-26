from graphics import *


def view():
    window = GraphWin("Chinese Poker ACO", 800, 800)
    window.setBackground('green')

    for x in range(1, 11):
        txtRow = Text(Point(25, 80 * x), x)
        txtRow.setTextColor('white')
        txtRow.draw(window)
        txtCol = Text(Point(75 * x, 25), x)
        txtCol.setTextColor('white')
        txtCol.draw(window)

    img = Image(Point(250, 250), "resources/2C.gif")
    img.draw(window)
    window.getMouse()
    window.close()


if __name__ == '__main__':
    view()
