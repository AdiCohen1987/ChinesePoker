import pygame

from const import WIDTH, HEIGHT, GREEN_COLOR, BLUE_COLOR, DIST_BETWEEN_COLUMNS, TRANS_COL_WIDTH, DIST_BETWEEN_NUMBERS, \
    DIST_FROM_TOP, DIST_FROM_BOTTOM, NUM_OF_HANDS_AND_CARDS, LEFT, DIST_FROM_RIGHT_SIDE
from game import Play
from view import GameView


class GameController:
    def __init__(self, gamePlay, view, player_1_cards, player_2_cards):
        self.gamePlay = gamePlay
        self.view = view
        self._player_1_cards = player_1_cards
        self._player_2_cards = player_2_cards

    def __setCard__(self, card):
        self.card = card

    def start(self, player1Turn=True):
        pygame.init()
        size = (WIDTH, HEIGHT)
        screen = pygame.display.set_mode(size)
        screen.fill(GREEN_COLOR)
        pygame.display.flip()
        self.view.createRowsNumbers(screen)
        self.view.createTransparentRect(screen)
        self.displaySideCard(screen, None)
        pygame.display.set_caption("Poker")
        clock = pygame.time.Clock()
        font, turnTextRect = self.createTurnTextRect()
        cardsCount = 10
        needToDrawCard = True
        self.refreshCards(screen)
        gameEnded = False
        while True:
            if needToDrawCard and not gameEnded:
                card = self.drawNewCard(font, player1Turn, screen, turnTextRect)
            needToDrawCard = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    if player1Turn:
                        for i in range(0, NUM_OF_HANDS_AND_CARDS):
                            if self.view.player_1_area[i].collidepoint(pos):
                                if self._player_1_cards[i].getHand().__len__() < 5:
                                    self._player_1_cards[i].addCard(card)
                                    cardsCount = cardsCount + 1
                                    player1Turn = False
                                    needToDrawCard = True
                                    self.refreshCards(screen)
                                    pygame.display.update()
                                break
                    else:
                        for i in range(0, NUM_OF_HANDS_AND_CARDS):
                            if self.view.player_2_area[i].collidepoint(pos):
                                if self._player_2_cards[i].getHand().__len__() < 5:
                                    self._player_2_cards[i].addCard(card)
                                    cardsCount = cardsCount + 1
                                    player1Turn = True
                                    needToDrawCard = True
                                    self.refreshCards(screen)
                                    pygame.display.update()
                                    break
            if cardsCount == 50 and not gameEnded:
                self.endOfGameActions(screen, turnTextRect, font)
                gameEnded = True
            clock.tick(60)

    def createTurnTextRect(self):
        font = pygame.font.Font('freesansbold.ttf', 14)
        turnText = font.render('', True, GREEN_COLOR, BLUE_COLOR)
        turnTextRect = turnText.get_rect()
        turnTextRect.center = (WIDTH - 100, HEIGHT // 2 + DIST_FROM_RIGHT_SIDE)
        return font, turnTextRect

    def endOfGameActions(self, screen, turnTextRect, font):
        self.displayPlayer2Cards(screen)
        turnText = font.render('Game Over', True, GREEN_COLOR, BLUE_COLOR)
        screen.blit(turnText, turnTextRect)
        gameResult = self.gamePlay.evaluateHands(self._player_1_cards, self._player_2_cards, True)
        self.view.createGameResult(screen, gameResult)
        pygame.display.update()
        print(gameResult)

    def drawNewCard(self, font, player1Turn, screen, turnTextRect):
        card = self.gamePlay.deck.dealCard()
        self.displaySideCard(screen, card)
        if player1Turn:
            turnText = font.render('Player 1 turn', True, GREEN_COLOR, BLUE_COLOR)
        else:
            turnText = font.render('Player 2 turn', True, GREEN_COLOR, BLUE_COLOR)
        screen.blit(turnText, turnTextRect)
        pygame.display.update()
        return card

    def getImgString(self, i, j, isPlayer1):
        if isPlayer1:
            return 'resources/{0}{1}.gif'.format(str(self._player_1_cards[i][j].getRank()), str(
                self._player_1_cards[i][j].getSuit()))
        else:
            if j == 4 and self._player_2_cards[i][j] is not None:
                return 'resources/backCard.gif'
            else:
                return 'resources/{0}{1}.gif'.format(str(self._player_2_cards[i][j].getRank()), str(
                    self._player_2_cards[i][j].getSuit()))

    def refreshCards(self, screen):
        for i in range(0, NUM_OF_HANDS_AND_CARDS):
            for j in range(0, NUM_OF_HANDS_AND_CARDS):
                try:
                    img_string = self.getImgString(i, j, True)
                    image = pygame.image.load(img_string)
                    screen.blit(image, ((DIST_BETWEEN_COLUMNS * (i + 1)) + (TRANS_COL_WIDTH / 4),
                                        (HEIGHT / 3) - ((j + 1) * DIST_BETWEEN_NUMBERS) + DIST_FROM_TOP + 10))
                except IndexError:
                    pass
                try:
                    img_string = self.getImgString(i, j, False)
                    image = pygame.image.load(img_string)
                    screen.blit(image, ((DIST_BETWEEN_COLUMNS * (i + 1)) + (TRANS_COL_WIDTH / 4),
                                        (HEIGHT / 3.3) + ((j + 1) * DIST_BETWEEN_NUMBERS) + DIST_FROM_BOTTOM + 10))
                except IndexError:
                    pass

    def displayPlayer2Cards(self, screen):
        lastIndex = 4
        for i in range(0, NUM_OF_HANDS_AND_CARDS):
            try:
                img_string = 'resources/{0}{1}.gif'.format(str(self._player_2_cards[i][lastIndex].getRank()),
                                                           str(self._player_2_cards[i][lastIndex].getSuit()))
                image = pygame.image.load(img_string)
                screen.blit(image, ((DIST_BETWEEN_COLUMNS * (i + 1)) + (TRANS_COL_WIDTH / 4),
                                    (HEIGHT / 3.3) + ((lastIndex + 1) * DIST_BETWEEN_NUMBERS) + DIST_FROM_BOTTOM + 10))
            except IndexError:
                pass

    def displaySideCard(self,screen, card):
        if card is None:
            SIDE_CARD_IMG = pygame.image.load('resources/backCard.gif')
            screen.blit(SIDE_CARD_IMG, (WIDTH - DIST_FROM_RIGHT_SIDE, HEIGHT // 2))
        else:
            try:
                img_string = 'resources/{0}{1}.gif'.format(str(card.getRank()), str(card.getSuit()))
                image = pygame.image.load(img_string)
                screen.blit(image, (WIDTH - DIST_FROM_RIGHT_SIDE, HEIGHT // 2))
            except IndexError:
                pass


if __name__ == '__main__':
    play = Play()
    view = GameView()
    game = GameController(play, view, play.__getPlayer1Hands__(), play.__getPlayer2Hands__())
    game.start()
