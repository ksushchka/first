import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    screen.fill('blue')
    clock = pygame.time.Clock()

    running = True
    running1 = False
    pos = (-1, -1)
    n = 20
    while running:  # главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                n = 20
                running1 = True
        while running1:
            pygame.draw.circle(screen, pygame.Color('yellow'),
                               pos, n)
            pygame.display.flip()
            clock.tick(10)
            n += 10
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    running1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill('blue')
                    pos = event.pos
                    n = 20
                    pygame.display.flip()
        pygame.display.flip()
    pygame.quit()