# Example file showing a circle moving on screen
import pygame


class Board:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        pass


# pygame setup
def main():
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board(5, 7)
    running = True
    speed = 150
    dt = 0
    fps = 60

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        board.render(screen)
        # fill the screen with a color to wipe away anything from last frame

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
