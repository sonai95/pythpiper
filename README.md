import pygame, sys, random, time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

playSurface = pygame.display.set_mode((720, 300))
pygame.display.set_caption("Suvadeep's game!")

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)
yellow = pygame.Color(255, 255, 0)
fpsController = pygame.time.Clock()

snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 30) * 10]
foodSpawn = True

obstaclePos = [[random.randrange(1, 72) * 10, random.randrange(1, 30) * 10],[random.randrange(1, 72) * 10, random.randrange(1, 30) * 10]]


direction = 'RIGHT'
changeto = direction

score = 0

def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()

    time.sleep(4)
    pygame.quit()
    sys.exit()


def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_SPACE:
                pygame.time.wait(2000)

    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 30) * 10]
    foodSpawn = True

    playSurface.fill(white)

    for pos in snakeBody:
        pygame.draw.rect(playSurface, red, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    pygame.draw.rect(playSurface, yellow, pygame.Rect(obstaclePos[0][0], obstaclePos[0][1], 10, 10))
    pygame.draw.rect(playSurface, yellow, pygame.Rect(obstaclePos[1][0], obstaclePos[1][1], 10, 10))

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 290 or snakePos[1] < 0:
        gameOver()
    if snakePos[0]==obstaclePos[0][0] and snakePos[1]==obstaclePos[0][1]:
        gameOver()
    if snakePos[0]==obstaclePos[1][0] and snakePos[1]==obstaclePos[1][1]:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()

    fpsController.tick(20)
