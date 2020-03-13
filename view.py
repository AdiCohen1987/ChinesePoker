import pygame


class GameView:
    _player_1_cards = []
    _player_2_cards = []
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 200, 0)
    RED = (255, 0, 0)
    WIDTH = 800
    HEIGHT = 600
    DIST_FROM_BOTTOM = 80
    DIST_FROM_TOP = 90
    DIST_BETWEEN_NUMBERS = 50
    DIST_FROM_LEFT_SIDE = 45
    TRANS_COL_WIDTH = 75
    TRANS_COL_TOP = 25
    TRANS_COL_BOTTOM = 315
    DIST_BETWEEN_COLUMNS = 120

    def __init__(self, _player_1_cards, _player_2_cards):
        self._player_1_cards = _player_1_cards
        self._player_2_cards = _player_2_cards
        self._player_1_cards = [['2C', '2D', '2S', '2H', '10S'], ['3C', '3D', '3S', '3H', '9D']]

    def createRowsNumbers(self, screen):
        for i in range(1, 6):
            font = pygame.font.Font('freesansbold.ttf', 20)
            text1 = font.render(str(i), True, self.RED, self.BLACK)
            screen.blit(text1, (self.DIST_FROM_LEFT_SIDE,
                                (self.HEIGHT / 3) + (i * self.DIST_BETWEEN_NUMBERS) + self.DIST_FROM_BOTTOM))
            screen.blit(text1, (self.DIST_FROM_LEFT_SIDE,
                                (self.HEIGHT / 3) - (i * self.DIST_BETWEEN_NUMBERS) + self.DIST_FROM_TOP))

    def createTransparentRect(self, screen):
        for i in range(1, 6):
            rect = pygame.Surface((self.TRANS_COL_WIDTH, (self.DIST_BETWEEN_NUMBERS * 5.05)), pygame.SRCALPHA)
            rect.fill((255, 255, 255, 128))
            screen.blit(rect, (self.DIST_BETWEEN_COLUMNS * i, self.TRANS_COL_TOP))
            screen.blit(rect, (self.DIST_BETWEEN_COLUMNS * i, self.TRANS_COL_BOTTOM))

    def view(self):
        pygame.init()
        size = (self.WIDTH, self.HEIGHT)
        screen = pygame.display.set_mode(size)
        screen.fill(self.GREEN)
        pygame.display.flip()
        self.createRowsNumbers(screen)
        self.createTransparentRect(screen)

        for i in range(0, 2):
            for j in range(0, 5):
                img_string = 'resources/' + self._player_1_cards[i][j] + '.gif'
                image = pygame.image.load(img_string)
                screen.blit(image, (self.DIST_FROM_LEFT_SIDE,
                                    (self.HEIGHT / 3) + (i * self.DIST_BETWEEN_NUMBERS) + self.DIST_FROM_BOTTOM))

        pygame.display.set_caption("Poker")
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        running = True
        while running:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # elif event.type == pygame.mouse.
            pygame.display.update()

            # --- Game logic should go here

            # --- Screen-clearing code goes here

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Close the window and quit.
        pygame.quit()

        # Draw Once
        Rectplace = pygame.draw.rect(self.window, (255, 0, 0), (100, 100, 100, 100))
        pygame.display.update()
        # Main Loop
        while running:
            # Mouse position and button clicking.
            pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            # Check if the rect collided with the mouse pos
            # and if the left mouse button was pressed.
            if Rectplace.collidepoint(pos) and pressed1:
                print("You have opened a chest!")
            # Quit pygame.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


if __name__ == '__main__':
    p1 = []
    p2 = []
    v = GameView(p1, p2)
    v.view()
