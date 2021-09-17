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
        self.cost = font.render('$'+str(cost[0])+'.'+str(cost[1]), False, (255, 255, 255))
        self.price = cost
        self.item = font.render(item, False, (255, 255, 255))
        self.textItem = item + '\n'
    def render(self):
        pygame.draw.rect(window, (0,0,0) , (self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, (255,255,255), (self.x, self.y, self.width, self.height), 3)
        window.blit(self.item, (self.x + 10, self.y + 10))
        window.blit(self.cost, (self.x + self.width - len(str(self.price)) * 20 - 30, self.y + 10))
    def collision(self, mousePos):
        if (mousePos[0] > self.x and mousePos[0] < self.x + self.width and mousePos[1] > self.y and mousePos[1] < self.y + self.height):
            return True
        return False
    def changeValue(self, newVal):
        self.price = newVal
        self.cost = font.render('$'+str(newVal[0])+'.'+str(newVal[1]), False, (255, 255, 255))

menu = [ button(50, 10, 500, 50, (3,5), "chocolate milk"),
        button(50, 70, 500, 50, (4,5), "chicken wrap"),
        button(50, 130, 500, 50, (3,0), "wedges"),
        button(50, 190, 500, 50, (1,5), "chicken strip"),
        button(50, 250, 500, 50, (3,5), "milo cup"),
        button(50, 310, 500, 50, (2,5), "orchy"),
        button(50, 370, 500, 50, (4,5), "pie"),
        button(50, 430, 500, 50, (4,0), "cheses tostie"),
        button(50, 490, 500, 50, (2,0), "bottled water"),]
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
        ammountText = font.render('$'+str(int(ammount/100))+'.'+str(ammount%100), False, (255, 255, 255))
        window.fill((22, 22, 22))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return (int(ammount / 100), ammount % 100)
                elif event.key == pygame.K_BACKSPACE:
                    ammount = int(ammount / 10)
                elif event.key == pygame.K_1:
                    ammount = ammount * 10 + 1
                elif event.key == pygame.K_2:
                    ammount = ammount * 10 + 2
                elif event.key == pygame.K_3:
                    ammount = ammount * 10 + 3
                elif event.key == pygame.K_4:
                    ammount = ammount * 10 + 4
                elif event.key == pygame.K_5:
                    ammount = ammount * 10 + 5
                elif event.key == pygame.K_6:
                    ammount = ammount * 10 + 6
                elif event.key == pygame.K_7:
                    ammount = ammount * 10 + 7
                elif event.key == pygame.K_8:
                    ammount = ammount * 10 + 8
                elif event.key == pygame.K_9:
                    ammount = ammount * 10 + 9
                elif event.key == pygame.K_0:
                    ammount *= 10
                elif event.key == pygame.K_MINUS:
                    ammount *= -1
        textX, textY = pygame.display.get_window_size()
        window.blit(ammountText, (textX/2, textY/2))
        pygame.display.flip()
    return (int(ammount / 100), ammount % 100)

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
            new = change()
            if new[1] + balance[1] > 99:
                balance = (1 + new[0] + balance[0], (new[1] + balance[1]) % 100)
            else:
                balance = (new[0] + balance[0], new[1] + balance[1])
            changeButton.changeValue(balance)
            edit.WRITE("balance", balance)
    pygame.time.delay(20)
