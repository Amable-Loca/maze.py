# maze.py
from pygame import *
init()

ANCHO, ALTO = 765, 545
BACK_IMG = 'background.jpg'
WIN_IMG = 'vict.jpg'
HERO_IMG = 'hero.png'
COLOR = (23, 5, 135)

class GameSprite(sprite.Sprite):
    def _init_(self, img, cor_x, cor_y, speed=0):
        super()._init_()
        self.image = transform.scale(image.load(img), (80, 80))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y

    def reset(self):
        pantalla.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        llaves = key.get_pressed()
        if llaves[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if llaves[K_d] and self.rect.x < ANCHO - 80:
            self.rect.x += self.speed
        if llaves[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if llaves[K_s] and self.rect.y < ALTO - 81:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def _init_(self, color, x, y, width, height):
        super()._init_()
        self.color = color
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        pantalla.blit(self.image, (self.rect.x, self.rect.y))

# Definir múltiples paredes para el laberinto
walls = sprite.Group()
walls.add(
    Wall(COLOR, 100, 200, 10, 100),
    Wall(COLOR, 200, 100, 150, 10),
    Wall(COLOR, 300, 250, 10, 150),
    Wall(COLOR, 450, 300, 200, 10),
    Wall(COLOR, 600, 100, 10, 200),
    Wall(COLOR, 50, 400, 300, 10),
    Wall(COLOR, 400, 450, 10, 100)
)

pantalla = display.set_mode((ANCHO, ALTO))
background = transform.scale(image.load(BACK_IMG), (ANCHO, ALTO))
victoria = transform.scale(image.load(WIN_IMG), (ANCHO, ALTO))
player = Player(HERO_IMG, 50, 50, 10)

clok = time.Clock()
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        pantalla.blit(background, (0, 0))
        player.reset()
        player.update()

        # Dibujar todas las paredes
        for wall in walls:
            wall.draw()

        # Comprobar colisión con cualquier pared
        if sprite.spritecollide(player, walls, False):
            pantalla.fill((0, 0, 0))
            pantalla.blit(victoria, (0, 0))
            finish = True

    display.update()
    clok.tick(60)

quit()
