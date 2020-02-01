import pygame


class GameView:
    _player_1_cards = []
    _player_2_cards = []

    def __init__(self, _player_1_cards, _player_2_cards):
        self._player_1_cards = _player_1_cards
        self._player_2_cards = _player_2_cards

    _player_1_cards = [['2C', '2D', '2S', '2H'], ['3C', '3D', '3S', '3H']]

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 200, 0)
    RED = (255, 0, 0)
    pygame.init()
    size = (800, 800)
    screen = pygame.display.set_mode(size)
    screen.fill(GREEN)
    pygame.display.flip()

    for i in range(len(_player_1_cards)):
        for j in range(len(_player_1_cards[i])):
            img_string = 'resources/'+ _player_1_cards[i][j] + '.gif'
            image = pygame.image.load(img_string)
            screen.blit(image, (80*j + 150, 80*i + 400))

    pygame.display.set_caption("Poker")
    # Loop until the user clicks the close button.
    done = False

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

        # --- Game logic should go here

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        # screen.fill(WHITE)

        # --- Drawing code should go here

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


    # Draw Once
    Rectplace = pygame.draw.rect(window, (255, 0, 0),(100, 100, 100, 100))
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
