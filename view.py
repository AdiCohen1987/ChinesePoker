import pygame


# player 1 top, player 2 bottom - computer
class GameView:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 200, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 128)
    WIDTH = 800
    HEIGHT = 600
    DIST_FROM_BOTTOM = 80
    DIST_FROM_TOP = 90
    DIST_BETWEEN_NUMBERS = 55
    DIST_FROM_LEFT_SIDE = 45
    TRANS_COL_WIDTH = 75
    TRANS_COL_TOP = 25
    TRANS_SIZE_FACTOR = 5.1
    LEFT = 1
    TRANS_COL_BOTTOM = 315
    DIST_BETWEEN_COLUMNS = 120
    card = ''

    def __init__(self, _player_1_cards, _player_2_cards):
        self._player_1_cards = _player_1_cards
        self._player_2_cards = _player_2_cards
        # self._player_1_cards = [['2C', '2D', '2S'], ['3C', '3D', '3S', '3H'],
        #                         ['6C', '6D', '6S', '6H', '13S'], ['7C', '7D', '7S'],
        #                         ['8C', '8D', '8S', '8H', '12S']]
        # self._player_2_cards = [['5C', '5D', '5S', '5H', '11S'], ['4C', '4D', '4S', '4H'],
        #                         ['11C', '11D'], ['9C', '9D', '4S', '9H', '14D'],
        #                         ['9C', '9D', '4S', '9H']]
        self.player_1_area = []
        self.player_2_area = []

    def __setCard__(self,card):
        self.card = card

    def createRowsNumbers(self, screen):
        for i in range(1, 6):
            font = pygame.font.Font('freesansbold.ttf', 20)
            text1 = font.render(str(i), True, self.RED, self.BLACK)
            screen.blit(text1, (self.DIST_FROM_LEFT_SIDE,
                                (self.HEIGHT / 3) + (i * self.DIST_BETWEEN_NUMBERS) + self.DIST_FROM_BOTTOM))
            screen.blit(text1, (self.DIST_FROM_LEFT_SIDE,
                                (self.HEIGHT / 2.75) - (i * self.DIST_BETWEEN_NUMBERS) + self.DIST_FROM_TOP))

    def createTransparentRect(self, screen):
        for i in range(1, 6):
            rect = pygame.Surface((self.TRANS_COL_WIDTH, (self.DIST_BETWEEN_NUMBERS * self.TRANS_SIZE_FACTOR)),
                                  pygame.SRCALPHA)
            rect.fill((255, 255, 255, 128))
            topRect = self.DIST_BETWEEN_COLUMNS * i, self.TRANS_COL_TOP
            self.player_1_area.append(screen.blit(rect, topRect))
            bottomRect = self.DIST_BETWEEN_COLUMNS * i, self.TRANS_COL_BOTTOM
            self.player_2_area.append(screen.blit(rect, bottomRect))

    def view(self, player1Turn=True):
        pygame.init()
        size = (self.WIDTH, self.HEIGHT)
        screen = pygame.display.set_mode(size)
        screen.fill(self.GREEN)
        pygame.display.flip()
        self.createRowsNumbers(screen)
        self.createTransparentRect(screen)

        pygame.display.set_caption("Poker")
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('', True, self.GREEN, self.BLUE)
        textRect = text.get_rect()
        textRect.center = (self.WIDTH, self.HEIGHT // 2)
        # -------- Main Program Loop -----------
        running = True
        while running:
            # --- Main event loop
            self.drawCards(screen)
            pygame.display.update()
            # if player1Turn:
            #     text = font.render('Player /n  1  /n turn', True, self.GREEN, self.BLUE)
            # else:
            #     text = font.render('Player 2 turn', True, self.GREEN, self.BLUE)
            # screen.blit(text, textRect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self.LEFT:
                    pos = pygame.mouse.get_pos()
                    if player1Turn:
                        for i in range(0, 5):
                            if self.player_1_area[i].collidepoint(pos) and self._player_1_cards[i].__len__() < 5:
                                self._player_1_cards[i].append(self.card)
                                break
                    else:
                        for i in range(0, 5):
                            if self.player_2_area[i].collidepoint(pos) and self._player_2_cards[i].__len__() < 5:
                                self._player_2_cards[i].append(self.card)
                                break
            pygame.display.update()
            self.drawCards(screen)
            # --- Game logic should go here

            # --- Screen-clearing code goes here

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Close the window and quit.
        pygame.quit()

    def drawCards(self, screen):
        for i in range(0, 5):
            for j in range(0, 5):
                try:
                    img_string = 'resources/' + self._player_1_cards[i][j] + '.gif'
                    image = pygame.image.load(img_string)
                    screen.blit(image, ((self.DIST_BETWEEN_COLUMNS * (i + 1)) + (self.TRANS_COL_WIDTH / 4),
                                        (self.HEIGHT / 3) - (
                                                (j + 1) * self.DIST_BETWEEN_NUMBERS) + self.DIST_FROM_TOP + 10))
                except IndexError:
                    pass
                try:
                    img_string = 'resources/' + self._player_2_cards[i][j] + '.gif'
                    image = pygame.image.load(img_string)
                    screen.blit(image, ((self.DIST_BETWEEN_COLUMNS * (i + 1)) + (self.TRANS_COL_WIDTH / 4),
                                        (self.HEIGHT / 3.3) + (
                                                (j + 1) * self.DIST_BETWEEN_NUMBERS) + self.DIST_FROM_BOTTOM + 10))
                except IndexError:
                    pass


if __name__ == '__main__':
    p1 = []
    p2 = []
    v = GameView(p1, p2)
    v.view('14H')
