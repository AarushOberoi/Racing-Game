# Endless Racing Game! - your original pygame code, adapted to run in the browser
# (runs through Pyodide + pygame-ce from index.html)
import asyncio
import random
import pygame
from js import window

pygame.init()

# Making the Display (fills the whole browser window)
w = int(window.innerWidth)
h = int(window.innerHeight)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Endless Racing Game!")
clock = pygame.time.Clock()

# Scale so cars and speeds look right on any screen size
s = min(h / 705, w / 700)
car_w = max(20, int(50 * s))
car_h = max(40, int(100 * s))

# Uploading Road Image
# (the music is played by the browser from index.html, because pygame's
# mixer does not work reliably inside the browser)
road = pygame.image.load("road.png")
road = pygame.transform.scale(road, (w, h))

# Uploading Images of Cars
mycar = pygame.image.load("car.png")
policecar = pygame.image.load("enemy_car.png")
badcars = [
    pygame.image.load("ddf.png"),
    pygame.image.load("dhd.png"),
    pygame.image.load("fdf.png"),
    pygame.image.load("xuc.png"),
    pygame.image.load("xyz.png"),
    pygame.image.load("zyz.png"),
]

# Making All Cars Small
mycar = pygame.transform.scale(mycar, (car_w, car_h))
policecar = pygame.transform.scale(policecar, (car_w, car_h))
badcars = [pygame.transform.scale(x, (car_w, car_h)) for x in badcars]

# Adding Road Boundaries (same proportions as the original 1370 wide screen)
leftroad = int(w * 250 / 1370)
rightroad = int(w * 1120 / 1370)

# Determining The Place of The Car
myx = (leftroad + rightroad) // 2
myy = h - int(120 * s)
myspeed = 6 * s

# Telling Enemies and Gap
enemys = []
gap = 150 * s

# Creating Score Calculator
font = pygame.font.Font(None, max(30, int(40 * s)))
score = 0


# Generating Random Enemies
def make_enemy():
    if random.randint(1, 8) == 1:
        img = policecar
    else:
        img = random.choice(badcars)

    for i in range(50):
        x = random.randint(leftroad, rightroad - car_w)
        y = random.randint(int(-300 * s), int(-100 * s))

        crash = False
        for e in enemys:
            ex, ey = e[1], e[2]
            if (x < ex + car_w and x + car_w > ex and y < ey + car_h + gap and y + car_h > ey):
                crash = True
                break

        if not crash:
            enemys.append([img, x, y])
            break


# Score Showing
def show_score():
    screen.fill((0, 0, 0))
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (w // 2 - text.get_width() // 2, h // 2))
    pygame.display.flip()


# Continuation of The Game
async def game():
    global myx, score, enemys
    enemys = []
    myx = (leftroad + rightroad) // 2
    run = True

    while run:
        screen.blit(road, (0, 0))

        for event in pygame.event.get():
            pass  # nothing to quit in the browser

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and myx > leftroad:
            myx -= myspeed
        if keys[pygame.K_RIGHT] and myx < rightroad - car_w:
            myx += myspeed

        if random.randint(1, 30) == 1:
            make_enemy()

        espeed = (5 + score // 10) * s

        for e in enemys:
            e[2] += espeed
            screen.blit(e[0], (e[1], e[2]))

            # Checking for a crash!
            if (myx < e[1] + car_w and myx + car_w > e[1] and myy < e[2] + car_h and myy + car_h > e[2]):
                run = False

        newlist = []
        for e in enemys:
            if e[2] >= h:
                score += 1
            else:
                newlist.append(e)
        enemys = newlist

        screen.blit(mycar, (myx, myy))

        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)  # lets the browser draw the frame


async def wait():
    show_score()
    start = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start < 10000:
        pygame.event.pump()
        await asyncio.sleep(0.1)


# Loading The Game Forever
async def main():
    global score
    while True:
        await game()
        await wait()
        score = 0
