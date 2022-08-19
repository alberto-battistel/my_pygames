import pygame

pygame.font.init()

pygame.init()

screen_size = {'width':1280, 
               'height':800,
               }

FPS = 60

SCREENRECT = pygame.Rect(0,0,1024,800)
#window_style = pygame.FULLSCREEN if self.fullscreen else 0
window_style = 0
# We want 32 bits of color depth
bit_depth = pygame.display.mode_ok(SCREENRECT.size, window_style, 32)
screen = pygame.display.set_mode(SCREENRECT.size, window_style, bit_depth)

#WIN = pygame.display.set_mode((screen_size['width'], screen_size['height']))
pygame.display.set_caption("First Game!")

clock = pygame.time.Clock()

run = True
while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
