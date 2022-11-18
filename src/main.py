import pygame

def start_game():
    """
    starts the game
    """

    setup_pygame()
    run = True
    while run:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    run = False
                    pygame.quit()
                    
                case pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    print(event.button)
                    if event.button == 1:
                        print(f"clicked on {event.pos}")


def setup_gameboard():
    cells = []
    

def setup_pygame():
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Conways game of life")

    clock = pygame.time.Clock()
    clock.tick(FRAMERATE)
    print(clock)
    rectangle3 = pygame.Rect(10, 30, 50, 70)
    pygame.draw.rect(WINDOW, (123, 221, 123), rectangle3)
    pygame.display.flip()
    print(clock)

    return WINDOW

def main():
    start_game()

if __name__ == "__main__":
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 820

    CAMERA_ZOOM = 1
    CAMERA_OFFSET = [0, 0]

    FRAMERATE = 60
    main()

