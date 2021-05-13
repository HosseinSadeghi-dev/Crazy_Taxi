import random
import time
import pygame
import car
from shared.color import Color


class Game:
    # accord to picture ratio
    pygame.init()
    height = 900
    width = 500
    background = pygame.transform.scale(pygame.image.load('assets/Images/road.png'), (width, height))
    sound = pygame.mixer.Sound('assets/Sounds/chase.mp3')
    bg1_position = 0
    bg2_position = -background.get_height()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Crazy Taxi')
    clock = pygame.time.Clock()
    fps = 60
    start_time = None

    @staticmethod
    def play():
        pygame.init()
        Game.start_time = time.time()
        Game.sound.play()
        pygame.key.set_repeat(1, 25)

        my_car = car.Lamborghini()
        cpu_cars = []

        while True:

            Game.bg1_position += 10
            Game.bg2_position += 10

            if Game.bg1_position > Game.background.get_height():
                Game.bg1_position = -Game.background.get_height()

            if Game.bg2_position > Game.background.get_height():
                Game.bg2_position = -Game.background.get_height()

            # win.blit(bg, (bgX, 0))  # draws our first bg image
            # win.blit(bg, (bgX2, 0))
            Game.screen.blit(Game.background, [0, Game.bg1_position])
            Game.screen.blit(Game.background, [0, Game.bg2_position])

            for event in pygame.event.get():
                # move with keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        my_car.move(1, 0)
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        my_car.move(-1, 0)
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        my_car.move(0, -1)
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        my_car.move(0, 1)
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    Game.sound.stop()
                    del my_car
                    del cpu_cars
                    Game.gameover()

            my_car.show()

            if len(cpu_cars) < random.choice([1, 2, 3]):
                if random.random() < 0.05:
                    cpu_cars.append(car.PassingCar())

            for cpu_car in cpu_cars:
                cpu_car.move()
                cpu_car.show()
                if cpu_car.y > Game.height + 1:
                    cpu_cars.remove(cpu_car)

            if my_car.check_crashed(cpu_cars):
                del my_car
                del cpu_cars
                Game.gameover()

            pygame.display.update()
            Game.clock.tick(Game.fps)

    @staticmethod
    def intro():
        pygame.init()
        pygame.mouse.set_visible(False)
        font = pygame.font.Font('assets/fonts/arial.ttf', 30)
        run_game = False

        while not run_game:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_KP_ENTER) or (event.key == 13):
                        pygame.mixer.Sound('assets/Sounds/engine start.wav').play()
                        run_game = True
                        break
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    exit()

            txt_1 = font.render(f"Press Enter To Start Engine", True, (255, 255, 255))
            text_1 = txt_1.get_rect(center=(Game.width / 2, Game.height / 2))

            Game.screen.fill(Color.black)
            Game.screen.blit(txt_1, text_1)
            pygame.display.update()

        time.sleep(2.5)
        Game.play()

    @staticmethod
    def gameover():
        pygame.init()
        Game.sound.stop()
        # font = pygame.font.Font(pygame.font.match_font('arial'), 30)
        font = pygame.font.Font('assets/fonts/arial.ttf', 30)

        alert = font.render(f"GAMEOVER !!!", True, (255, 255, 255))
        alert_box = alert.get_rect(center=(Game.width / 2, Game.height / 2 - 70))

        score = font.render(f'Time Survived : {round(time.time() - Game.start_time, 1)}s', True, (255, 255, 255))
        score_box = score.get_rect(center=(Game.width / 2, Game.height / 2 - 30))

        txt = font.render(f"Press Enter To PLAY AGAIN", True, (255, 255, 255))
        text = txt.get_rect(center=(Game.width / 2, Game.height / 2 + 30))

        txt_1 = font.render(f"Press Esc To Exit", True, (255, 255, 255))
        text_1 = txt_1.get_rect(center=(Game.width / 2, Game.height / 2 + 70))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or event.key == 13:
                        main()
                if event.type == pygame.QUIT:
                    exit()
            Game.screen.fill(Color.black)

            Game.screen.blit(alert, alert_box)
            Game.screen.blit(score, score_box)
            Game.screen.blit(txt, text)
            Game.screen.blit(txt_1, text_1)
            pygame.display.update()


def main():
    Game.intro()


if __name__ == "__main__":
    main()
