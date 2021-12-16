import random
import pygame
pygame.init()


#set screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Turtle! Far From Home")
icon = pygame.image.load("img/turtle.png")
pygame.display.set_icon(icon)


#load sound
music = pygame.mixer.Sound('sound/bg.mp3')
music.set_volume(0.2)
music.play()
fail = pygame.mixer.Sound('sound/fail.wav')
fail.set_volume(0.2)


#load images
bg = pygame.image.load("img/greenbg.jpg")
load_player = pygame.image.load("img/turtle.png")
load_car = pygame.image.load('img/car.png')
load_car2 = pygame.image.load('img/car2.png')
load_car3 = pygame.image.load('img/car3.png')
load_car4 = pygame.image.load('img/car4.png')
load_car5 = pygame.image.load('img/car5.png')
load_car6 = pygame.image.load('img/car6.png')
load_car7 = pygame.image.load('img/car7.png')
load_car8 = pygame.image.load('img/car8.png')
load_car9 = pygame.image.load('img/car9.png')
load_car10 = pygame.image.load('img/car10.png')
goal_img = pygame.image.load('img/goal.png')
start = pygame.image.load('img/start.png')
exit = pygame.image.load('img/exit.png')
howtoplay = pygame.image.load('img/howtoplay.png')
start_img = pygame.transform.scale(start, (200, 200))
exit_img = pygame.transform.scale(exit, (200, 138))
howtoplay_img = pygame.transform.scale(howtoplay, (200, 45))
goal = pygame.transform.scale(goal_img, (50, 50))
goal_rect = goal.get_rect(topleft=[370, 10])


#player
posX = 370
posY = 600 - 60
player = pygame.transform.scale(load_player, (50, 50))
player_rect = player.get_rect(topleft=[posX, posY])
move = 2


#cars
carX = random.randint(100, 100)
carY = random.randint(50, 500)
car = pygame.transform.scale(load_car, (50, 25))
car_rect = car.get_rect(topleft=[carX, carY])
carX2 = random.randint(200, 200)
carY2 = random.randint(50, 500)
car2 = pygame.transform.scale(load_car2, (50, 25))
car2_rect = car.get_rect(topleft=[carX2, carY2])
carX3 = random.randint(300, 300)
carY3 = random.randint(50, 500)
car3 = pygame.transform.scale(load_car3, (50, 25))
car3_rect = car.get_rect(topleft=[carX3, carY3])
carX4 = random.randint(400, 400)
carY4 = random.randint(50, 500)
car4 = pygame.transform.scale(load_car4, (50, 25))
car4_rect = car.get_rect(topleft=[carX4, carY4])
carX5 = random.randint(500, 500)
carY5 = random.randint(50, 500)
car5 = pygame.transform.scale(load_car5, (50, 25))
car5_rect = car.get_rect(topleft=[carX5, carY5])
carX6 = random.randint(600, 600)
carY6 = random.randint(50, 500)
car6 = pygame.transform.scale(load_car6, (50, 25))
car6_rect = car.get_rect(topleft=[carX6, carY6])
carX7 = random.randint(700, 700)
carY7 = random.randint(50, 500)
car7 = pygame.transform.scale(load_car7, (50, 25))
car7_rect = car.get_rect(topleft=[carX7, carY7])
carX8 = random.randint(800, 800)
carY8 = random.randint(50, 500)
car8 = pygame.transform.scale(load_car8, (50, 25))
car8_rect = car.get_rect(topleft=[carX8, carY8])
carX9 = random.randint(0, 800)
carY9 = random.randint(50, 500)
car9 = pygame.transform.scale(load_car9, (50, 25))
car9_rect = car.get_rect(topleft=[carX9, carY7])
carX10 = random.randint(0, 800)
carY10 = random.randint(50, 500)
car10 = pygame.transform.scale(load_car10, (50, 25))
car10_rect = car.get_rect(topleft=[carX10, carY10])
carmove = 1


#Text and Font
level = 1
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
small_font = pygame.font.Font('freesansbold.ttf', 20)
Title_font = pygame.font.Font('freesansbold.ttf', 58)


main_menu = True


#button
class Button:
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		screen.blit(self.image, self.rect)

		return action


def show_score(x, y):
	score = font.render('Level : ' + str(level), True, (0, 0, 0))
	screen.blit(score, (x, y))


def game_over_text():
	over_text = over_font.render("GAME OVER", True, (0, 0, 0))
	screen.blit(over_text, (200, 250))


def game_over():
	game_over_text()
	music.stop()
	fail.play()


#my button
start_button = Button(800 // 2 - 100, 600 // 2 - 175, start_img)
exit_button = Button(800 // 2 - 100, 600 // 2 + 50, exit_img)


#main
run = True
while run:
	pygame.time.delay(12)
	screen.blit(bg, (0, 0))

	if main_menu == True:
		over_text = Title_font.render("TURTLE! FAR FROM HOME", True, (0, 0, 0))
		screen.blit(over_text, (15, 40))
		if exit_button.draw():
			run = False
		if start_button.draw():
			main_menu = False
		over_text = small_font.render("HOW TO PLAY : Press An Arrow Key On Your Keyboard To Control", True, (0, 0, 0))
		screen.blit(over_text, (70, 530))
		over_text = small_font.render("                          The Turtle And Get Through The Sea.", True, (0, 0, 0))
		screen.blit(over_text, (70, 555))

	else:
		screen.blit(goal, goal_rect)

		#player movement
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player_rect.x > 0:
			player_rect.x -= move
		if keys[pygame.K_RIGHT] and player_rect.x < 800-50:
			player_rect.x += move
		if keys[pygame.K_UP] and player_rect.y > 0:
			player_rect.y -= move
		if keys[pygame.K_DOWN] and player_rect.y < 600-50:
			player_rect.y += move

		#car movement
		car_rect.x -= carmove
		if car_rect.x == 0:
			car_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car2_rect.x -= carmove
		if car2_rect.x == 0:
			car2_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car3_rect.x -= carmove
		if car3_rect.x == 0:
			car3_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car4_rect.x -= carmove
		if car4_rect.x == 0:
			car4_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car5_rect.x -= carmove
		if car5_rect.x == 0:
			car5_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car6_rect.x -= carmove
		if car6_rect.x == 0:
			car6_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car7_rect.x -= carmove
		if car7_rect.x == 0:
			car7_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car8_rect.x -= carmove
		if car8_rect.x == 0:
			car8_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car9_rect.x -= carmove
		if car9_rect.x == 0:
			car9_rect = car.get_rect(topleft=[800, random.randint(50, 500)])
		car10_rect.x -= carmove
		if car10_rect.x == 0:
			car10_rect = car.get_rect(topleft=[800, random.randint(50, 500)])

		#collision conditions
		if player_rect.colliderect(goal_rect):
			level += 1
			carmove += 0.3
			player_rect = player.get_rect(topleft=[posX, posY])

		if player_rect.colliderect(car_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car2_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car3_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car4_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car5_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car6_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car7_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car8_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car9_rect):
			game_over()
			carmove = 0
			move = 0
		if player_rect.colliderect(car10_rect):
			game_over()
			carmove = 0
			move = 0

		#show score
		show_score(textX, testY)

		#display player and car images
		screen.blit(player, player_rect)
		screen.blit(car, car_rect)
		screen.blit(car2, car2_rect)
		screen.blit(car3, car3_rect)
		screen.blit(car4, car4_rect)
		screen.blit(car5, car5_rect)
		screen.blit(car6, car6_rect)
		screen.blit(car7, car7_rect)
		screen.blit(car8, car8_rect)
		screen.blit(car9, car9_rect)
		screen.blit(car10, car10_rect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	pygame.display.update()
