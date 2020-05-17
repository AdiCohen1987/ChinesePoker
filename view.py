import pygame

# player 1 top, player 2 bottom - computer
from const import RED_COLOR, BLACK_COLOR, DIST_FROM_LEFT_SIDE, HEIGHT, DIST_BETWEEN_NUMBERS, DIST_FROM_BOTTOM, \
    DIST_FROM_TOP, TRANS_COL_WIDTH, TRANS_SIZE_FACTOR, DIST_BETWEEN_COLUMNS, TRANS_COL_TOP, TRANS_COL_BOTTOM, \
    COL_TOP_FACTOR, COL_BOTTOM_FACTOR, GREEN_COLOR


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
            topRect = DIST_BETWEEN_COLUMNS * i, TRANS_COL_TOP + COL_TOP_FACTOR
            self.player_1_area.append(screen.blit(rect, topRect))
            bottomRect = DIST_BETWEEN_COLUMNS * i, TRANS_COL_BOTTOM + COL_BOTTOM_FACTOR
            self.player_2_area.append(screen.blit(rect, bottomRect))

    def createGameResult(self, screen, gameResult):
        for i in range(0, 10):
            result = gameResult[i].split(" ")
            font = pygame.font.Font('freesansbold.ttf', 20)
            if i < 5:
                if result[1] == '1':
                    text = font.render('Win', True, RED_COLOR, BLACK_COLOR)
                    topRect = DIST_BETWEEN_COLUMNS * (i + 1), TRANS_COL_TOP - COL_TOP_FACTOR
                    screen.blit(text, topRect)
                else:
                    text = font.render('Win', True, RED_COLOR, BLACK_COLOR)
                    bottomRect = DIST_BETWEEN_COLUMNS * (i + 1), HEIGHT - COL_BOTTOM_FACTOR
                    screen.blit(text, bottomRect)
            else:
                if result[1] == '1':
                    text1 = font.render('Win', True, RED_COLOR, BLACK_COLOR)
                    text2 = font.render('   ', True, RED_COLOR, GREEN_COLOR)
                    screen.blit(text1,
                                (DIST_FROM_LEFT_SIDE,
                                 (HEIGHT / 2.75) - ((i - 4) * DIST_BETWEEN_NUMBERS) + DIST_FROM_TOP))
                    screen.blit(text2,
                                (DIST_FROM_LEFT_SIDE,
                                 (HEIGHT / 3) + ((i - 4) * DIST_BETWEEN_NUMBERS) + DIST_FROM_BOTTOM))

                else:
                    text1 = font.render('   ', True, RED_COLOR, GREEN_COLOR)
                    text2 = font.render('Win', True, RED_COLOR, BLACK_COLOR)
                    screen.blit(text1,
                                (DIST_FROM_LEFT_SIDE,
                                 (HEIGHT / 2.75) - ((i - 4) * DIST_BETWEEN_NUMBERS) + DIST_FROM_TOP))
                    screen.blit(text2,
                                (DIST_FROM_LEFT_SIDE,
                                 (HEIGHT / 3) + ((i - 4) * DIST_BETWEEN_NUMBERS) + DIST_FROM_BOTTOM))
