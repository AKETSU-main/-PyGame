import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    speed = 10
    dt = 0
    fps = 30
    r = 0
    flag = False
    while running:
        screen.fill("blue")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = event.pos
                flag = True
                r = 0
        if flag:
            pygame.draw.circle(screen, "yellow", pos, r)
            r += speed
        pygame.display.flip()
        dt = speed * clock.tick(fps) / 1000

    pygame.quit()
