import pygame
import scripts.balance as edit
balance = edit.READ()

pygame.init()
pygame.font.init() 
font = pygame.font.Font("data/font.ttf", 40)
window = pygame.display.set_mode((600, 610))
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
        self.textItem = item + '\n'
    def render(self):
        pygame.draw.rect(window, (0,0,0) , (self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, (255,255,255), (self.x, self.y, self.width, self.height), 3)
        window.blit(self.item, (self.x + 10, self.y + 10))
        window.blit(self.cost, (self.x +  self.width - 80, self.y + 10))
    def collision(self, mousePos):
        if (mousePos[0] > self.x and mousePos[0] < self.x + self.width and mousePos[1] > self.y and mousePos[1] < self.y + self.height):
            return True
        return False
    def changeValue(self, newVal):
        self.price = newVal
        self.cost = font.render(str(newVal), False, (255, 255, 255))

menu = [ button(50, 10, 500, 50, 3.50, "chocolate milk"),
        button(50, 70, 500, 50, 4.50, "chicken wrap"),
        button(50, 130, 500, 50, 3.0, "wedges"),
        button(50, 190, 500, 50, 1.50, "chicken strip"),
        button(50, 250, 500, 50, 3.50, "milo cup"),
        button(50, 310, 500, 50, 2.50, "orchy"),
        button(50, 370, 500, 50, 4.50, "pie"),
        button(50, 430, 500, 50, 4.00, "cheses tostie"),
        button(50, 490, 500, 50, 2.00, "bottled water"),]
changeButton = button(50, 550, 500, 50, balance, "change balance")
mouse = False

def draw():
    window.fill((0,0,0))
    for item in menu:
        item.render()
    changeButton.render()
    pygame.display.flip()

def inputHandle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
    return False

def change():
    ammount = 0
    window.fill((22, 22, 22))
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return ammount
                if event.key == pygame.K_1:
                    ammount = ammount * 10 + 0.01
                if event.key == pygame.K_2:
                    ammount = ammount * 10 + 0.02
                if event.key == pygame.K_3:
                    ammount = ammount * 10 + 0.03
                if event.key == pygame.K_4:
                    ammount = ammount * 10 + 0.04
                if event.key == pygame.K_5:
                    ammount = ammount * 10 + 0.05
                if event.key == pygame.K_6:
                    ammount = ammount * 10 + 0.06
                if event.key == pygame.K_7:
                    ammount = ammount * 10 + 0.07
                if event.key == pygame.K_8:
                    ammount = ammount * 10 + 0.08
                if event.key == pygame.K_9:
                    ammount = ammount * 10 + 0.08
                if event.key == pygame.K_0:
                    ammount = ammount * 10
    return ammount

while 1:
    mousePos = pygame.mouse.get_pos()
    draw()
    mouse = inputHandle()
    if mouse:
        for item in menu:
            if item.collision(mousePos):
                balance, banckrupt = edit.BACNKRUPT(balance, item.price)
                if not banckrupt:
                    edit.WRITE("order", item.textItem, 'a')
                    edit.WRITE("balance", balance)
                    changeButton.changeValue(balance)
        if changeButton.collision(mousePos):
            balance += round(change(), 2)
            changeButton.changeValue(balance)
    pygame.time.delay(20)
