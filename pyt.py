import pygame
from paddle import Paddle

pygame.init()

# Цвет
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Окно
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Ракетка
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Спрайты
all_sprites_list = pygame.sprite.Group()


all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# Игра до бесконечности пока игрок не нажмёт крестик //////
carryOn = True

# Обновление экрана
clock = pygame.time.Clock()

# Основной код
while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False  # Выход из цикла
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Выход из игры клавишей x
                carryOn = False

    # Дмижение платформ
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

        #  Логика
    all_sprites_list.update()


    # Чёрный экран
    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Все спрайты
    all_sprites_list.draw(screen)


    pygame.display.flip()

    #  Кадры
    clock.tick(60)

# Конец программы
pygame.quit()