import pygame
import numpy as np
import scipy.special as sp


pygame.init()
exit=False
WIDTH,HEIGHT=1000,800
canvas=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Pendel")
balls=[]
g=981
l=200
font=pygame.font.SysFont("arial",25)
font1=pygame.font.SysFont("arial",20)
icon=pygame.image.load("IconSkaliert.png")
pygame.display.set_icon(icon)
ic=0
thetag=45
theta0=np.radians(thetag)
while not exit:
    canvas.fill("white")
    if len(balls)>0:
        text_surface=font.render("Länge="+str(l)+"cm",True,"black")
        text_rect=text_surface.get_rect(center=(95,40))
        canvas.blit(text_surface,text_rect)
        text_surface=font.render("Anzahl Pendel: "+str(len(balls)),True,"black")
        text_rect=text_surface.get_rect(center=(105,60))
        canvas.blit(text_surface,text_rect)
        text_surface=font.render("Auslenkungswinkel: "+str(thetag)+"°",True,"black")
        text_rect=text_surface.get_rect(center=(135,80))
        canvas.blit(text_surface,text_rect)
    tick=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                cor=pygame.mouse.get_pos()
                balls.append({"x0":cor[0],"y0":cor[1],"t0":tick})
            if event.button==3:
                cor2=pygame.mouse.get_pos()
                ic+=1
            if event.button==4:
                if thetag<180:
                    thetag+=5
                    theta0=np.radians(thetag)
            if event.button==5:
                if thetag>0:
                    thetag-=5
                    theta0=np.radians(thetag)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                if len(balls)>0:
                    balls.pop(len(balls)-1)
            if event.key==pygame.K_DELETE:
                balls=[]
            if event.key==pygame.K_LEFT:
                if l>10:
                    l=l-10
            if event.key==pygame.K_RIGHT:
                l=l+10
        if event.type==pygame.VIDEORESIZE:
            WIDTH=event.w
            HEIGHT=event.h   
    if ic%2 !=0 :
        r=pygame.Rect(cor2[0]-200,cor2[1]-50,400,250)
        pygame.draw.rect(canvas,"grey90",r,0)
        text_surface=font1.render("Delete drücken um Pendel zu löschen",True,("black"))
        text_rect=text_surface.get_rect(center=(cor2))
        canvas.blit(text_surface,text_rect)
        text_surface=font1.render("Zurück drücken um letztes Pendel zu löschen",True,("black"))
        text_rect=text_surface.get_rect(center=(cor2[0],cor2[1]+30))
        canvas.blit(text_surface,text_rect)
        text_surface=font1.render("Hoch scrollen um Auslenkungswinkel zu erhöhen",True,("black"))
        text_rect=text_surface.get_rect(center=(cor2[0],cor2[1]+60))
        canvas.blit(text_surface,text_rect)
        text_surface=font1.render("Runter scrollen um Auslenkungswinkel zu verkleinern",True,("black"))
        text_rect=text_surface.get_rect(center=(cor2[0],cor2[1]+90))
        canvas.blit(text_surface,text_rect)
        text_surface=font1.render("Pfeiltaste Rechts um Länge zu erhöhen",True,("black"))
        text_rect=text_surface.get_rect(center=(cor2[0],cor2[1]+120))
        canvas.blit(text_surface,text_rect)
        text_surface=font1.render("Pfeiltaste Links um Länge zu verkleinern",True,("black"))
        text_rect=text_surface.get_rect(center=(cor2[0],cor2[1]+150))
        canvas.blit(text_surface,text_rect)
    for ball in balls:
        u=np.sqrt(g/l)*(tick-ball["t0"])/1000
        k=np.sin(theta0/2)
        sn, cn, dn, am = sp.ellipj(u, k)
        theta=2*np.arcsin(k*sn)
        x=l*np.sin(theta)
        y=l*np.cos(theta)

        ort=(ball["x0"]+x,ball["y0"]+y)
        pygame.draw.line(canvas,"black",(ball["x0"],ball["y0"]), ort,10)
        pygame.draw.circle(canvas,"black",(ball["x0"],ball["y0"]),10)
        pygame.draw.circle(canvas,"red",ort,30)


    pygame.display.update()
