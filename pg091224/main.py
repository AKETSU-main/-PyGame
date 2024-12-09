# Example file showing a circle moving on screen
import pygame

# pygame setup
if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    speed = 150
    dt = 0
    fps = 60
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 1000)

    # while running:
    #     screen.fill("purple")
    #     # poll for events
    #     # pygame.QUIT event means the user clicked X to close your window
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEMOTION:
    #             pygame.draw.circle(screen, "red", event.pos, 40)
    #             pygame.draw.circle(screen, "red", (event.pos[0], width - event.pos[1]), 40)
    #             pygame.draw.circle(screen, "red", (height - event.pos[0], event.pos[1]), 40)
    #         if event.type == MYEVENTTYPE:
    #             print('Hello')
    screen2 = pygame.Surface(screen.get_size())
    x1, y1, w, h = 0, 0, 0, 0
    drawing = False  # режим рисования выключен
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True  # включаем режим рисования
                # запоминаем координаты одного угла
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                # сохраняем нарисованное (на втором холсте)
                screen2.blit(screen, (0, 0))
                drawing = False
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                # запоминаем текущие размеры
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
        # рисуем на экране сохранённое на втором холсте
        screen.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        if drawing:  # и, если надо, текущий прямоугольник
            if w > 0 and h > 0:
                pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
            if w < 0 and h < 0:
                pygame.draw.rect(screen, (0, 0, 255), ((x1 + w, y1 + h), (abs(w), abs(h))), 5)
        pygame.display.flip()
        # fill the screen with a color to wipe away anything from last frame

        # flip() the display to put your work on screen
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000

    pygame.quit()
