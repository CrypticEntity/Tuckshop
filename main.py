import pygame

pygame.init()
pygame.font.init() 
font = pygame.font.Font("data/font.ttf", 40)
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Tuckshop")

class button():
    def __init__(self, x, y, width, height, cost, item):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cost = font.render(str(cost), False, (255, 255, 255))
        self.price = cost
        self.item = font.render(item, False, (255, 255, 255))
    def render(self):
        pygame.draw.rect(window, (0,0,0) , (self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, (255,255,255), (self.x, self.y, self.width, self.height), 3)
        window.blit(self.item, (self.x + 10, self.y + 10))
        window.blit(self.cost, (self.x +  self.width - (10 + (40 * len(str(self.price)))), self.y + 10))
    def collision(self, mousePosX, mousePosY):
        if (mousePosX > self.x and mousePosX < self.x + self.width and mousePosY > self.y and mousePosY < self.y + self.height):
            return True
        return False

menu = [ button(50, 10, 500, 50, 7, "chocolate milk"),
        ]

def draw():
    window.fill((0,0,0))
    for item in menu:
        item.render()
    pygame.display.flip()

while 1:
    draw()
