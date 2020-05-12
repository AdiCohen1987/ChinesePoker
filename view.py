import pygame

# player 1 top, player 2 bottom - computer
from const import RED_COLOR, BLACK_COLOR, DIST_FROM_LEFT_SIDE, HEIGHT, DIST_BETWEEN_NUMBERS, DIST_FROM_BOTTOM, \
    DIST_FROM_TOP, TRANS_COL_WIDTH, TRANS_SIZE_FACTOR, DIST_BETWEEN_COLUMNS, TRANS_COL_TOP, TRANS_COL_BOTTOM, WIDTH, \
    GREEN_COLOR, BLUE_COLOR


class GameView:
    def __init__(self):
        self.player_1_area = []
        self.player_2_area = []

    def createRowsNumbers(self, screen):
        for i in range(1, 6):
            font = pygame.font.Font('freesansbold.ttf', 20)
            text1 = font.render(str(i), True, RED_COLOR, BLACK_COLOR)
            screen.blit(text1, (DIST_FROM_LEFT_SIDE, (HEIGHT / 3) + (i * DIST_BETWEEN_NUMBERS) + DIST_FROM_BOTTOM))
            screen.blit(text1, (DIST_FROM_LEFT_SIDE, (HEIGHT / 2.75) - (i * DIST_BETWEEN_NUMBERS) + DIST_FROM_TOP))

    def createTransparentRect(self, screen):
        for i in range(1, 6):
            rect = pygame.Surface((TRANS_COL_WIDTH, (DIST_BETWEEN_NUMBERS * TRANS_SIZE_FACTOR)), pygame.SRCALPHA)
            rect.fill((255, 255, 255, 128))
            topRect = DIST_BETWEEN_COLUMNS * i, TRANS_COL_TOP
            self.player_1_area.append(screen.blit(rect, topRect))
            bottomRect = DIST_BETWEEN_COLUMNS * i, TRANS_COL_BOTTOM
            self.player_2_area.append(screen.blit(rect, bottomRect))

    def view(self, pygame, screen):
        size = (WIDTH, HEIGHT)
        screen = pygame.display.set_mode(size)
        screen.fill(GREEN_COLOR)
        pygame.display.flip()
        self.createRowsNumbers(screen)
        self.createTransparentRect(screen)

        pygame.display.set_caption("Poker")
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('', True, GREEN_COLOR, BLUE_COLOR)
        textRect = text.get_rect()
        textRect.center = (WIDTH, HEIGHT // 2)
