import pygame


class GameView:
    _player_1_cards = []
    _player_2_cards = []
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 200, 0)
    RED = (255, 0, 0)
    HEIGHT = 800
    WIDTH = 800

    def __init__(self, _player_1_cards, _player_2_cards):
        self._player_1_cards = _player_1_cards
        self._player_2_cards = _player_2_cards
        self._player_1_cards = [['2C', '2D', '2S', '2H'], ['3C', '3D', '3S', '3H']]

    def create_numbers(self, HEIGHT, screen):
        for i in range(1, 6):
            font = pygame.font.Font('freesansbold.ttf', 25)
            text1 = font.render(str(i), True, self.RED, self.BLACK)
            textRect = text1.get_rect()
            screen.blit(text1, (40, (HEIGHT / 2) - (70 * i) - 15))
            screen.blit(text1, (40, (HEIGHT / 2) + (70 * i) - 30))

    def create_transparent_rect(self, HEIGHT, screen):
        for i in range(1, 6):
            rect = pygame.Surface((70, (HEIGHT / 2.5)), pygame.SRCALPHA)  # per-pixel alpha
            rect.fill((255, 255, 255, 128))  # notice the alpha value in the color
            screen.blit(rect, (130 * i, (HEIGHT / 2) - (70 * 5) - 15))
            screen.blit(rect, (130 * i, (HEIGHT / 2) + 70 - 35))

    def view(self):
        pygame.init()
        size = (self.HEIGHT, self.WIDTH)
        screen = pygame.display.set_mode(size)
        screen.fill(self.GREEN)
        pygame.display.flip()
        self.create_numbers(self.HEIGHT, screen)
        self.create_transparent_rect(self.HEIGHT, screen)
        for i in range(len(self._player_1_cards)):
            for j in range(len(self._player_1_cards[i])):
                img_string = 'resources/' + self._player_1_cards[i][j] + '.gif'
                image = pygame.image.load(img_string)
                screen.blit(image, (80 * j + 150, 80 * i + 400))


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
