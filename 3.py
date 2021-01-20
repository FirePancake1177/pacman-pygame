# импорт нужны нам библиотек
import os
import pygame

# инициализация игрового цикла
pygame.init()

# установка размеров окна
size = width, height = 560, 670
screen = pygame.display.set_mode(size)

# установка названия окна
pygame.display.set_caption('Pacman')

# переменная, отвечающая за отображение очков
score = 0

# группа спрайтов
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
end_game = pygame.sprite.Group()
life1 = pygame.sprite.Group()
life2 = pygame.sprite.Group()
life3 = pygame.sprite.Group()
lives = 3


# функция для загрузки изображения из локального хранилища
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)

    except pygame.error as message:

        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


# создание класса Lab
class Lab(pygame.sprite.Sprite):
    image = load_image("lab.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Lab.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Life1(pygame.sprite.Sprite):
    image = load_image("life.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Life1.image
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 625


class Life2(pygame.sprite.Sprite):
    image = load_image("life.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Life2.image
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 625


class Life3(pygame.sprite.Sprite):
    image = load_image("life.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Life3.image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 625


class Up_Collider(pygame.sprite.Sprite):
    image = load_image("up_collider.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Up_Collider.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0


# создание нижнего коллайдера

class Down_Collider(pygame.sprite.Sprite):
    image = load_image("down_collider.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Down_Collider.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0


# создание левого коллайдера

class Left_Collider(pygame.sprite.Sprite):
    image = load_image("left_collider.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Left_Collider.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0


# создание правого коллайдера

class Right_Collider(pygame.sprite.Sprite):
    image = load_image("right_collider.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Right_Collider.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0


# создание главного класса спрайтов

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites2)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


# создаем класс Board
class Board:

    # конструктор класса
    def __init__(self, width1, height1):
        # ширина поля
        self.width = width1

        # высота поля
        self.height = height1

        # само игровое поле
        self.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 4,
             2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 1, 2, 1],
            [1, 4, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4,
             2, 2, 2, 2, 4, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2,
             1, 1, 1, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2,
             1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 4, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 4,
             2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2,
             1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
             1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
             1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
             1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 4,
             0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
             1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
             1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 2,
             1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2,
             1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2,
             1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 1, 1, 2, 2, 2, 4, 2, 2, 2,
             2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 1, 1, 4, 2, 2, 4, 2, 2, 2, 0, 0, 0, 0, 0, 4, 0, 0, 4,
             1, 1, 2, 2, 2, 1],
            [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2,
             1, 1, 2, 1, 1, 1],
            [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2,
             1, 1, 2, 1, 1, 1],
            [1, 2, 2, 4, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2,
             2, 2, 4, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2,
             2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1]]

        # прочие характеристики (размер клетки, координаты)
        self.start = False
        self.left = 10
        self.top = 10
        self.cell_size = 20

    def render(self, screen1):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 2 or self.board[y][x] == 4:
                    pygame.draw.rect(screen1, pygame.Color(253, 189, 150),
                                     (x * self.cell_size
                                      + self.cell_size // 2 - 3,
                                      y * self.cell_size
                                      + self.cell_size // 2 - 3, 6,
                                      6), 0)

    def get_cell_num(self, cell_num):
        return self.board[cell_num[0]][cell_num[1]]

    def get_cell(self, pos):
        if pos[0] // self.cell_size > self.width - 1 or \
                pos[1] // self.cell_size > self.height - 1:
            return None
        return pos[0] // self.cell_size, pos[1] // self.cell_size

    def scoring(self, pos):
        try:
            global score
            if self.board[pos[1] //
                          self.cell_size][pos[0] // self.cell_size] == 2:
                self.board[pos[1]
                           // self.cell_size][pos[0] // self.cell_size] = 0
                score += 10
            if self.board[pos[1]
                          // self.cell_size][pos[0] // self.cell_size] == 4:
                self.board[pos[1]
                           // self.cell_size][pos[0] // self.cell_size] = 3
                score += 10
        except:
            pass


# класс призрака
class Blinky(AnimatedSprite):
    def __init__(self, sheet, columns, rows, x, y):
        self.frame = 0
        self.destination = 'right'
        super().__init__(sheet, columns, rows, x, y)

    def restart(self):
        self.rect.x = 264
        self.rect.y = 455

    def update(self):
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0

        if self.destination == 'right':
            self.frame2 = self.frame
        elif self.destination == 'left':
            self.frame2 = self.frame + 2
        elif self.destination == 'up':
            self.frame2 = self.frame + 4
        elif self.destination == 'down':
            self.frame2 = self.frame + 6

        self.image = self.frames[self.frame2]
        self.mask = pygame.mask.from_surface(self.image)

    def check(self):
        cell = board.get_cell((self.rect.x, self.rect.y + 15))
        pac = pacman.where()
        if board.get_cell_num((cell[1], cell[0] + 1)) != 1:
            dist1 = (((cell[0] + 1) * 20 - pac[0]) ** 2 + (cell[1] * 20 + 17 -
                                                           pac[1]) ** 2) ** 0.5
        else:
            dist1 = 1000
        if board.get_cell_num((cell[1], cell[0] - 1)) != 1:
            dist2 = (((cell[0] - 1) * 20 - pac[0]) ** 2 + (cell[1] * 20 + 17 -
                                                           pac[1]) ** 2) ** 0.5
        else:
            dist2 = 1000
        if board.get_cell_num((cell[1] + 1, cell[0])) != 1:
            dist3 = ((cell[0] * 20 - pac[0]) ** 2 + ((cell[1] + 1) * 20 + 17 -
                                                     pac[1]) ** 2) ** 0.5
        else:
            dist3 = 1000
        if board.get_cell_num((cell[1] - 1, cell[0])) != 1:
            dist4 = ((cell[0] * 20 - pac[0]) ** 2 + ((cell[1] - 1) * 20 + 17 -
                                                     pac[1]) ** 2) ** 0.5
        else:
            dist4 = 1000

        if dist1 == min(dist1, dist2, dist3, dist4):
            self.destination = 'right'
            # self.rect = self.rect.move(1, 0)
        elif dist2 == min(dist1, dist2, dist3, dist4):
            self.destination = 'left'
            # self.rect = self.rect.move(-1, 0)
        elif dist3 == min(dist1, dist2, dist3, dist4):
            self.destination = 'down'
            # self.rect = self.rect.move(0, 1)
        elif dist4 == min(dist1, dist2, dist3, dist4):
            self.destination = 'up'
            # self.rect = self.rect.move(0, -1)

    def where(self):
        return self.rect.x + 10, self.rect.y + 15

    def move(self):
        cell = board.get_cell((self.rect.x, self.rect.y + 15))
        if self.destination == 'right':
            if board.get_cell_num((cell[1], cell[0])) != 4 and \
                    board.get_cell_num((cell[1], cell[0])) != 3:
                self.rect = self.rect.move(1, 0)
            else:
                blinky.check()
        elif self.destination == 'left':
            if board.get_cell_num((cell[1], cell[0])) != 4 and \
                    board.get_cell_num((cell[1], cell[0])) != 3:
                self.rect = self.rect.move(-1, 0)
            else:
                blinky.check()
        elif self.destination == 'up':
            if board.get_cell_num((cell[1], cell[0])) != 4 and \
                    board.get_cell_num((cell[1], cell[0])) != 3:
                self.rect = self.rect.move(0, 1)
            else:
                blinky.check()
        elif self.destination == 'down':
            if board.get_cell_num((cell[1], cell[0])) != 4 and \
                    board.get_cell_num((cell[1], cell[0])) != 3:
                self.rect = self.rect.move(0, -1)
            else:
                blinky.check()


# создание класса Пакмана
class Pacman(AnimatedSprite):

    # инициализация класса
    def __init__(self, sheet, columns, rows, x, y):
        self.angle = 0
        self.next_ang = 0
        super().__init__(sheet, columns, rows, x, y)

    def restart(self):
        self.rect.x = 294
        self.rect.y = 453.5

    def move(self):

        # функция поворота
        if self.next_ang != self.angle:
            if self.next_ang == 90:
                if not pygame.sprite.collide_mask(self, down_collider):
                    self.angle = self.next_ang
            elif self.next_ang == -90:
                if not pygame.sprite.collide_mask(self, up_collider):
                    self.angle = self.next_ang
            elif self.next_ang == 0:
                if not pygame.sprite.collide_mask(self, left_collider):
                    self.angle = self.next_ang
            elif self.next_ang == 180:
                if not pygame.sprite.collide_mask(self, right_collider):
                    self.angle = self.next_ang

        if self.angle == 0:
            if not pygame.sprite.collide_mask(self, left_collider):
                self.rect = self.rect.move(1, 0)
            else:
                self.image = self.frames[1]
                self.image = pygame.transform.rotate(self.image, self.angle)

        elif self.angle == 180:
            if not pygame.sprite.collide_mask(self, right_collider):
                self.rect = self.rect.move(-1, 0)
            else:
                self.image = self.frames[1]
                self.image = pygame.transform.rotate(self.image, self.angle)

        elif self.angle == 90:
            if not pygame.sprite.collide_mask(self, down_collider):
                if -34 < self.rect.x < 560:
                    self.rect = self.rect.move(0, -1)
            else:
                self.image = self.frames[1]
                self.image = pygame.transform.rotate(self.image, self.angle)

        elif self.angle == -90:
            if not pygame.sprite.collide_mask(self, up_collider):
                if -34 < self.rect.x < 560:
                    self.rect = self.rect.move(0, 1)
            else:
                self.image = self.frames[1]
                self.image = pygame.transform.rotate(self.image, self.angle)

        if self.rect.x < -34:
            self.rect.x = 561
        elif self.rect.x > 560:
            self.rect.x = -34

    # здесь реализуется возможность будущего поворота
    def rot(self, angle):
        if angle == abs(90):
            if -34 < self.rect.x < 560:
                self.next_ang = angle
        else:
            self.next_ang = angle

    # местоположение Пакмана
    def where(self):
        return self.rect.x + 17, self.rect.y + 17

    # обновление
    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)


class End_Game(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(end_game)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)


# настройка коллайдеров
up_collider = Up_Collider()
down_collider = Down_Collider()
left_collider = Left_Collider()
right_collider = Right_Collider()
pacman = Pacman(load_image("pacman2.png"), 4, 1, 294, 453.5)
blinky = Blinky(load_image("blinky.png"), 4, 2, 264, 455)
end_game_ = End_Game(load_image("end_game.png"), 9, 1, 264, 453.5)

# вызов метода класса Lab
Lab(all_sprites)
Life1(life1)
Life2(life2)
Life3(life3)
board = Board(28, 31)

# устанавливаем FPS
fps = 140

# исходный счетчик
tick = 0

# начало отсчета времени
clock = pygame.time.Clock()
pause = False
running = True

while running:
    # заливаем фон черным цветом
    screen.fill(pygame.Color("black"))

    # вызываем метод спрайтов
    all_sprites.draw(screen)

    # события игрового цикла
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # управление клавишами
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.rot(180)
            if event.key == pygame.K_RIGHT:
                pacman.rot(0)
            if event.key == pygame.K_UP:
                pacman.rot(90)
            if event.key == pygame.K_DOWN:
                pacman.rot(-90)

    # проверка счетчика
    if tick == 2:
        blinky.update()
        # end_game.update()
        pacman.update()
        end_game_.update()
        if pause:
            fps = 140
            pacman.restart()
            blinky.restart()
            pause = False
    if pacman.where() == blinky.where():
        lives -= 1
        end_game.draw(screen)
        pause = True
        fps = 30
    else:
        all_sprites2.draw(screen)
    if not pause:
        pacman.move()
        blinky.check()
        # blinky.move()
    board.render(screen)
    board.scoring(pacman.where())

    # настройка счетчика
    board.scoring(pacman.where())

    # настройка шрифта
    font = pygame.font.Font(None, 30)

    # сама надпись счета
    text = font.render(f"Score: {str(score)}", True, (0, 255, 0))

    # координаты надписи
    text_x = 0
    text_y = 630

    # высота и ширина подписи
    text_w = text.get_width()
    text_h = text.get_height()

    if lives == 3:
        life1.draw(screen)
        life2.draw(screen)
        life3.draw(screen)
    elif lives == 2:
        life1.draw(screen)
        life2.draw(screen)
    elif lives == 1:
        life1.draw(screen)
    screen.blit(text, (text_x + 50, text_y))

    # увеличиваем переменную на 1
    tick += 1

    # проверка на то, чтобы переменная была не больше 3
    if tick > 4:
        tick = 0

    # стандартная функция времени игрового цикла
    clock.tick(fps)

    # обновление экрана
    pygame.display.flip()

# завершение игрового события
pygame.quit()
