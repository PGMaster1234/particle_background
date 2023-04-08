import pygame
import random
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()
screen2 = pygame.Surface((screen_width, screen_height))

clock = pygame.time.Clock()

particles = []

font12 = pygame.font.Font("freesansbold.ttf", 15)
showing_stats = True

max_up = False
max_down = False
num_up = False
num_down = False

squares = False


class StartingColor:
    def __init__(self):
        pass
    r = 1
    g = 1
    b = 1


class EndingColor:
    def __init__(self):
        pass
    r = 161
    g = 129
    b = 184


red_increasing_by = 1
green_increasing_by = 1
blue_increasing_by = 1

number_of_circles = 10
min_width_of_particles = 1
max_width_of_particles = 40

min_particle_speed = 2
max_particle_speed = 10
speed_up = False
speed_down = False

pr = 0
pg = 0
pb = 0

running = True
while running:

    mx, my = pygame.mouse.get_pos()

    screen.fill((50, 50, 50))
    screen2.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                max_up = True
            if event.key == pygame.K_DOWN:
                max_down = True
            if event.key == pygame.K_RIGHT:
                num_up = True
            if event.key == pygame.K_LEFT:
                num_down = True
            if event.key == pygame.K_SPACE:
                if showing_stats:
                    showing_stats = False
                else:
                    showing_stats = True
            if event.key == pygame.K_0:
                particles = []
            if event.key == pygame.K_EQUALS:
                speed_up = True
            if event.key == pygame.K_MINUS:
                speed_down = True
            if event.key == pygame.K_TAB:
                if squares:
                    squares = False
                else:
                    squares = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                max_up = False
            if event.key == pygame.K_DOWN:
                max_down = False
            if event.key == pygame.K_RIGHT:
                num_up = False
            if event.key == pygame.K_LEFT:
                num_down = False
            if event.key == pygame.K_EQUALS:
                speed_up = False
            if event.key == pygame.K_MINUS:
                speed_down = False

    for i in range(number_of_circles):
        particles.append([random.randint(-max_width_of_particles, screen_width + max_width_of_particles),
                          screen_height + max_width_of_particles,
                          random.randint(int(min_width_of_particles),
                                         int(max_width_of_particles)), 0, 0, 0,
                          random.uniform(min_particle_speed, max_particle_speed)])

    for p in particles:
        # if random.randint(0, 20) != 1:
        p[1] -= p[6]

        if p[3] < (255 - red_increasing_by):
            p[3] += red_increasing_by
        if p[4] < (255 - green_increasing_by):
            p[4] += green_increasing_by
        if p[5] < (255 - blue_increasing_by):
            p[5] += blue_increasing_by

        if squares:
            pygame.draw.rect(screen2, (p[3], p[4], p[5]),
                             pygame.Rect(p[0] - p[2], p[1] - p[2], p[2] * 2, p[2] * 2))
        else:
            pygame.draw.circle(screen2, (p[3], p[4], p[5]), (p[0], p[1]), p[2], 0)

        if p[1] < -max_width_of_particles:
            particles.remove(p)

    if max_up:
        max_width_of_particles += 1
    if max_width_of_particles > 1:
        if max_down:
            max_width_of_particles -= 1
    min_width_of_particles = max_width_of_particles / 2
    if num_up:
        number_of_circles += 1
    if number_of_circles > 1:
        if num_down:
            number_of_circles -= 1

    if speed_up:
        max_particle_speed += 0.1
    if max_particle_speed > 0.1:
        if speed_down:
            max_particle_speed -= 0.1
    min_particle_speed = max_particle_speed / 2

    average_particle_speed = (max_particle_speed + min_particle_speed) / 2
    red_increasing_by = EndingColor.r / (screen_height / average_particle_speed)
    blue_increasing_by = EndingColor.g / (screen_height / average_particle_speed)
    green_increasing_by = EndingColor.b / (screen_height / average_particle_speed)

    if showing_stats:
        screen2.blit(font12.render('Max Particle Size', True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3))
        screen2.blit(font12.render('Number Of Particles', True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 40))
        screen2.blit(font12.render(str(max_width_of_particles), True, (255, 255, 255)),
                     (screen_width/4 * 3 + 100, screen_height/4 * 3 + 20))
        screen2.blit(font12.render(str(number_of_circles), True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 60))
        fps = clock.get_fps()
        fps_rounded = round(fps * 10000000) / 10000000
        screen2.blit(font12.render('Fps', True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 80))
        screen2.blit(font12.render(str(fps_rounded), True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 100))
        screen2.blit(font12.render('Particle Speed', True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 120))
        screen2.blit(font12.render(str(max_particle_speed), True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 140))
        screen2.blit(font12.render('Total Number of Particles', True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 160))
        screen2.blit(font12.render(str(particles.__len__()), True, (255, 255, 255)),
                     (screen_width / 4 * 3 + 100, screen_height / 4 * 3 + 180))

        description = ['Press   [space]   to toggle stats on and off',
                       'Press   [up arrow]   to increase max particle size',
                       'Press   [down arrow]   to decrease max particle size',
                       'Press   [right arrow]   to increase the number of particles',
                       'Press   [left arrow]   to decrease the number of particles',
                       'Press   [=]   (bc + and = are on the same button) to increase particle speed',
                       'Press   [-]   to decrease particle speed',
                       'Press   [tab]   to switch between circles and squares',
                       'Changing the speed of the particles will change the color']
        y = 0
        for sentence in description:
            screen2.blit(font12.render(sentence, True, (255, 255, 255)),
                         (50, screen_height / 4 * 3 + y))
            y += 15

    screen.blit(screen2, (0, 0))

    pygame.display.update()
    clock.tick(60)
