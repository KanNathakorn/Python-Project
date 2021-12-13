from typing import Union
import pygame
from pygame.rect import Rect, RectType

pygame.init()

clock = pygame.time.Clock()
fps = 200

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ไว้ก่อนเหอะ')

#define game variables
tile_size = 50

#load images here naaaa
bg_img = pygame.image.load('img/whitebg.jpg')
square_img = pygame.image.load('img/square.jpg')
triangle_img = pygame.image.load('img/triangle.png')
triangle2_img = pygame.transform.rotate(triangle_img, -90)
triangle3_img = pygame.transform.rotate(triangle_img, -180)
triangle4_img = pygame.transform.rotate(triangle_img, 90)

clicked = False


def draw_grid():
    for line in range(0, 200):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


def draw_block():
    for row in range(14):
        for col in range(20):
            if world_data[row][col] > 0:
                if world_data[row][col] == 1:
                    #square blocks
                    img = pygame.transform.scale(square_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 2:
                    #triangle blocks
                    img = pygame.transform.scale(triangle_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 3:
                    img = pygame.transform.scale(triangle2_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 4:
                    img = pygame.transform.scale(triangle3_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 5:
                    img = pygame.transform.scale(triangle4_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))


#####how to move charecter automatically#####
class Player:
    rect: Union[Rect, RectType, None]

    def __init__(self, x, y):
        x = 100
        y = 700-100
        img = pygame.image.load('img/ball.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, self.rect)
        if self.rect.x > 0:
            self.rect.x += 1
        #ทำไม่เป็น
        elif self.rect.x < 500:
            self.rect.x -= 1


class World:
    def __init__(self, data):
        self.tile_list = []

        #load images
        square_img = pygame.image.load('img/square.jpg')
        triangle_img = pygame.image.load('img/triangle.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(square_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(triangle_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


world_data = [
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Player(100, screen_height - 100)
world = World(world_data)


run = True
while run:
    screen.blit(bg_img, (0, 0))
    world.draw()
    player.update()
    draw_grid()
    draw_block()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // tile_size
            y = pos[1] // tile_size
            # check that the coordinates are within the tile area
            if x < 20 and y < 14:
                # update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] += 1
                    if world_data[y][x] > 5:
                        world_data[y][x] = 0
                elif pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] -= 1
                    if world_data[y][x] < 0:
                        world_data[y][x] = 5
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
