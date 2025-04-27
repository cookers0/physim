import pygame
import numpy as np
import scipy.special as sp

class Simulation2:
    def __init__(self, screen):
        self.screen = screen
        self.WIDTH,self.HEIGHT=1000,800
        self.canvas=pygame.display.set_mode((self.WIDTH,self.HEIGHT),pygame.RESIZABLE)
        pygame.display.set_caption("Pendel")
        self.balls=[]
        self.g=981
        self.l=200
        self.font=pygame.font.SysFont("arial",25)
        self.font1=pygame.font.SysFont("arial",20)
        self.ic=0
        self.thetag=45
        self.theta0=np.radians(self.thetag)
        self.cdball=0
        self.cddel=0
        self.cdtext=0
        self.cdconfig=0

    def run(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
        
        self.canvas.fill("white")
        tick=pygame.time.get_ticks()

        if len(self.balls)>0:
            text_surface=self.font.render("Länge="+str(self.l)+"cm",True,"black")
            text_rect=text_surface.get_rect(center=(95,40))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font.render("Anzahl Pendel: "+str(len(self.balls)),True,"black")
            text_rect=text_surface.get_rect(center=(105,60))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font.render("Auslenkungswinkel: "+str(self.thetag)+"°",True,"black")
            text_rect=text_surface.get_rect(center=(135,80))
            self.canvas.blit(text_surface,text_rect)
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if self.cdball == 0:
                    cor=pygame.mouse.get_pos()
                    self.balls.append({"x0":cor[0],"y0":cor[1],"t0":tick})
                    self.cdball = 20
            if event.button==3:
                if self.cdtext == 0:
                    self.cor2=pygame.mouse.get_pos()
                    self.ic+=1
                    self.cdtext = 15

        if self.cdball > 0:
            self.cdball -= 1

        if self.cdtext > 0:
            self.cdtext -= 1

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                if self.cddel == 0:
                    if len(self.balls)>0:
                        self.balls.pop(len(self.balls)-1)
                        self.cddel = 15
            if event.key==pygame.K_DELETE:
                self.balls=[]
            if event.key==pygame.K_UP:
                if self.cdconfig == 0:
                    if self.l > 10:
                        self.l=self.l - 10
                        self.cdconfig = 5
            if event.key==pygame.K_DOWN:
                if self.cdconfig == 0:
                    self.l=self.l + 10
                    self.cdconfig = 5
            if event.key==pygame.K_LEFT:
                if self.cdconfig == 0:
                    if self.thetag < 180:
                        self.thetag += 5
                        self.theta0 = np.radians(self.thetag)
                        self.cdconfig = 5
            if event.key==pygame.K_RIGHT:
                if self.cdconfig == 0:
                    if self.thetag > 0:
                        self.thetag -= 5
                        self.theta0 = np.radians(self.thetag)
                        self.cdconfig = 5

        if self.cddel > 0:
            self.cddel -= 1

        if self.cdconfig > 0:
            self.cdconfig -= 1

        if event.type==pygame.VIDEORESIZE:
            self.WIDTH=event.w
            self.HEIGHT=event.h   

        if self.ic%2 !=0 :
            r=pygame.Rect(self.cor2[0]-200,self.cor2[1]-50,400,250)
            pygame.draw.rect(self.canvas,"grey90",r,0)
            text_surface=self.font1.render("Delete drücken um Pendel zu löschen",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font1.render("Zurück drücken um letztes Pendel zu löschen",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2[0],self.cor2[1]+30))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font1.render("Pfeiltaste Links um Auslenkungswinkel zu verkleinern",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2[0],self.cor2[1]+60))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font1.render("Pfeiltaste Rechts um Auslenkungswinkel zu vergrössern",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2[0],self.cor2[1]+90))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font1.render("Pfeiltaste Oben um Länge zu erhöhen",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2[0],self.cor2[1]+120))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font1.render("Pfeiltaste Unten um Länge zu verkleinern",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2[0],self.cor2[1]+150))
            self.canvas.blit(text_surface,text_rect)
            
        for ball in self.balls:
            u=np.sqrt(self.g/self.l)*(tick-ball["t0"])/1000
            k=np.sin(self.theta0/2)
            sn, cn, dn, am = sp.ellipj(u, k)
            theta=2*np.arcsin(k*sn)
            x=self.l*np.sin(theta)
            y=self.l*np.cos(theta)

            ort=(ball["x0"]+x,ball["y0"]+y)
            pygame.draw.line(self.canvas,"black",(ball["x0"],ball["y0"]), ort,10)
            pygame.draw.circle(self.canvas,"black",(ball["x0"],ball["y0"]),10)
            pygame.draw.circle(self.canvas,"red",ort,30)

        pygame.display.update()
        return False
