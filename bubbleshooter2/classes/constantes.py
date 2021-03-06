from pygame import *
font.init()
from math import sin,cos,atan2,degrees,radians


def applies_alpha(surface1,surface2):
    output = surface2.copy().convert_alpha()
    surfarray.pixels_alpha(output)[:] = surfarray.array_alpha(surface1)
    return output

hole = image.load('res/erase.png')
star1 = image.load('res/plop.png')
star3 = image.load('res/plop3.png')
mainclock = time.Clock()


test = {    'one':image.load('res/testChar1.png'), 
            'two':image.load('res/testChar2.png'), 
            'three':image.load('res/testChar3.png'),
            'red':image.load('res/testChar2.png')   }

balls = {   'red':test['red'],
            'blu':image.load('res/bubblebleutest.png'),
            'yel':image.load('res/bubblejaunetest.png'),
            'gre':image.load('res/bubbleverttest.png'),
            'pur':image.load('res/bubbleviolettest.png'),
            'bla':image.load('res/bubblenoirtest.png'),
            'whi' :image.load('res/bubbleblanctest.png')   }

ball_rect = balls['red'].get_rect()
alpha = int(cos(radians(30))*ball_rect.height)
screen = Rect(0,0,15*ball_rect.width,16*ball_rect.height+alpha)

beta = ball_rect.centerx
gamma = ball_rect.width
delta = ball_rect.width**2*0.6
zeta = 15 * alpha
eta = 14 * alpha + ball_rect.width

scr = display.set_mode(screen.size)

bg = image.load('res/darktest.jpg').convert()
ball_rect.center = bg.fill((128,128,128),(0,eta,screen.width,2*ball_rect.width),special_flags=BLEND_ADD).center

countfont = font.Font('res/MonospaceTypewriter.ttf',24)
messfont = font.Font(None,80)
menu2font = font.Font(None,30)