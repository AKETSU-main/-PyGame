# Example file showing a circle moving on screen
import pygame


class Board:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def draw_board(self, screen, x, y):
        pygame.draw.rect(screen, pygame.Color('white'), (
            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), self.board[x][y])

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                self.draw_board(screen, x, y)

    def set_view(self, left, top, cell_size):
        self.left, self.top, self.cell_size = left, top, cell_size

    def get_click(self, pos, screen):
        cell = self.get_cell(pos)
        self.on_click(cell, screen)

    def get_cell(self, pos):
        x = (pos[0] - self.left) // self.cell_size
        y = (pos[1] - self.top) // self.cell_size
        if 0 < x + 1 <= self.width and 0 < y + 1 <= self.height:
            return x, y

    def on_click(self, cell, screen):
        print(f'clicked {cell}')
        print(self.board)
        if self.board[cell[0]][cell[1]] == 0:
            self.board[cell[0]][cell[1]] = 1

        else:
            self.board[cell[0]][cell[1]] = 0

        self.render(screen)


# pygame setup
def main():
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board(8, 8)
    board.set_view(50, 50, 50)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos, screen)
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
