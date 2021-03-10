import pygame


pygame.init()
pygame.font.init() #initilising pygame and pygame font
font = pygame.font.Font("data/font.ttf", 50)
smallFont = pygame.font.Font("data/font.ttf", 10) #initilising fonts from the ./data directory
window = pygame.display.set_mode((500, 300))

class button(): #button class
    def __init__(self, x, y, width, height, image, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.value = value #initilises variables of class from input
    def render(self):
        window.blit(self.image, (self.x, self.y)) #custom render function
    def collision(self, mousePosX, mousePosY):
        if (mousePosX > self.x and mousePosX < self.x + self.width and 
                mousePosY > self.y and mousePosY < self.y + self.height):
                #spliting if statment is used for clarity
            return True
        return False #checks if colliding
