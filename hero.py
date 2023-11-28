import pygame

pygame.init()

SCREEN_HEIGH = 600 
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
clock = pygame.time.Clock()

class Hero:
    def __init__(self, sprite_sheet, start_x, start_y):
        self.sprite_sheet = sprite_sheet
        self.x = start_x
        self.y = start_y
        self.frame = 1
        self.direction = "right"

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = "left"
            if self.x - 5 > 0:
                self.x -= 5
                self.frame += 1
                if self.frame == 10:
                    self.frame = 1
                    
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            if self.x + 5 < SCREEN_WIDTH - 64:
                self.x += 5
                self.frame += 1
                if self.frame == 10:
                    self.frame = 1
        else:
            self.frame = 0

    def render(self, surface):
        if self.direction == "right":
            if self.frame == 0:
                surface.blit(self.sprite_sheet, (self.x, self.y), (0, 0, 64, 129))
            else:
                surface.blit(self.sprite_sheet, (self.x, self.y), (self.frame * 64, 0, 64, 129))
        elif self.direction == "left":
            if self.frame == 0:
                surface.blit(self.sprite_sheet, (self.x, self.y), (0, 129, 64, 129))
            else:
                surface.blit(self.sprite_sheet, (self.x, self.y), (self.frame * 64, 129, 64, 129))

def main():
    sprite_sheet = pygame.image.load("walking_animation.png")
    hero = Hero(sprite_sheet, 0, SCREEN_HEIGH - 129)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        hero.update()
        screen.fill((0, 0, 0))
        hero.render(screen)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
