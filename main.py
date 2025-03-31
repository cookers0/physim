import pygame
pygame.init()
color = "lightblue"
exit=False
WIDTH,HEIGHT=1000,700
canvas=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
falling=False
t0=0
radius=50
font=pygame.font.Font(None,int(radius/3))
font1=pygame.font.Font(None,20)
balls=[]
image=pygame.image.load("Sonne.png")
image2=pygame.image.load("Wolke.png")
while not exit:
    canvas.fill(color)
    tick=pygame.time.get_ticks()
    pygame.draw.line(canvas,"black",(10,0),(10,HEIGHT),5)
    pygame.draw.polygon(canvas,"green",[(0,HEIGHT),(100,HEIGHT-100),(WIDTH,HEIGHT-100),(WIDTH,HEIGHT)])
    canvas.blit(image,dest=(WIDTH-300,50))
    canvas.blit(image2,dest=(WIDTH/4,20))
    for a in range(int(HEIGHT/100)):
        if a==0:
            text_surface=font1.render(str(a)+" Meter",True,("black"))
            text_rect=text_surface.get_rect(center=(40,HEIGHT-10))
            canvas.blit(text_surface,text_rect)
        else:
            text_surface=font1.render(str(a)+" Meter",True,("black"))
            text_rect=text_surface.get_rect(center=(40,HEIGHT-a*100))
            canvas.blit(text_surface,text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit= True
        if event.type==pygame.MOUSEBUTTONDOWN:
            cor=pygame.mouse.get_pos()
            balls.append({"y0":cor[1]-radius,"t0":tick,"x0":cor[0],"t_land":None})
        if event.type==pygame.VIDEORESIZE:
            WIDTH,HEIGHT=event.w,event.h
            canvas=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
            balls=[]
    for ball in balls:
        t=(tick-ball["t0"])/1000
        y=ball["y0"]+0.5*981*t**2
        x=ball["x0"]
        if y>HEIGHT-radius:
            y=HEIGHT-radius
            if ball["t_land"] is None:
                ball["t_land"]=tick

        pygame.draw.circle(canvas,"blue",(int(x),int(y)),radius)
        text_surface=font.render("Fallhöhe = "+str((HEIGHT-ball["y0"]-radius))+"cm",True,("red"))
        text_rect=text_surface.get_rect(center=(int(x),int(y)))
        canvas.blit(text_surface,text_rect)

        if ball["t_land"] is not None:
            fall_time=(ball["t_land"]-ball["t0"])/1000
            text_surface=font.render("Fallzeit = "+f"{fall_time:.2f}s",True,("red"))
            text_rect=text_surface.get_rect(center=(int(x),int(y)+15))
            canvas.blit(text_surface,text_rect)

            
    pygame.display.update()
    

