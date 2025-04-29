import pygame
import numpy as np


class Simulation1:
    def __init__(self, screen):
        self.screen = screen
        self.radius=60
        self.font=pygame.font.Font(None,int(self.radius/3))
        self.font1=pygame.font.Font(None,20)
        self.font2=pygame.font.SysFont("arial",20)
        self.balls=[]
        self.image=pygame.image.load("Sonne.png")
        self.image2=pygame.image.load("Wolke.png")
        self.color = "lightblue"
        self.WIDTH,self.HEIGHT=1000,700
        self.canvas=pygame.display.set_mode((self.WIDTH,self.HEIGHT),pygame.RESIZABLE)
        self.falling=False
        self.t0=0
        self.d=0
        self.schnitt=0
        self.dd=0
        self.zschnitt=0
        self.ic=0
        self.cdball=0
        self.cddel=0
        self.cdtext=0
    
    def run(self, event):

        self.WIDTH, self.HEIGHT = self.canvas.get_size()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True

        pygame.display.set_caption("PyPhySim - Gravitation                       Anzahl Bälle: "
                               +str(len(self.balls))+
                               "   Durchschnittliche Fallhöhe: "
                               +f"{self.schnitt:.2f}cm"
                               +"    Durchschnittliche Fallzeit: "
                               +f"{self.zschnitt:.3f}s")
        if len(self.balls)>0:
            self.schnitt=self.d/len(self.balls)
            self.zschnitt=self.dd/len(self.balls)
        else:
            self.schnitt=0
            self.zschnitt=0
        
        self.canvas.fill(self.color)
        tick=pygame.time.get_ticks()
        pygame.draw.line(self.canvas,"black",(10,0),(10,self.HEIGHT),5)
        pygame.draw.polygon(self.canvas,"chartreuse4",[(0,self.HEIGHT),(100,self.HEIGHT-100),(self.WIDTH,self.HEIGHT-100),(self.WIDTH,self.HEIGHT)])
        self.canvas.blit(self.image,dest=(self.WIDTH-300,50))
        self.w=self.WIDTH*np.sin(tick/10000)
        self.canvas.blit(self.image2,dest=(self.w,20))
        if self.w>self.WIDTH-450:
            self.color="lightblue3"
        if self.w>self.WIDTH-200:
            self.color="lightblue"
        else:
            self.color="lightblue"
        for a in range(int((self.HEIGHT+99)/100)):
            if a==0:
                text_surface=self.font1.render(str(a)+" Meter",True,("black"))
                text_rect=text_surface.get_rect(center=(40,self.HEIGHT-10))
                self.canvas.blit(text_surface,text_rect)
            else:
                text_surface=self.font1.render(str(a)+" Meter",True,("black"))
                text_rect=text_surface.get_rect(center=(40,self.HEIGHT-a*100))
                self.canvas.blit(text_surface,text_rect)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if self.cdball == 0:
                    self.cdball = 20
                    cor=pygame.mouse.get_pos()
                    self.balls.append({"y0":cor[1]-self.radius,"t0":tick,"x0":cor[0],"t_land":None})
                    self.d+=self.HEIGHT-cor[1]
            if event.button==3:
                if self.cdtext == 0:
                    self.cdtext = 15
                    self.cor2=pygame.mouse.get_pos()
                    self.ic+=1


        if self.ic%2 !=0 :
            text_surface=self.font2.render("Delete drücken um Bälle zu löschen",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2))
            self.canvas.blit(text_surface,text_rect)
            text_surface=self.font2.render("Zurück drücken um letzten Ball zu löschen",True,("black"))
            text_rect=text_surface.get_rect(center=(self.cor2[0],self.cor2[1]+30))
            self.canvas.blit(text_surface,text_rect)

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
                    self.d=0
                    self.dd=0

        if self.cddel > 0:
            self.cddel -= 1

        for ball in self.balls:
            t=(tick-ball["t0"])/1000
            y=ball["y0"]+0.5*981*t**2
            x=ball["x0"]
            if y>self.HEIGHT-self.radius:
                y=self.HEIGHT-self.radius
                if ball["t_land"] is None:
                    ball["t_land"]=tick
                    self.dd+=(tick-ball["t0"])/1000             
            pygame.draw.circle(self.canvas,"blue",(int(x),int(y)),self.radius)
            text_surface=self.font.render("Fallhöhe = "+str((self.HEIGHT-ball["y0"]-self.radius))+"cm",True,("red"))
            text_rect=text_surface.get_rect(center=(int(x),int(y)))
            self.canvas.blit(text_surface,text_rect)

            if ball["t_land"] is not None:
                fall_time=(ball["t_land"]-ball["t0"])/1000
                text_surface=self.font.render("Fallzeit = "+f"{fall_time:.3f}s",True,("red"))
                text_rect=text_surface.get_rect(center=(int(x),int(y)+15))
                self.canvas.blit(text_surface,text_rect)
        
        pygame.display.update()
        return False