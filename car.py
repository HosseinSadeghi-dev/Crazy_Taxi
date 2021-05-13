import random
import time

import pygame
import main


class Car:
    def __init__(self):
        self.speed = 5

        self.image = pygame.transform.scale(self.image, (64, 128))
        self.d_x = self.d_x
        self.d_y = self.d_y
        self.x = random.randint(32, main.Game.width - self.image.get_width() - 32)
        self.y = self.y

    def show(self):
        main.Game.screen.blit(self.image, [self.x, self.y])

    def move(self, d_x=None, d_y=None):
        # user car move
        if (d_x is not None) and (d_y is not None):
            self.d_x = d_x
            self.d_y = d_y
        else:
            pass
            # if self.y > main.Game.height / 3 and (self.d_x != 0):
            #     self.d_x = random.choice([-1, 0, 1])

        self.x += self.d_x * self.speed
        self.y += self.d_y * self.speed

        # stay in road
        # 32 is roadside width
        if not 32 < self.x < main.Game.width - self.image.get_width() - 32:
            self.x -= self.d_x * self.speed
        # just for user to stay in Y axis of road
        if (not 0 < self.y < main.Game.height - self.image.get_height()) and (d_x is not None) and (d_y is not None):
            self.y -= self.d_y * self.speed

    def check_crashed(self, cpu_cars):
        for car in cpu_cars:
            if pygame.Rect(
                    self.x, self.y, 50, 100).colliderect(pygame.Rect(car.x, car.y, 50, 100)):
                main.Game.sound.stop()
                pygame.mixer.Sound('assets/Sounds/crash1.wav').play()
                time.sleep(2.5)
                return True


class Lamborghini(Car):
    def __init__(self):
        self.image = pygame.image.load('assets/images/lamborghini.png')
        self.y = main.Game.height - self.image.get_height() / 2
        self.d_x = 0
        self.d_y = 0
        Car.__init__(self)


class PassingCar(Car):
    def __init__(self):
        images = ['black', 'blue', 'purple', 'red']
        self.image = pygame.image.load(f'assets/images/{random.choice(images)} car.png')
        self.image = pygame.transform.flip(self.image, False, True)
        self.y = 0
        self.d_x = 0
        self.d_y = 1
        Car.__init__(self)
