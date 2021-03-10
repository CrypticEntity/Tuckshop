import pygame

pygame.init()
pygame.font.init() 
font = pygame.font.Font("data/font.ttf", 50)
smallFont = pygame.font.Font("data/font.ttf", 10) 
window = pygame.display.set_mode((500, 300))

class button():
    def __init__(self, x, y, width, height, image, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.value = value
    def render(self):
        window.blit(self.image, (self.x, self.y))
    def collision(self, mousePosX, mousePosY):
        if (mousePosX > self.x and mousePosX < self.x + self.width and mousePosY > self.y and mousePosY < self.y + self.height):
            return True
        return False

menu = [ button(7, 7, 7, 7, 7, 0),
         button(7, 7, 7, 7, 7, 0)]
