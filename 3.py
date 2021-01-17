# импорт нужных нам библиотек
import os
import pygame

# инициализация игрового цикла
pygame.init()

# установка размеров окна
size = width, height = 560, 670
screen = pygame.display.set_mode(size)

# установка названия окна
pygame.display.set_caption('Pacman')

# создаем точку отсчета времени
clock = pygame.time.Clock()

# переменная, отвечающая за отображение очков
score = 0

all_sprites = pygame.sprite.Group()


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


# создание верхнего коллайдера
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
        super().__init__(all_sprites)
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


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 1],
                      [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                      [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                      [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                      [1, 4, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 4, 1],
                      [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                      [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                      [1, 2, 2, 2, 2, 2, 4, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 4, 2, 2, 2, 2, 2, 1],
                      [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 2, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                      [1, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 1, 1, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                      [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                      [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                      [1, 2, 2, 2, 1, 1, 4, 2, 2, 4, 2, 2, 2, 0, 0, 0, 0, 0, 4, 0, 0, 4, 1, 1, 2, 2, 2, 1],
                      [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
                      [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
                      [1, 2, 2, 4, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 4, 2, 2, 1],
                      [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                      [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                      [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.start = False
        self.left = 10
        self.top = 10
        self.cell_size = 20

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 2 or self.board[y][x] == 4:
                    pygame.draw.rect(screen, pygame.Color(253, 189, 150),
                                     (x * self.cell_size + \
                                      self.cell_size // 2 - 3,
                                      y * self.cell_size + \
                                      self.cell_size // 2 - 3, 6,
                                      6), 0)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] // self.cell_size > self.width - 1 or \
                mouse_pos[1] // self.cell_size > self.height - 1:
            return None
        return (mouse_pos[0] // self.cell_size, mouse_pos[1] // self.cell_size)

    def om_nom_nom(self, pos):
        try:
            global score
            if self.board[pos[1] // self.cell_size] \
                    [pos[0] // self.cell_size] == 2:
                self.board[pos[1] // self.cell_size] \
                    [pos[0] // self.cell_size] = 0
                score += 10
            if self.board[pos[1] // self.cell_size] \
                    [pos[0] // self.cell_size] == 4:
                self.board[pos[1] // self.cell_size] \
                    [pos[0] // self.cell_size] = 3
                score += 10
        except:
            pass


class Blinky(AnimatedSprite):
    def __init__(self, sheet, columns, rows, x, y):
        self.frame = 0
        self.dest = 'up'
        super().__init__(sheet, columns, rows, x, y)

    def update(self):
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0
        self.image = self.frames[self.frame]
        self.mask = pygame.mask.from_surface(self.image)


class Pacman(AnimatedSprite):
    def __init__(self, sheet, columns, rows, x, y):
        self.angle = 0
        self.next_ang = 0
        super().__init__(sheet, columns, rows, x, y)

    def move(self):
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
                self.rect = self.rect.move(0, -1)
            else:
                self.image = self.frames[1]
                self.image = pygame.transform.rotate(self.image, self.angle)
        elif self.angle == -90:
            if not pygame.sprite.collide_mask(self, up_collider):
                self.rect = self.rect.move(0, 1)
            else:
                self.image = self.frames[1]
                self.image = pygame.transform.rotate(self.image, self.angle)

        if self.rect.x < -34:
            self.rect.x = 561
        elif self.rect.x > 560:
            self.rect.x = -34

    def rot(self, angle):
        self.next_ang = angle

    def where(self):
        return (self.rect.x + 17, self.rect.y + 17)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)


blinky = Blinky(load_image("blinky.png"), 4, 2, 264, 453.5)
pacman = Pacman(load_image("pacman2.png"), 4, 1, 264, 453.5)

up_collider = Up_Collider()
down_collider = Down_Collider()
left_collider = Left_Collider()
right_collider = Right_Collider()
Lab(all_sprites)
board = Board(28, 31)
fps = 140
tick = 0
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.rot(180)
            if event.key == pygame.K_RIGHT:
                pacman.rot(0)
            if event.key == pygame.K_UP:
                pacman.rot(90)
            if event.key == pygame.K_DOWN:
                pacman.rot(-90)
    if tick == 2:
        # blinky.update()
        pacman.update()
    pacman.move()
    # blinky.move()
    board.render(screen)
    board.om_nom_nom(pacman.where())

    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {str(score)}", True, (0, 255, 0))
    text_x = 0
    text_y = 630
    text_w = text.get_width()
    text_h = text.get_height()

    screen.blit(text, (text_x + 50, text_y))
    tick += 1
    if tick > 4:
        tick = 0
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
