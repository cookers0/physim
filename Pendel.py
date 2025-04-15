import pygame
import numpy as np
import scipy.special as sp


pygame.init()
exit=False
WIDTH,HEIGHT=1000,800
canvas=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
balls=[]
g=981
l=200
font=pygame.font.Font(None,30)
while not exit:
    canvas.fill("white")
    if len(balls)>0:
        text_surface=font.render("Länge="+str(l)+"cm",True,"black")
        text_rect=text_surface.get_rect(center=(70,40))
        canvas.blit(text_surface,text_rect)
    tick=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                cor=pygame.mouse.get_pos()
                balls.append({"x0":cor[0],"y0":cor[1],"t0":tick})
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                if len(balls)>0:
                    balls.pop(len(balls)-1)
            if event.key==pygame.K_LEFT:
                if l>10:
                    l=l-10
            if event.key==pygame.K_RIGHT:
                l=l+10
        if event.type==pygame.VIDEORESIZE:
            WIDTH=event.w
            HEIGHT=event.h   
    for ball in balls:
        u=np.sqrt(g/l)*(tick-ball["t0"])/900
        k=0.4
        sn, cn, dn, am = sp.ellipj(u, k)
        x=l*np.sin(sn)
        y=l*np.cos(sn)

        ort=(ball["x0"]+x,ball["y0"]+y)
        pygame.draw.line(canvas,"black",(ball["x0"],ball["y0"]), ort,10)
        pygame.draw.circle(canvas,"black",(ball["x0"],ball["y0"]),10)
        pygame.draw.circle(canvas,"red",ort,30)


    pygame.display.update()
