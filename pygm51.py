from PodSixNet.Connection import ConnectionListener, connection
from time import sleep,time
from math import *
import sys,pygame
from pygame.locals import *
import cv2
import numpy as np
import random
from thread import start_new_thread
traverse=0
prevvel=[50,50]
prevangl=[40,150]
help(ConnectionListener)
list12=['pygme.png','pygme1.png','pygme3.png','pygme4.png','pygme5.png']
a=random.randint(0,5)-1
img14=np.zeros([500,600,3],np.uint8)
cv2.imwrite('img123b.png',img14)

cv2.imwrite('img123b1.png',img14)
img13=np.ones([500,600,3],np.uint8)*255
img12=cv2.imread('pygme.png')
img14=np.ones([500,600,3],np.uint8)*255
tank=[0,0]
list134=['img123a.png','img123a1.png']
list456=['img123b.png','img123b1.png']
list789=['ty.png','ty1.png']
list1011=['ce.png','ce1.png']
#help(pygame.locals) it has all keys and event nme defined(no functions only data)
#help(pygame.event)
pygame.init()
clock=pygame.time.Clock()  #Clock is class and clock an instance of it
soundBllt=pygame.mixer.Sound('bullet_whizzing_by-Mike_Koenig-2005433595.wav')
soundBmb=pygame.mixer.Sound('Bomb-SoundBible.com-891110113.wav')
x=width,height=600,500
screen=pygame.display.set_mode(x)
test3=pygame.image.load('test3.png')
test3=pygame.transform.scale(test3,x)
tux=pygame.image.load('pygme.png')
tux=pygame.transform.scale(tux,x)
tank[0]=pygame.image.load('tnk1.png')
tank[0]=pygame.transform.scale(tank[0],(20,20))
tank[1]=pygame.image.load('tnk2.png')
tank[1]=pygame.transform.scale(tank[1],(20,20))
shwWpn=pygame.image.load('pygme2.png')
shwWpn=pygame.transform.scale(shwWpn,(30,30))
shwWpn2=pygame.image.load('pygme3.png')
shwWpn2=pygame.transform.scale(shwWpn2,(30,30))
shwWpn3=pygame.image.load('pygme4.png')
shwWpn3=pygame.transform.scale(shwWpn3,(30,30))
shwWpn4=pygame.image.load('pygme6.png')
shwWpn4=pygame.transform.scale(shwWpn4,(30,30))
shwWpn5=pygame.image.load('pygme7.png')
shwWpn5=pygame.transform.scale(shwWpn5,(30,30))
cursor=pygame.image.load('pygme5.png')
cursor=pygame.transform.scale(cursor,(30,30))
bullt=pygame.transform.scale(test3,(4,4))
bullt1=pygame.transform.scale(test3,(8,8))
bullt2=pygame.image.load('pygme8.png')
bullt2=pygame.transform.scale(bullt2,(4,4))
dstrX=[0,0,0,0,0,0,0,0,0]
dstrY=[0,0,0,0,0,0,0,0,0]
dstrSize=[0,0,0,0,0,0,0,0,0]
cnter=0

projYL=[3,3]
projYH=[3,3]
fl2=[0,0]
fl1=[0,0]
wpn=[-1,-1]
screen.blit(tux,(0,0))  #top left corner of corner
mx=0
my=0
p=1.2
wpnX=[0,0]
wpnY=[0,0]
projY=[3,3]
projX=[4,4]
projYT=[3,3]
projXT=[4,4]
projYT1=[3,3]
projXT1=[4,4]
messgX=[0,0]
messgY=[0,0]
messgXa=[0,0]
messgYa=[0,0]
messgXb=[0,0]
messgYb=[0,0]
messgXc=[0,0]
messgYc=[0,0]
sign=[1,1]
x=4
u=77.6
p=1.2
y=3
black=(0,255,0)  #rgb
red=[255,0,0]
screen.blit(tux,(0,0))
pygame.display.flip()  #reresh the screen
i=0

x1=3

img12=cv2.resize(img12,(600,500),0,0,cv2.INTER_CUBIC)
grey=[255,255,0]
orange=[0,255,255]
font=pygame.font.SysFont(None,25)  #sysfont is a class with constructor font is instance
vel=[50,50]
angl=[40,150]
scoreVal=[0,0]
posY=[0,0]
mov=[0,0]
cnt=[0,0]
increase=[0,0]
posX=[0,450]
mx1=[400,400]
my1=[0,0]
plyr=0
wpn1=[-1,-1]
def cordy(t,img,l=0):
    while l<500:
        if ((img[l+1,t]>img[l,t])[0])or ((img[l+1,t]>img[l,t])[1]) or ((img[l+1,t]>img[l,t])[2]) :
            return l
        l+=1
posY[0]=cordy(posX[0],img12)
print posY[0]
class BoxesGame(ConnectionListener):
    
    def Network_player(self,data):
        global plyr,img12,list12,tux
        plyr=data["plyrno"]
        print list12[plyr]
        img12=cv2.imread(list12[plyr])
        img12=cv2.resize(img12,(600,500),0,0,cv2.INTER_CUBIC)
        tux=pygame.image.load(list12[plyr])
        tux=pygame.transform.scale(tux,(600,500))

    def Network_mov1rv(self,data):
        global mov
        mov[0]=data["mov0r"]

    def Network_mov0rv(self,data):
        global mov
        mov[1]=data["mov1r"]

    def Network_plyr1wpnrv(self,data):
        global wpn1
        wpn1[0]=data["wpn0rv"]

    def Network_plyr0wpnrv(self,data):
        global wpn1
        wpn1[1]=data["wpn1rv"]

    def Network_plyr1anglrv(self,data):
        global angl
        angl[0]=data["angl0rv"]

    def Network_plyr0anglrv(self,data):
        global angl
        angl[1]=data["angl1rv"]

    def Network_plyr1velrv(self,data):
        global vel
        vel[0]=data["vel0rv"]

    def Network_plyr0velrv(self,data):
        global vel
        vel[1]=data["vel1rv"]    
        

def downhill(x,a,b):
    global img12
    global tux
    global screen
    global cntw
    global cntw1
    global plyr
    t=[-1,-1]*590
    bt=[-1,-1]*620
    ak=[2,2]*590
    gh=[-1,-1]*590
    strtw=[-1,-1]*590
    ias=[0,0]*590
    cntw=0
    cntw1=[0,0]*590
    for trv in range(a,b):
        
        for y in range(cordy(trv,img12)+1,350):
            
            if img12[y,trv,0]==0 and img12[y,trv,1]==0 and img12[y,trv,2]==0 :
                bt[trv-a]=np.copy(img12[(cordy(trv,img12)+1):y,trv:trv+1])
                print trv-a
                t[trv-a]=y
                gh[trv-a]=y-cordy(trv,img12)-1
                strtw[trv-a]=cordy(trv,img12,l=y)
                break
    dwnH2=pygame.image.load(list456[plyr])
    while True:
        for trv in range(a,b):
            if t[trv-a]!=-1:
                cv2.imwrite(list134[plyr],bt[trv-a])
                
                dwnH=pygame.image.load(list134[plyr])
                dwnH2=pygame.transform.scale(dwnH2,(1,3))
                screen.blit(dwnH2,(trv,cordy(trv,img12)+1))
                acv=cordy(trv,img12)
            
                if (acv+gh[trv-a]-2)<strtw[trv-a]:
                    img12[acv+1][trv][0]=0
                    img12[acv+1][trv][1]=0
                    img12[acv+1][trv][2]=0
                    img12[acv+2][trv][0]=0
                    img12[acv+2][trv][1]=0
                    img12[acv+2][trv][2]=0
                    img12[acv+3][trv][0]=0
                    img12[acv+3][trv][1]=0
                    img12[acv+3][trv][2]=0
                
                    
                    
                    img12[(acv+4):(acv+4+gh[trv-a]),trv:trv+1]=(bt[trv-a])
                    
                    
                    screen.blit(dwnH,(trv,cordy(trv,img12)+1))
                else:
                    img12[(strtw[trv-a]-gh[trv-a]+2):(strtw[trv-a]+2),trv:trv+1]=(bt[trv-a])
                    print 'x'
                    t[trv-a]=-1
                    
            
            else:
                if cntw1[trv-a]==0:
                    cntw+=1
                    cntw1[trv-a]=1
            
        cv2.imwrite(list789[plyr],img12)
        tux=pygame.image.load(list789[plyr])    
        pygame.display.flip()        
        if cntw is (b-a):
             
             cv2.imwrite(list789[plyr],img12)
             tux=pygame.image.load(list789[plyr])
             screen.blit(tux,(0,0))
             pygame.display.flip()
             
             break
            
    

       

    

def mssgToScreen(msg,color,x,y):
    scrnText=font.render(msg,True,color)
    screen.blit(scrnText,(x,y))

def score(value,X,Y,t1):
    while Y>30:
                                                     #screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                     #screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                     #screen.blit(tank[1],(450,posY[1]))
                                                     
                                                     mssgToScreen(str(value),[255,255,255],X,Y-2)
                                                     Y-=1
                                                     if sign[0]==1:
                                                         X+=1
                                                     else:
                                                         X-=1
                                                     if X==posX[(t1+1)%2]+20:
                                                         sign[0]=-1
                                                     elif X==posX[(t1+1)%2]-20:
                                                         sign[0]=1
                                                     pygame.display.flip()
                                                     clock.tick(100)
                                                    
running=False
print 'address of server'

host, port="localhost", 80
ConnectionListener().Connect((host,int(port)))
print "Boxes client started"
ConnectionListener().Pump()
connection.Pump()
sleep(0.01)


#determine attributes from player #

'''
if self.num==0:
    self.turn=True
    self.marker = self.greenplayer
    self.othermarker = self.blueplayer
else:
    self.turn=False
    self.marker=self.blueplayer
    self.othermarker = self.greenplayer
'''
b134=BoxesGame()
while True:
      #x toward right y toward bottom
    if plyr==0:
        if mov[0]==1:
            ConnectionListener().Send({"action": "plyr0mv","mov0s": mov[0]})

    elif plyr==1:
        if mov[1]==1:
            ConnectionListener().Send({"action": "plyr1mv","mov1s": mov[1]})    
        
    connection.Pump()
    b134.Pump()
    screen.blit(tux,(0,0))
                        
    if mov[0]==1:
        while cnt[0]<50:
            screen.blit(tux,(0,0))
            screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
            screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))     
            posX[0]+=1
            cnt[0]+=1
            posY[0]=cordy(posX[0],img12)-17
            pygame.display.flip()
            clock.tick(50)
        mov[0]=0
        cnt[0]=0

    if mov[1]==1:
        while cnt[1]<50:
            screen.blit(tux,(0,0))
            screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
            screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
            posX[1]-=1
            cnt[1]+=1
            posY[1]=cordy(posX[1],img12)-17
            pygame.display.flip()
            clock.tick(50)
        mov[1]=0
        cnt[1]=0    
    posY[0]=cordy(posX[0],img12)-17
    screen.blit(tank[0],(posX[0],posY[0]))
    posY[1]=cordy(posX[1],img12)-17
    screen.blit(tank[1],(posX[1],posY[1]))
    if plyr==0:
        screen.blit(cursor,(int(posX[0]+100*cos(angl[0]*3.142/180)-15),int(posY[0]-100*sin(angl[0]*3.142/180)-15)))

    else:
        screen.blit(cursor,(int(posX[1]+100*cos(angl[1]*3.142/180)-15),int(posY[1]-100*sin(angl[1]*3.142/180)-15)))
        
    screen.fill(grey,rect=(0,375,600,125))
    screen.fill(red,rect=(30,420,60,60))
    screen.fill(red,rect=(150,420,120,60))
    screen.fill(red,rect=(320,420,150,60))
    screen.fill(red,rect=(500,420,60,60))
    screen.fill(red,rect=(230,380,130,30))
    screen.fill([0,0,0],rect=(155,445,80,35))
    screen.fill([0,50,0],rect=(325,445,140,30))
    af=[0,0]
    bf=[0,0]
    cf=[0,0]
    t=[0,0]
    cntbt=[0,0]
    cntbt1=[0,0]
    msfg=[0,0]
    brk=[0,0]
    wpn3cnt=[0,0]
    b=[0,0]
    c=[0,0]
    d=[0,0]
    i1=0
    i2=0
    fla=[0,0]
    #screen.fill(red,rect=(0,400,600,100))
    mssgToScreen('WEAPONS',orange,250,385)
    mssgToScreen('PLAYER 1',[200,20,100],20,20)
    mssgToScreen('PLAYER 2',[200,20,100],500,20)
    mssgToScreen('FIRE',orange,40,440)
    mssgToScreen('ANGLE',orange,160,425)
    mssgToScreen('POWER',orange,330,425)
    mssgToScreen('MOVE',orange,505,440)
    screen.fill([100,100,100],rect=(244,426,21,24))
    screen.fill([100,100,100],rect=(244,452,21,23))
    pygame.draw.polygon(screen,(230,120,200),[(253,428),(244,447),(262,447)])
    pygame.draw.polygon(screen,(230,120,200),[(253,473),(244,454),(262,454)])
    if plyr==1:
        
        if wpn1[0]!=-1:
            while True:

#start
                            
                            screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                            screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                            screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                            
                            if wpn1[0]==2:
                                     if projX[0]+posX[0]>599:
                                              projX[0]=4
                                              projY[0]=3
                                              projYH[0]=3
                                              projYL[0]=3
                                              
                                              break

                                              
                                     
                                     if af[0]!=1:
                                         if (posY[0]-2-projY[0])<cordy(projX[0]+posX[0],img12):
                                            projY[0]=int(projX[0]*tan(angl[0]*3.142/180)-5*projX[0]*projX[0]/(vel[0]*vel[0]*(cos(angl[0]*3.142/180)**2)))
                                            screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projY[0]+2)))
                                            
                                         else:
                                             
                                             soundBmb.play()
                                             af[0]=1
                                             cnter+=1
                                             dstrX[cnter]=projX[0]+posX[0]
                                             dstrY[cnter]=posY[0]-projY[0]+2
                                             dstrSize[cnter]=25
                                             pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                             img13=np.copy(img14)
                                             img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                             img12=cv2.bitwise_and(img12,img13,mask=None)
                                             astart=dstrX[cnter]-dstrSize[cnter]
                                             cv2.imwrite(list1011[plyr],img12)
                                             tux=pygame.image.load(list1011[plyr])
                                             if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                 increase[0]=25
                                                 if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                     increase[0]=50
                                                     if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                           increase[0]=100
                                                 scoreVal[0]+=increase[0]
                                                 messgXa[0]=posX[1]
                                                 messgYa[0]=posY[1]
                                                 ia=increase[0]
                                           
                                             
                                                 
                                     if bf[0]!=1:        
                                         if (posY[0]-2-projYL[0])<cordy(projX[0]+posX[0],img12):
                                             vel1=(vel[0]*vel[0]*sin(2*(angl[0])*3.142/180)-300)/sin(2*(angl[0]-5)*3.142/180)
                                             vel1=vel1**(1/2.0)
                                             projYL[0]=int(projX[0]*tan((angl[0]-5)*3.142/180)-5*projX[0]*projX[0]/(vel1*vel1*(cos((angl[0]-5)*3.142/180)**2)))
                                             screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projYL[0]+2)))
                                
                                         else:
                                             soundBmb.play()
                                             bf[0]=1
                                             cnter+=1
                                             dstrX[cnter]=projX[0]+posX[0]
                                             dstrY[cnter]=posY[0]-projYL[0]+2
                                             dstrSize[cnter]=25
                                             pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                             img13=np.copy(img14)
                                             img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                             img12=cv2.bitwise_and(img12,img13,mask=None)
                                             cv2.imwrite(list1011[plyr],img12)
                                             tux=pygame.image.load(list1011[plyr])

                                             if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projYL[0]-2)-posY[1])<50:
                                                 increase[0]=25
                                                 if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projYL[0]-2)-posY[1])<25:
                                                     increase[0]=50
                                                     if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projYL[0]-2)-posY[1])<10:
                                                           increase[0]=100
                                                 scoreVal[0]+=increase[0]
                                                 messgXb[0]=posX[1]
                                                 messgYb[0]=posY[1]
                                                 ib=increase[0]
                                        
                                     if cf[0]!=1:        
                                         if (posY[0]-2-projYH[0])<cordy(projX[0]+posX[0],img12):
                                             vel2=(vel[0]*vel[0]*sin(2*(angl[0])*3.142/180)+300)/sin(2*(angl[0]+5)*3.142/180)
                                             vel2=vel2**(1/2.0)
                                             projYH[0]=int(projX[0]*tan((angl[0]+5)*3.142/180)-5*projX[0]*projX[0]/(vel2*vel2*(cos((angl[0]+5)*3.142/180)**2)))
                                             screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projYH[0]+2)))
                                             
                                         else:
                                             soundBmb.play()
                                             cf[0]=1
                                             cnter+=1
                                             dstrX[cnter]=projX[0]+posX[0]
                                             dstrY[cnter]=posY[0]-projYH[0]+2
                                             dstrSize[cnter]=25
                                             pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                             img13=np.copy(img14)

                                             img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                             img12=cv2.bitwise_and(img12,img13,mask=None)

                                             cv2.imwrite(list1011[plyr],img12)
                                             tux=pygame.image.load(list1011[plyr])
                                             bend=dstrX[cnter]+dstrSize[cnter]

                                             if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projYH[0]-2)-posY[1])<50:
                                                 increase[0]=25
                                                 if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projYH[0]-2)-posY[1])<25:
                                                     increase[0]=50
                                                     if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projYH[0]-2)-posY[1])<10:
                                                           increase[0]=100
                                                 scoreVal[0]+=increase[0]
                                                 messgXc[0]=posX[1]
                                                 messgYc[0]=posY[1]
                                                 ic=increase[0]
                                     if af[0]==1 or bf[0]==1 or cf[0]==1:
                                         if b[0]!=1:
                                             if af[0]==1:
                                                 if messgYa[0]>30:
                                                         mssgToScreen(str(ia),[255,255,255],messgXa[0],messgYa[0]-2)
                                                         messgYa[0]-=1
                                                         if sign[0]==1:
                                                             messgXa[0]+=1
                                                         else:
                                                             messgXa[0]-=1
                                                         if messgXa[0]==posX[1]+20:
                                                             sign[0]=-1
                                                         elif messgXa[0]==posX[1]-20:
                                                             sign[0]=1
                                                         
                                                 else:
                                                     wpn3cnt[0]+=1
                                                     b[0]=1
                                         if c[0]!=1:
                                             if bf[0]==1:
                                                 if messgYb[0]>30:
                                                         
                                                         mssgToScreen(str(ib),[255,255,255],messgXb[0],messgYb[0]-2)
                                                         messgYb[0]-=1
                                                         if sign[0]==1:
                                                             messgXb[0]+=1
                                                         else:
                                                             messgXb[0]-=1
                                                         if messgXb[0]==posX[1]+20:
                                                             sign[0]=-1
                                                         elif messgXb[0]==posX[1]-20:
                                                             sign[0]=1
                                                         
                                                 else:
                                                     wpn3cnt[0]+=1
                                                     c[0]=1
                                         if d[0]!=1:
                                             if cf[0]==1:
                                                 if messgYc[0]>30:
                                                         
                                                         mssgToScreen(str(ic),[255,255,255],messgXc[0],messgYc[0]-2)
                                                         messgYc[0]-=1
                                                         if sign[0]==1:
                                                             messgXc[0]+=1
                                                         else:
                                                             messgXc[0]-=1
                                                         if messgXc[0]==posX[1]+20:
                                                             sign[0]=-1
                                                         elif messgXc[0]==posX[1]-20:
                                                             sign[0]=1
                                                         
                                                 else:
                                                     wpn3cnt[0]+=1
                                                     d[0]=1
                                     if wpn3cnt[0]==3:
                                         abcd=downhill(traverse,astart,bend)
                                         projX[0]=4
                                         projY[0]=3
                                         projYH[0]=3
                                         projYL[0]=3
                                         break
                                     projX[0]+=1
                                     pygame.display.flip()



                            elif wpn1[0]==4:
                                     soundBllt.play()
                                     while True:
                                         laserX=int(posX[0]+i1*cos(angl[0]*3.142/180)-2)
                                         laserY=int(posY[0]-i1*sin(angl[0]*3.142/180)-2)
                                         screen.blit(bullt2,(laserX,laserY+4))
                                         i1+=1
                                         
                                         if abs(laserX-posX[1])<20 and abs(laserY-posY[1]+4)<20 :
                                                 soundBmb.play()
                                                 scoreVal[0]+=75
                                                 messgX[0]=posX[1]
                                                 messgY[0]=posY[1]
                                             
                                                 while messgY[0]>30:
                                                     screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                     screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                     screen.blit(tank[1],(450,posY[1]))
                                                     mssgToScreen(str(25),[255,255,255],messgX[0],messgY[0]-2)
                                                     mssgToScreen(str(25),[255,255,255],messgX[0]+10,messgY[0]-15)
                                                     mssgToScreen(str(25),[255,255,255],messgX[0],messgY[0]-29)
                                                     
                                                     messgY[0]-=1
                                                     if sign[0]==1:
                                                         messgX[0]+=1
                                                     else:
                                                         messgX[0]-=1
                                                     if messgX[0]==posX[1]+20:
                                                         sign[0]=-1
                                                     elif messgX[0]==posX[1]-20:
                                                         sign[0]=1
                                                     pygame.display.flip()    
                                                     clock.tick(100)
                                                 break
                                         pygame.display.flip()
                                         clock.tick(100)
                                     
                                     break
                                    
                            elif wpn1[0]==0 or wpn1[0]==1 or wpn1[0]==3:
                                    if (posY[0]-2-projY[0])<cordy(projX[0]+posX[0],img12):
                                         if projX[0]+posX[0]>599:
                                              projX[0]=4
                                              projY[0]=3
                                        
                                              break

                                             
                                         projY[0]=int(projX[0]*tan(angl[0]*3.142/180)-5*projX[0]*projX[0]/(vel[0]*vel[0]*(cos(angl[0]*3.142/180)**2)))
                                         if wpn1[0]==0:
                                             screen.blit(bullt1,(projX[0]+posX[0],(posY[0]-projY[0]+2)))

                                         elif wpn1[0]==1 or wpn1[0]==3:
                                             screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projY[0]+2)))
                                         projX[0]+=1
                                         
                                    else:
                                        soundBmb.play()
                                        if wpn1[0]==0:
                                            cnter+=1
                                            dstrX[cnter]=projX[0]+posX[0]
                                            dstrY[cnter]=posY[0]-projY[0]+2
                                            dstrSize[cnter]=75
                                            pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                            img13=np.copy(img14)
                                            img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                            img12=cv2.bitwise_and(img12,img13,mask=None)
                                            traverse=dstrX[cnter]-dstrSize[cnter]
                                              
                                            abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])              
                                            
                                        elif wpn1[0]==1:
                                            cnter+=1
                                            dstrX[cnter]=projX[0]+posX[0]
                                            dstrY[cnter]=posY[0]-projY[0]+2
                                            dstrSize[cnter]=50
                                            pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                            img13=np.copy(img14)
                                            img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                            img12=cv2.bitwise_and(img12,img13,mask=None)
                                            traverse=dstrX[cnter]-dstrSize[cnter]
                                              
                                            abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                        elif wpn1[0]==3:
                                            cnter+=1
                                            dstrX[cnter]=projX[0]+posX[0]
                                            dstrY[cnter]=posY[0]-projY[0]+2
                                            dstrSize[cnter]=50
                                            pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                            img13=np.copy(img14)
                                            img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                            img12=cv2.bitwise_and(img12,img13,mask=None)    
                                            traverse=dstrX[cnter]-dstrSize[cnter]
                                              
                                            abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])
                                                                            
                                            
                                            
                                        if wpn1[0]==0:
                                            if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                 increase[0]=25
                                                 if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                     increase[0]=50
                                                     if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                           increase[0]=100
                                                 scoreVal[0]+=increase[0]
                                                 messgX[0]=posX[1]
                                                 messgY[0]=posY[1]
                                             
                                                 while messgY[0]>30:
                                                     screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                     screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                     screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                     mssgToScreen(str(increase[0]),[255,255,255],messgX[0],messgY[0]-2)
                                                     messgY[0]-=1
                                                     if sign[0]==1:
                                                         messgX[0]+=1
                                                     else:
                                                         messgX[0]-=1
                                                     if messgX[0]==posX[1]+20:
                                                         sign[0]=-1
                                                     elif messgX[0]==posX[1]-20:
                                                         sign[0]=1
                                                     pygame.display.flip()    
                                                     clock.tick(100)

                                        elif wpn1[0]==1:
                                            if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                 increase[0]=10
                                                 if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                     increase[0]=20
                                                     if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                           increase[0]=50
                                                 scoreVal[0]+=increase[0]
                                                 messgX[0]=posX[1]
                                                 messgY[0]=posY[1]
                                             
                                                 while messgY[0]>30:
                                                     screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                     screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                     screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                     mssgToScreen(str(increase[0]),[255,255,255],messgX[0],messgY[0]-2)
                                                     messgY[0]-=1
                                                     if sign[0]==1:
                                                         messgX[0]+=1
                                                     else:
                                                         messgX[0]-=1
                                                     if messgX[0]==posX[1]+20:
                                                         sign[0]=-1
                                                     elif messgX[0]==posX[1]-20:
                                                         sign[0]=1
                                                     pygame.display.flip()    
                                                     clock.tick(100)

                                            
                                        elif wpn1[0]==3:
                                            if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                 increase[0]=25
                                                 if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                     increase[0]=50
                                                     if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                           increase[0]=100
                                                 scoreVal[0]+=increase[0]
                                                 messgX[0]=posX[1]
                                                 messgY[0]=posY[1]
                                             
                                                 
                                                 while True:
                                                     screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                    
                                                     if messgY[0]>30:
                                                         mssgToScreen(str(increase[0]),[255,255,255],messgX[0],messgY[0]-2)
                                                         messgY[0]-=1
                                                         if sign[0]==1:
                                                             messgX[0]+=1
                                                         else:
                                                             messgX[0]-=1
                                                         if messgX[0]==posX[1]+20:
                                                             sign[0]=-1
                                                         elif messgX[0]==posX[1]-20:
                                                             sign[0]=1
                                                     else:
                                                         msfg[0]=1
                                                     if fl2[0]!=1:
                                                         if (posY[1]-projYT[0])<cordy(projXT[0]+posX[1],img12):
                                                             if projXT[0]+posX[1]>580:
                                                                  posX[1]=580
                                                                  projXT[0]=4
                                                                  projYT[0]=3
                                                                  fl2[0]=1
                                                                  cntbt[0]=1

                                                             
                                                             projYT[0]=int(projXT[0]*tan(60*3.142/180)-5*projXT[0]*projXT[0]/(30*30*(cos(60*3.142/180)**2)))
                                                             screen.blit(tank[1],(projXT[0]+posX[1],(posY[1]-projYT[0]-17)))
                                                             projXT[0]+=1

                                                         else:
                                                             posX[1]=projXT[0]+posX[1]
                                                             projXT[0]=4
                                                             projYT[0]=3
                                                             fl2[0]=1
                                                             cntbt[0]=1
                                                     else:
                                                         screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                         
                                                     if fl1[0]!=1:
                                                         if (posY[0]-projYT[1])<cordy(posX[0]-projXT[1],img12):
                                                             if posX[0]-projXT[1]<20:
                                                                  posX[0]=10
                                                                  projXT[1]=4
                                                                  projYT[1]=3
                                                                  fl1[0]=1
                                                                  cntbt1[0]=1

                                                             
                                                             projYT[1]=int(projXT[1]*tan(60*3.142/180)-5*projXT[1]*projXT[1]/(30*30*(cos(60*3.142/180)**2)))
                                                             screen.blit(tank[0],(posX[0]-projXT[1],(posY[0]-projYT[1]-17)))
                                                             projXT[1]+=1

                                                         else:
                                                             posX[0]=posX[0]-projXT[1]
                                                             projXT[1]=4
                                                             projYT[1]=3
                                                             fl1[0]=1
                                                             cntbt1[0]=1
                                                     else:
                                                         screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                     if msfg[0]==1 and cntbt1[0]==1 and cntbt[0]==1:
                                                         break
                                                     pygame.display.flip()   
                                                       
                                                 
                                        projX[0]=4
                                        projY[0]=3
                                        
                                        break
                            pygame.display.flip()
            wpn1[0]=-1                
#end                            
            
    else:
        
        if wpn1[1]!=-1:
            print wpn1[1]
            while True:
                                screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                               

                                
                                screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                            

                
                                if wpn1[1]==2:
                                         if posX[1]-projX[1]>599:
                                                  projX[1]=4
                                                  projY[1]=3
                                                  projYH[1]=3
                                                  projYL[1]=3
                                                  
                                                  break

                                                  
                                         
                                         if af[1]!=1:
                                             if (posY[1]-2-projY[1])<cordy(posX[1]-projX[1],img12):
                                                projY[1]=int(projX[1]*tan((180-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel[1]*vel[1]*(cos((180-angl[1])*3.142/180)**2)))
                                                screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projY[1]+2)))
                                                
                                             else:
                                                 soundBmb.play()
                                                 af[1]=1
                                                 cnter+=1
                                                 dstrX[cnter]=posX[1]-projX[1]
                                                 dstrY[cnter]=posY[1]-projY[1]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 astart=dstrX[cnter]-dstrSize[cnter]
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])
                    
                                                 if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         
                                                         scoreVal[1]+=increase[1]
                                                         messgXa[1]=posX[0]
                                                         messgYa[1]=posY[0]
                                                         ia1=increase[1]
                                         if bf[1]!=1:        
                                             if (posY[1]-2-projYL[1])<cordy(posX[1]-projX[1],img12):
                                                 vel11=(vel[1]*vel[1]*sin(2*(180-angl[1])*3.142/180)+300)/sin(2*(185-angl[1])*3.142/180)
                                                 vel11=vel11**(1/2.0)
                                                 projYL[1]=int(projX[1]*tan((185-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel11*vel11*(cos((185-angl[1])*3.142/180)**2)))
                                                 screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projYL[1]+2)))
                                                
                                             else:
                                                 soundBmb.play()
                                                 
                                                 bf[1]=1
                                                 cnter+=1
                                                 dstrX[cnter]=posX[1]-projX[1]
                                                 dstrY[cnter]=posY[1]-projYL[1]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])

                                                 if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projYL[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         scoreVal[1]+=increase[1]
                                                 
                                                     
                                                         messgXb[1]=posX[0]
                                                         messgYb[1]=posY[0]
                                                         ib1=increase[1]
                                         if cf[1]!=1:        
                                             if (posY[1]-2-projYH[1])<cordy(posX[1]-projX[1],img12):
                                                 vel21=(vel[1]*vel[1]*sin(2*(180-angl[1])*3.142/180)-300)/sin(2*(175-angl[1])*3.142/180)
                                                 vel21=vel21**(1/2.0)
                                                 projYH[1]=int(projX[1]*tan((175-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel21*vel21*(cos((175-angl[1])*3.142/180)**2)))
                                                 screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projYH[1]+2)))
                                                 
                                             else:
                                                 soundBmb.play()
                                                 
                                                 cf[1]=1
                                                 cnter+=1
                                                 dstrX[cnter]=posX[1]-projX[1]
                                                 dstrY[cnter]=posY[1]-projYH[1]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 bend=dstrX[cnter]+dstrSize[cnter]
                                              
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])
                                                 if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projYH[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projYH[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projYH[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                    
                                                         scoreVal[1]+=increase[1]
                                                         messgXc[1]=posX[0]
                                                         messgYc[1]=posY[0]
                                                         ic1=increase[1]

                                         if af[1]==1 or bf[1]==1 or cf[1]==1:
                                             if b[1]!=1:
                                                 if af[1]==1:
                                                     if messgYa[1]>30:
                                                             mssgToScreen(str(ia1),[255,255,255],messgXa[1],messgYa[1]-2)
                                                             messgYa[1]-=1
                                                             if sign[1]==1:
                                                                 messgXa[1]+=1
                                                             else:
                                                                 messgXa[1]-=1
                                                             if messgXa[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgXa[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             
                                                     else:
                                                         wpn3cnt[1]+=1
                                                         b[1]=1
                                             if c[1]!=1:
                                                 if bf[1]==1:
                                                     if messgYb[1]>30:
                                                             
                                                             mssgToScreen(str(ib1),[255,255,255],messgXb[1],messgYb[1]-2)
                                                             messgYb[1]-=1
                                                             if sign[1]==1:
                                                                 messgXb[1]+=1
                                                             else:
                                                                 messgXb[1]-=1
                                                             if messgXb[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgXb[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             
                                                     else:
                                                         wpn3cnt[1]+=1
                                                         c[1]=1
                                             if d[1]!=1:
                                                 if cf[1]==1:
                                                     if messgYc[1]>30:
                                                             
                                                             mssgToScreen(str(ic1),[255,255,255],messgXc[1],messgYc[1]-2)
                                                             messgYc[1]-=1
                                                             if sign[1]==1:
                                                                 messgXc[1]+=1
                                                             else:
                                                                 messgXc[1]-=1
                                                             if messgXc[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgXc[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             
                                                     else:
                                                         wpn3cnt[1]+=1
                                                         d[1]=1                
                                         if wpn3cnt[1]==3:
                                             abcd=downhill(traverse,astart,bend)
                                             projX[1]=4
                                             projY[1]=3
                                             projYH[1]=3
                                             projYL[1]=3
                                             
                                             break
                                         projX[1]+=1
                                         pygame.display.flip()

                                elif wpn1[1]==4:
                                         soundBllt.play()
                                         while True:
                                             laserX2=int(posX[1]+i2*cos(angl[1]*3.142/180)-2)
                                             laserY2=int(posY[1]-i2*sin(angl[1]*3.142/180)-2)
                                             screen.blit(bullt2,(laserX2,laserY2+4))
                                             i2+=1
                                             
                                             if abs(laserX2-posX[0])<20 and abs(laserY2-posY[0]+4)<20 :
                                                     soundBmb.play()
                                                     scoreVal[1]+=75
                                                     messgX[1]=posX[0]
                                                     messgY[1]=posY[0]
                                                 
                                                     while messgY[1]>30:
                                                         screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                        
                                                         screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                         screen.blit(tank[0],(posX[0],posY[0]))
                                                         mssgToScreen(str(25),[255,255,255],messgX[1],messgY[1]-2)
                                                         mssgToScreen(str(25),[255,255,255],messgX[1]+10,messgY[1]-15)
                                                         mssgToScreen(str(25),[255,255,255],messgX[1],messgY[1]-29)
                                                         
                                                         messgY[1]-=1
                                                         if sign[1]==1:
                                                             messgX[1]+=1
                                                         else:
                                                             messgX[1]-=1
                                                         if messgX[1]==posX[0]+20:
                                                             sign[1]=-1
                                                         elif messgX[1]==posX[0]-20:
                                                             sign[1]=1
                                                         pygame.display.flip()    
                                                         clock.tick(100)
                                                     break
                                             pygame.display.flip()
                                             clock.tick(100)
                                         
                                         break
                                        
                                elif wpn1[1]==0 or wpn1[1]==1 or wpn1[1]==3:     
                                            if (posY[1]-2-projY[1])<cordy(posX[1]-projX[1],img12):
                                                 if posX[1]-projX[1]<0:
                                                      projX[1]=4
                                                      projY[1]=3
                                                      
                                                      break
                                                 print (projX[1],vel[1],angl[1],projY[1])   
                                                 projY[1]=int(projX[1]*tan((180-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel[1]*vel[1]*(cos((180-angl[1])*3.142/180)**2)))
                                                 if wpn1[1]==0:
                                                     screen.blit(bullt1,(posX[1]-projX[1],(posY[1]-projY[1]+2)))

                                                 if wpn1[1]==1 or wpn1[1]==3 :
                                                     screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projY[1]+2)))    
                                                 projX[1]+=1
                                                 
                                            else:
                                                soundBmb.play()
                                                if wpn1[1]==0:
                                                    cnter+=1
                                                    dstrX[cnter]=posX[1]-projX[1]
                                                    dstrY[cnter]=posY[1]-projY[1]+2
                                                    dstrSize[cnter]=75
                                                    pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                    img13=np.copy(img14)
                                                    img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                    img12=cv2.bitwise_and(img12,img13,mask=None)
                                                    traverse=dstrX[cnter]-dstrSize[cnter]
                                                    abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                                elif wpn1[1]==1:
                                                    cnter+=1
                                                    dstrX[cnter]=posX[1]-projX[1]
                                                    dstrY[cnter]=posY[1]-projY[1]+2
                                                    dstrSize[cnter]=50
                                                    pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                    img13=np.copy(img14)
                                                    img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                    img12=cv2.bitwise_and(img12,img13,mask=None)
                                                    traverse=dstrX[cnter]-dstrSize[cnter]
                                                    abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                                elif wpn1[1]==3:
                                                    cnter+=1
                                                    dstrX[cnter]=posX[1]-projX[1]
                                                    dstrY[cnter]=posY[1]-projY[1]+2
                                                    dstrSize[cnter]=50
                                                    pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                    img13=np.copy(img14)
                                                    img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                    img12=cv2.bitwise_and(img12,img13,mask=None)    
                                                    traverse=dstrX[cnter]-dstrSize[cnter]
                                                    abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                                if wpn1[1]==0:
                                                    if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         scoreVal[1]+=increase[1]
                                                         messgX[1]=posX[0]
                                                         messgY[1]=posY[0]
                                                         while messgY[1]>30:
                                                             screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                             screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                             screen.blit(tank[1],(450,posY[1]))
                                                             mssgToScreen(str(increase[1]),[255,255,255],messgX[1],messgY[1]-2)
                                                             messgY[1]-=1
                                                             if sign[1]==1:
                                                                 messgX[1]+=1
                                                             else:
                                                                 messgX[1]-=1
                                                             if messgX[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgX[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             pygame.display.flip()    
                                                             clock.tick(100)


                                                elif wpn1[1]==1:
                                                    if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=10
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=20
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=50
                                                         scoreVal[1]+=increase[1]
                                                         messgX[1]=posX[0]
                                                         messgY[1]=posY[0]
                                                         while messgY[1]>30:
                                                             screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                             
                                                             screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                             screen.blit(tank[1],(450,posY[1]))
                                                             mssgToScreen(str(increase[1]),[255,255,255],messgX[1],messgY[1]-2)
                                                             messgY[1]-=1
                                                             if sign[1]==1:
                                                                 messgX[1]+=1
                                                             else:
                                                                 messgX[1]-=1
                                                             if messgX[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgX[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             pygame.display.flip()    
                                                             clock.tick(100)


                                                elif wpn1[1]==3:
                                                     if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         scoreVal[1]+=increase[1]
                                                         messgX[1]=posX[0]
                                                         messgY[1]=posY[0]
                                                         while True:
                                                             screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                             
                                                             if messgY[1]>30:
                                                                 mssgToScreen(str(increase[1]),[255,255,255],messgX[1],messgY[1]-2)
                                                                 messgY[1]-=1
                                                                 if sign[1]==1:
                                                                     messgX[1]+=1
                                                                 else:
                                                                     messgX[1]-=1
                                                                 if messgX[1]==posX[0]+20:
                                                                     sign[1]=-1
                                                                 elif messgX[1]==posX[0]-20:
                                                                     sign[1]=1

                                                             else:
                                                                 msfg[1]=1

                                                             if fl2[1]!=1:
                                                                 if (posY[1]-projYT1[0])<cordy(projXT1[0]+posX[1],img12):
                                                                     if projXT1[0]+posX[1]>580:
                                                                          posX[1]=580
                                                                          projXT1[0]=4
                                                                          projYT1[0]=3
                                                                    
                                                                          fl2[1]=1
                                                                          cntbt[1]=1

                                                                     
                                                                     projYT1[0]=int(projXT1[0]*tan(60*3.142/180)-5*projXT1[0]*projXT1[0]/(30*30*(cos(60*3.142/180)**2)))
                                                                     screen.blit(tank[1],(projXT1[0]+posX[1],(posY[1]-projYT1[0]-17)))
                                                                     projXT1[0]+=1

                                                                 else:
                                                                     posX[1]=projXT1[0]+posX[1]
                                                                     projXT1[0]=4
                                                                     projYT1[0]=3
                                                            
                                                                     fl2[1]=1
                                                                     cntbt[1]=1
                                                             else:
                                                                 screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                                 
                                                             if fl1[1]!=1:
                                                                 if (posY[0]-projYT1[1])<cordy(posX[0]-projXT1[1],img12):
                                                                     

                                                                     
                                                                     projYT1[1]=int(projXT1[1]*tan(60*3.142/180)-5*projXT1[1]*projXT1[1]/(30*30*(cos(60*3.142/180)**2)))
                                                                     screen.blit(tank[0],(posX[0]-projXT1[1],(posY[0]-projYT1[1]-17)))
                                                                     projXT1[1]+=1
                                                                     if posX[0]-projXT1[1]<40:
                                                                          posX[0]=10
                                                                          projXT1[1]=4
                                                                          projYT1[1]=3
                                                                        
                                                                          fl1[1]=1
                                                                          cntbt1[1]=1

                                                                 else:
                                                                     posX[0]=posX[0]-projXT1[1]
                                                                     projXT1[1]=4
                                                                     projYT1[1]=3
                                                            
                                                                     fl1[1]=1
                                                                     cntbt1[1]=1
                                                             else:
                                                                 screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                             if msfg[1]==1 and cntbt1[1]==1 and cntbt[1]==1:
                                                                 break
                                                             pygame.display.flip()   
                                                 
                                                     
                                                     
                                                           
                                                     
                                                projX[1]=4
                                                projY[1]=3
                                        
                                                break
                                pygame.display.flip()
            wpn1[1]=-1                            
    
    for event in pygame.event.get():  #event is a queue which inserts its event in background
        if event.type==pygame.QUIT:
              sys.exit()
        elif event.type==KEYDOWN and event.key==K_ESCAPE:  #any key down
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            
                event=pygame.event.get()
                mx,my=pygame.mouse.get_pos()
                if mx>326 and mx<470:   #compares first element then 2nd
                    if my>446 and my<472:
                        while True:
                            if plyr==0:
                                for event in pygame.event.get():
                                    if event.type!=MOUSEBUTTONUP:
                                        mx1[0],my1[0]=pygame.mouse.get_pos()
                                        if mx1[0]>326 and mx1[0]<470:   #compares first element then 2nd
                                            if my1[0]>446 and my1[0]<472:
                                                screen.fill([0,50,0],rect=(325,445,140,30))
                                                screen.fill([100,0,0],rect=(327,447,mx1[0]-332,25))
                                                pygame.display.flip()
                                    else :
                                        t[0]=1
                                        break
                                if t[0]==1:
                                    break

                            else:
                                for event in pygame.event.get():
                                    if event.type!=MOUSEBUTTONUP:
                                        mx1[1],my1[1]=pygame.mouse.get_pos()
                                        if mx1[1]>326 and mx1[1]<470:   #compares first element then 2nd
                                            if my1[1]>446 and my1[1]<472:
                                                screen.fill([0,50,0],rect=(325,445,140,30))
                                                screen.fill([100,0,0],rect=(327,447,mx1[1]-332,25))
                                                pygame.display.flip()
                                    else :
                                        t[1]=1
                                        break
                                if t[1]==1:
                                    break   

                                

                elif mx>244 and mx<265:
                     if my>426 and my<450:
                         if plyr==0:
                             angl[0]+=1
                             if angl[0]>359:
                                 angl[0]=angl[0]-360
                         else:
                             angl[1]+=1
                             if angl[1]>359:
                                 angl[1]=angl[1]-360
                             
                     elif my>452 and my<473:
                         if plyr==0:
                             angl[0]-=1
                             if angl[0]<0:
                                 angl[0]=360+angl[0]
                         else:
                            angl[1]-=1
                            if angl[1]<0:
                                 angl[1]=360+angl[1]
                elif mx>500 and mx<560:
                    if my>420 and my<480:
                        if plyr==0:
                            mov[0]=1
                        else:    
                            mov[1]=1
                elif mx>30 and mx<90:
                    if my>420 and my<480:
                            soundBllt.play()
    
                            if plyr==0:
                                        ConnectionListener().Send({"action": "plyr1wpn","wpn0s":wpn[0] })
                                        print time()
                                        
                            if plyr==1:
                                        ConnectionListener().Send({"action": "plyr0wpn","wpn1s":wpn[1] })
                            connection.Pump()
                            b134.Pump()
                            
                            while True:
                                    
        
                                    
                                screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                

                                    
                                screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                
                                if wpn[0]==2:
                                         if projX[0]+posX[0]>599:
                                                  projX[0]=4
                                                  projY[0]=3
                                                  projYH[0]=3
                                                  projYL[0]=3
                                                  
                                                  break

                                                  
                                         
                                         if af[0]!=1:
                                             if (posY[0]-2-projY[0])<cordy(projX[0]+posX[0],img12):
                                                projY[0]=int(projX[0]*tan(angl[0]*3.142/180)-5*projX[0]*projX[0]/(vel[0]*vel[0]*(cos(angl[0]*3.142/180)**2)))
                                                screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projY[0]+2)))
                                                
                                             else:
                                                 soundBmb.play()
                                                 af[0]=1
                                                 cnter+=1
                                                 dstrX[cnter]=projX[0]+posX[0]
                                                 dstrY[cnter]=posY[0]-projY[0]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 astart=dstrX[cnter]-dstrSize[cnter]
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])

                                                 if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                     increase[0]=25
                                                     if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                         increase[0]=50
                                                         if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                               increase[0]=100
                                                     scoreVal[0]+=increase[0]
                                                     messgXa[0]=posX[1]
                                                     messgYa[0]=posY[1]
                                                     ia=increase[0]
                                               
                                                 
                                                     
                                         if bf[0]!=1:        
                                             if (posY[0]-2-projYL[0])<cordy(projX[0]+posX[0],img12):
                                                 vel1=(vel[0]*vel[0]*sin(2*(angl[0])*3.142/180)-300)/sin(2*(angl[0]-5)*3.142/180)
                                                 vel1=vel1**(1/2.0)
                                                 projYL[0]=int(projX[0]*tan((angl[0]-5)*3.142/180)-5*projX[0]*projX[0]/(vel1*vel1*(cos((angl[0]-5)*3.142/180)**2)))
                                                 screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projYL[0]+2)))
                                    
                                             else:
                                                 soundBmb.play()
                                                 bf[0]=1
                                                 cnter+=1
                                                 dstrX[cnter]=projX[0]+posX[0]
                                                 dstrY[cnter]=posY[0]-projYL[0]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])
                                                 if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projYL[0]-2)-posY[1])<50:
                                                     increase[0]=25
                                                     if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projYL[0]-2)-posY[1])<25:
                                                         increase[0]=50
                                                         if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projYL[0]-2)-posY[1])<10:
                                                               increase[0]=100
                                                     scoreVal[0]+=increase[0]
                                                     messgXb[0]=posX[1]
                                                     messgYb[0]=posY[1]
                                                     ib=increase[0]
                                            
                                         if cf[0]!=1:        
                                             if (posY[0]-2-projYH[0])<cordy(projX[0]+posX[0],img12):
                                                 vel2=(vel[0]*vel[0]*sin(2*(angl[0])*3.142/180)+300)/sin(2*(angl[0]+5)*3.142/180)
                                                 vel2=vel2**(1/2.0)
                                                 projYH[0]=int(projX[0]*tan((angl[0]+5)*3.142/180)-5*projX[0]*projX[0]/(vel2*vel2*(cos((angl[0]+5)*3.142/180)**2)))
                                                 screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projYH[0]+2)))
                                                 
                                             else:
                                                 soundBmb.play()
                                                 cf[0]=1
                                                 cnter+=1
                                                 dstrX[cnter]=projX[0]+posX[0]
                                                 dstrY[cnter]=posY[0]-projYH[0]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 bend=dstrX[cnter]+dstrSize[cnter]
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])
                                                 if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projYH[0]-2)-posY[1])<50:
                                                     increase[0]=25
                                                     if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projYH[0]-2)-posY[1])<25:
                                                         increase[0]=50
                                                         if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projYH[0]-2)-posY[1])<10:
                                                               increase[0]=100
                                                     scoreVal[0]+=increase[0]
                                                     messgXc[0]=posX[1]
                                                     messgYc[0]=posY[1]
                                                     ic=increase[0]
                                         if af[0]==1 or bf[0]==1 or cf[0]==1:
                                             if b[0]!=1:
                                                 if af[0]==1:
                                                     if messgYa[0]>30:
                                                             mssgToScreen(str(ia),[255,255,255],messgXa[0],messgYa[0]-2)
                                                             messgYa[0]-=1
                                                             if sign[0]==1:
                                                                 messgXa[0]+=1
                                                             else:
                                                                 messgXa[0]-=1
                                                             if messgXa[0]==posX[1]+20:
                                                                 sign[0]=-1
                                                             elif messgXa[0]==posX[1]-20:
                                                                 sign[0]=1
                                                             
                                                     else:
                                                         wpn3cnt[0]+=1
                                                         b[0]=1
                                             if c[0]!=1:
                                                 if bf[0]==1:
                                                     if messgYb[0]>30:
                                                             
                                                             mssgToScreen(str(ib),[255,255,255],messgXb[0],messgYb[0]-2)
                                                             messgYb[0]-=1
                                                             if sign[0]==1:
                                                                 messgXb[0]+=1
                                                             else:
                                                                 messgXb[0]-=1
                                                             if messgXb[0]==posX[1]+20:
                                                                 sign[0]=-1
                                                             elif messgXb[0]==posX[1]-20:
                                                                 sign[0]=1
                                                             
                                                     else:
                                                         wpn3cnt[0]+=1
                                                         c[0]=1
                                             if d[0]!=1:
                                                 if cf[0]==1:
                                                     if messgYc[0]>30:
                                                             
                                                             mssgToScreen(str(ic),[255,255,255],messgXc[0],messgYc[0]-2)
                                                             messgYc[0]-=1
                                                             if sign[0]==1:
                                                                 messgXc[0]+=1
                                                             else:
                                                                 messgXc[0]-=1
                                                             if messgXc[0]==posX[1]+20:
                                                                 sign[0]=-1
                                                             elif messgXc[0]==posX[1]-20:
                                                                 sign[0]=1
                                                             
                                                     else:
                                                         wpn3cnt[0]+=1
                                                         d[0]=1
                                         if wpn3cnt[0]==3:
                                             abcd=downhill(traverse,astart,bend)
                                             projX[0]=4
                                             projY[0]=3
                                             projYH[0]=3
                                             projYL[0]=3
                                             break
                                         projX[0]+=1
                                         pygame.display.flip()



                                elif wpn[0]==4:
                                         soundBllt.play()
                                         while True:
                                             laserX=int(posX[0]+i1*cos(angl[0]*3.142/180)-2)
                                             laserY=int(posY[0]-i1*sin(angl[0]*3.142/180)-2)
                                             screen.blit(bullt2,(laserX,laserY+4))
                                             i1+=1
                                             
                                             if abs(laserX-posX[1])<20 and abs(laserY-posY[1]+4)<20 :
                                                     soundBmb.play()
                                                     scoreVal[0]+=75
                                                     messgX[0]=posX[1]
                                                     messgY[0]=posY[1]
                                                 
                                                     while messgY[0]>30:
                                                         screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                         screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                         screen.blit(tank[1],(450,posY[1]))
                                                         mssgToScreen(str(25),[255,255,255],messgX[0],messgY[0]-2)
                                                         mssgToScreen(str(25),[255,255,255],messgX[0]+10,messgY[0]-15)
                                                         mssgToScreen(str(25),[255,255,255],messgX[0],messgY[0]-29)
                                                         
                                                         messgY[0]-=1
                                                         if sign[0]==1:
                                                             messgX[0]+=1
                                                         else:
                                                             messgX[0]-=1
                                                         if messgX[0]==posX[1]+20:
                                                             sign[0]=-1
                                                         elif messgX[0]==posX[1]-20:
                                                             sign[0]=1
                                                         pygame.display.flip()    
                                                         clock.tick(100)
                                                     break
                                             pygame.display.flip()
                                             clock.tick(100)
                                         
                                         break
                                        
                                elif wpn[0]==0 or wpn[0]==1 or wpn[0]==3:
                                        if (posY[0]-2-projY[0])<cordy(projX[0]+posX[0],img12):
                                             if projX[0]+posX[0]>599:
                                                  projX[0]=4
                                                  projY[0]=3
                                            
                                                  break

                                                 
                                             projY[0]=int(projX[0]*tan(angl[0]*3.142/180)-5*projX[0]*projX[0]/(vel[0]*vel[0]*(cos(angl[0]*3.142/180)**2)))
                                             if wpn[0]==0:
                                                 screen.blit(bullt1,(projX[0]+posX[0],(posY[0]-projY[0]+2)))

                                             elif wpn[0]==1 or wpn[0]==3:
                                                 screen.blit(bullt,(projX[0]+posX[0],(posY[0]-projY[0]+2)))
                                             projX[0]+=1
                                             
                                        else:
                                            soundBmb.play()
                                            if wpn[0]==0:
                                                cnter+=1
                                                dstrX[cnter]=projX[0]+posX[0]
                                                dstrY[cnter]=posY[0]-projY[0]+2
                                                dstrSize[cnter]=75
                                                pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                img13=np.copy(img14)
                                                img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                img12=cv2.bitwise_and(img12,img13,mask=None)
                                                traverse=dstrX[cnter]-dstrSize[cnter]
                                                start_new_thread(downhill,(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter],))

                                            elif wpn[0]==1:
                                                cnter+=1
                                                dstrX[cnter]=projX[0]+posX[0]
                                                dstrY[cnter]=posY[0]-projY[0]+2
                                                dstrSize[cnter]=50
                                                pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                img13=np.copy(img14)
                                                img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                img12=cv2.bitwise_and(img12,img13,mask=None)
                                                traverse=dstrX[cnter]-dstrSize[cnter]
                                                abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                            elif wpn[0]==3:
                                                cnter+=1
                                                dstrX[cnter]=projX[0]+posX[0]
                                                dstrY[cnter]=posY[0]-projY[0]+2
                                                dstrSize[cnter]=50
                                                pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                img13=np.copy(img14)
                                                img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                img12=cv2.bitwise_and(img12,img13,mask=None)    

                                                traverse=dstrX[cnter]-dstrSize[cnter]
                                                #abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])
                                                start_new_thread(downhill,(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter],))


                                                
                                                
                                            if wpn[0]==0:
                                                if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                     increase[0]=25
                                                     if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                         increase[0]=50
                                                         if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                               increase[0]=100
                                                     scoreVal[0]+=increase[0]
                                                     messgX[0]=posX[1]
                                                     messgY[0]=posY[1]
                                                 
                                                     while messgY[0]>30:
                                                         screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                         screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                         screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                         mssgToScreen(str(increase[0]),[255,255,255],messgX[0],messgY[0]-2)
                                                         messgY[0]-=1
                                                         if sign[0]==1:
                                                             messgX[0]+=1
                                                         else:
                                                             messgX[0]-=1
                                                         if messgX[0]==posX[1]+20:
                                                             sign[0]=-1
                                                         elif messgX[0]==posX[1]-20:
                                                             sign[0]=1
                                                         pygame.display.flip()    
                                                         clock.tick(100)

                                            elif wpn[0]==1:
                                                if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                     increase[0]=10
                                                     if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                         increase[0]=20
                                                         if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                               increase[0]=50
                                                     scoreVal[0]+=increase[0]
                                                     messgX[0]=posX[1]
                                                     messgY[0]=posY[1]
                                                 
                                                     while messgY[0]>30:
                                                         screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                         screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                         screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                         mssgToScreen(str(increase[0]),[255,255,255],messgX[0],messgY[0]-2)
                                                         messgY[0]-=1
                                                         if sign[0]==1:
                                                             messgX[0]+=1
                                                         else:
                                                             messgX[0]-=1
                                                         if messgX[0]==posX[1]+20:
                                                             sign[0]=-1
                                                         elif messgX[0]==posX[1]-20:
                                                             sign[0]=1
                                                         pygame.display.flip()    
                                                         clock.tick(100)

                                                
                                            elif wpn[0]==3:
                                                if abs(projX[0]+posX[0]-posX[1])<50 and abs((posY[0]-projY[0]-2)-posY[1])<50:
                                                     increase[0]=25
                                                     if abs(projX[0]+posX[0]-posX[1])<25 and abs((posY[0]-projY[0]-2)-posY[1])<25:
                                                         increase[0]=50
                                                         if abs(projX[0]+posX[0]-posX[1])<10 and abs((posY[0]-projY[0]-2)-posY[1])<10:
                                                               increase[0]=100
                                                     scoreVal[0]+=increase[0]
                                                     messgX[0]=posX[1]
                                                     messgY[0]=posY[1]
                                                 
                                                     
                                                     while True:
                                                         screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                         
                                                         if messgY[0]>30:
                                                             mssgToScreen(str(increase[0]),[255,255,255],messgX[0],messgY[0]-2)
                                                             messgY[0]-=1
                                                             if sign[0]==1:
                                                                 messgX[0]+=1
                                                             else:
                                                                 messgX[0]-=1
                                                             if messgX[0]==posX[1]+20:
                                                                 sign[0]=-1
                                                             elif messgX[0]==posX[1]-20:
                                                                 sign[0]=1
                                                         else:
                                                             msfg[0]=1
                                                         if fl2[0]!=1:
                                                             if (posY[1]-projYT[0])<cordy(projXT[0]+posX[1],img12):
                                                                 if projXT[0]+posX[1]>580:
                                                                      posX[1]=580
                                                                      projXT[0]=4
                                                                      projYT[0]=3
                                                                      fl2[0]=1
                                                                      cntbt[0]=1

                                                                 
                                                                 projYT[0]=int(projXT[0]*tan(60*3.142/180)-5*projXT[0]*projXT[0]/(30*30*(cos(60*3.142/180)**2)))
                                                                 screen.blit(tank[1],(projXT[0]+posX[1],(posY[1]-projYT[0]-17)))
                                                                 projXT[0]+=1

                                                             else:
                                                                 posX[1]=projXT[0]+posX[1]
                                                                 projXT[0]=4
                                                                 projYT[0]=3
                                                                 fl2[0]=1
                                                                 cntbt[0]=1
                                                         else:
                                                             screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                             
                                                         if fl1[0]!=1:
                                                             if (posY[0]-projYT[1])<cordy(posX[0]-projXT[1],img12):
                                                                 if posX[0]-projXT[1]<20:
                                                                      posX[0]=10
                                                                      projXT[1]=4
                                                                      projYT[1]=3
                                                                      fl1[0]=1
                                                                      cntbt1[0]=1

                                                                 
                                                                 projYT[1]=int(projXT[1]*tan(60*3.142/180)-5*projXT[1]*projXT[1]/(30*30*(cos(60*3.142/180)**2)))
                                                                 screen.blit(tank[0],(posX[0]-projXT[1],(posY[0]-projYT[1]-17)))
                                                                 projXT[1]+=1

                                                             else:
                                                                 posX[0]=posX[0]-projXT[1]
                                                                 projXT[1]=4
                                                                 projYT[1]=3
                                                                 fl1[0]=1
                                                                 cntbt1[0]=1
                                                         else:
                                                             screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                         if msfg[0]==1 and cntbt1[0]==1 and cntbt[0]==1:
                                                             break
                                                         pygame.display.flip()   
                                                           
                                                     
                                            projX[0]=4
                                            projY[0]=3
                                            
                                            break      
                                
                                if wpn[1]==2:
                                         if posX[1]-projX[1]>599:
                                                  projX[1]=4
                                                  projY[1]=3
                                                  projYH[1]=3
                                                  projYL[1]=3
                                                  
                                                  break

                                                  
                                         
                                         if af[1]!=1:
                                             if (posY[1]-2-projY[1])<cordy(posX[1]-projX[1],img12):
                                                projY[1]=int(projX[1]*tan((180-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel[1]*vel[1]*(cos((180-angl[1])*3.142/180)**2)))
                                                screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projY[1]+2)))
                                                
                                             else:
                                                 soundBmb.play()
                                                 af[1]=1
                                                 cnter+=1
                                                 dstrX[cnter]=posX[1]-projX[1]
                                                 dstrY[cnter]=posY[1]-projY[1]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 astart=dstrX[cnter]-dstrSize[cnter]
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])
                                                 
                                                 if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         
                                                         scoreVal[1]+=increase[1]
                                                         messgXa[1]=posX[0]
                                                         messgYa[1]=posY[0]
                                                         ia1=increase[1]
                                         if bf[1]!=1:        
                                             if (posY[1]-2-projYL[1])<cordy(posX[1]-projX[1],img12):
                                                 vel11=(vel[1]*vel[1]*sin(2*(180-angl[1])*3.142/180)+300)/sin(2*(185-angl[1])*3.142/180)
                                                 vel11=vel11**(1/2.0)
                                                 projYL[1]=int(projX[1]*tan((185-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel11*vel11*(cos((185-angl[1])*3.142/180)**2)))
                                                 screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projYL[1]+2)))
                                                
                                             else:
                                                 soundBmb.play()
                                                 
                                                 bf[1]=1
                                                 cnter+=1
                                                 dstrX[cnter]=posX[1]-projX[1]
                                                 dstrY[cnter]=posY[1]-projYL[1]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])
                                                 if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projYL[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         scoreVal[1]+=increase[1]
                                                 
                                                     
                                                         messgXb[1]=posX[0]
                                                         messgYb[1]=posY[0]
                                                         ib1=increase[1]
                                         if cf[1]!=1:        
                                             if (posY[1]-2-projYH[1])<cordy(posX[1]-projX[1],img12):
                                                 vel21=(vel[1]*vel[1]*sin(2*(180-angl[1])*3.142/180)-300)/sin(2*(175-angl[1])*3.142/180)
                                                 vel21=vel21**(1/2.0)
                                                 projYH[1]=int(projX[1]*tan((175-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel21*vel21*(cos((175-angl[1])*3.142/180)**2)))
                                                 screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projYH[1]+2)))
                                                 
                                             else:
                                                 soundBmb.play()
                                                 
                                                 cf[1]=1
                                                 cnter+=1
                                                 dstrX[cnter]=posX[1]-projX[1]
                                                 dstrY[cnter]=posY[1]-projYH[1]+2
                                                 dstrSize[cnter]=25
                                                 pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                 img13=np.copy(img14)
                                                 img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                 img12=cv2.bitwise_and(img12,img13,mask=None)
                                                 bend=dstrX[cnter]+dstrSize[cnter]
                                                 cv2.imwrite(list1011[plyr],img12)
                                                 tux=pygame.image.load(list1011[plyr])
                                                 if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projYH[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projYH[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projYH[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                    
                                                         scoreVal[1]+=increase[1]
                                                         messgXc[1]=posX[0]
                                                         messgYc[1]=posY[0]
                                                         ic1=increase[1]

                                         if af[1]==1 or bf[1]==1 or cf[1]==1:
                                             if b[1]!=1:
                                                 if af[1]==1:
                                                     if messgYa[1]>30:
                                                             mssgToScreen(str(ia1),[255,255,255],messgXa[1],messgYa[1]-2)
                                                             messgYa[1]-=1
                                                             if sign[1]==1:
                                                                 messgXa[1]+=1
                                                             else:
                                                                 messgXa[1]-=1
                                                             if messgXa[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgXa[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             
                                                     else:
                                                         wpn3cnt[1]+=1
                                                         b[1]=1
                                             if c[1]!=1:
                                                 if bf[1]==1:
                                                     if messgYb[1]>30:
                                                             
                                                             mssgToScreen(str(ib1),[255,255,255],messgXb[1],messgYb[1]-2)
                                                             messgYb[1]-=1
                                                             if sign[1]==1:
                                                                 messgXb[1]+=1
                                                             else:
                                                                 messgXb[1]-=1
                                                             if messgXb[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgXb[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             
                                                     else:
                                                         wpn3cnt[1]+=1
                                                         c[1]=1
                                             if d[1]!=1:
                                                 if cf[1]==1:
                                                     if messgYc[1]>30:
                                                             
                                                             mssgToScreen(str(ic1),[255,255,255],messgXc[1],messgYc[1]-2)
                                                             messgYc[1]-=1
                                                             if sign[1]==1:
                                                                 messgXc[1]+=1
                                                             else:
                                                                 messgXc[1]-=1
                                                             if messgXc[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgXc[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             
                                                     else:
                                                         wpn3cnt[1]+=1
                                                         d[1]=1                
                                         if wpn3cnt[1]==3:
                                             abcd=downhill(0,astart,bend)
                                             projX[1]=4
                                             projY[1]=3
                                             projYH[1]=3
                                             projYL[1]=3
                                             
                                             break
                                         projX[1]+=1
                                         pygame.display.flip()

                                elif wpn[1]==4:
                                         soundBllt.play()
                                         while True:
                                             laserX2=int(posX[1]+i2*cos(angl[1]*3.142/180)-2)
                                             laserY2=int(posY[1]-i2*sin(angl[1]*3.142/180)-2)
                                             screen.blit(bullt2,(laserX2,laserY2+4))
                                             i2+=1
                                             
                                             if abs(laserX2-posX[0])<20 and abs(laserY2-posY[0]+4)<20 :
                                                     soundBmb.play()
                                                     scoreVal[1]+=75
                                                     messgX[1]=posX[0]
                                                     messgY[1]=posY[0]
                                                 
                                                     while messgY[1]>30:
                                                         screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                        
                                                         screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                         screen.blit(tank[0],(posX[0],posY[0]))
                                                         mssgToScreen(str(25),[255,255,255],messgX[1],messgY[1]-2)
                                                         mssgToScreen(str(25),[255,255,255],messgX[1]+10,messgY[1]-15)
                                                         mssgToScreen(str(25),[255,255,255],messgX[1],messgY[1]-29)
                                                         
                                                         messgY[1]-=1
                                                         if sign[1]==1:
                                                             messgX[1]+=1
                                                         else:
                                                             messgX[1]-=1
                                                         if messgX[1]==posX[0]+20:
                                                             sign[1]=-1
                                                         elif messgX[1]==posX[0]-20:
                                                             sign[1]=1
                                                         pygame.display.flip()    
                                                         clock.tick(100)
                                                     break
                                             pygame.display.flip()
                                             clock.tick(100)
                                         
                                         break
                                        
                                elif wpn[1]==0 or wpn[1]==1 or wpn[1]==3:     
                                            if (posY[1]-2-projY[1])<cordy(posX[1]-projX[1],img12):
                                                 if posX[1]-projX[1]<0:
                                                      projX[1]=4
                                                      projY[1]=3
                                                      
                                                      break
                                                 projY[1]=int(projX[1]*tan((180-angl[1])*3.142/180)-5*projX[1]*projX[1]/(vel[1]*vel[1]*(cos((180-angl[1])*3.142/180)**2)))
                                                 if wpn[1]==0:
                                                     screen.blit(bullt1,(posX[1]-projX[1],(posY[1]-projY[1]+2)))

                                                 if wpn[1]==1 or wpn[1]==3 :
                                                     screen.blit(bullt,(posX[1]-projX[1],(posY[1]-projY[1]+2)))    
                                                 projX[1]+=1
                                                 
                                            else:
                                                soundBmb.play()
                                                if wpn[1]==0:
                                                    cnter+=1
                                                    dstrX[cnter]=posX[1]-projX[1]
                                                    dstrY[cnter]=posY[1]-projY[1]+2
                                                    dstrSize[cnter]=75
                                                    pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                    img13=np.copy(img14)
                                                    img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                    img12=cv2.bitwise_and(img12,img13,mask=None)
                                                    traverse=dstrX[cnter]-dstrSize[cnter]
                                                    abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                                elif wpn[1]==1:
                                                    cnter+=1
                                                    dstrX[cnter]=posX[1]-projX[1]
                                                    dstrY[cnter]=posY[1]-projY[1]+2
                                                    dstrSize[cnter]=50
                                                    pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                    img13=np.copy(img14)
                                                    img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                    img12=cv2.bitwise_and(img12,img13,mask=None)
                                                    traverse=dstrX[cnter]-dstrSize[cnter]
                                                    abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                                elif wpn[1]==3:
                                                    cnter+=1
                                                    dstrX[cnter]=posX[1]-projX[1]
                                                    dstrY[cnter]=posY[1]-projY[1]+2
                                                    dstrSize[cnter]=50
                                                    pygame.draw.circle(screen,[0,0,0],[dstrX[cnter],dstrY[cnter]],dstrSize[cnter])
                                                    img13=np.copy(img14)
                                                    img13=cv2.circle(img13,(dstrX[cnter],dstrY[cnter]),dstrSize[cnter],(0,0,0),-1)
                                                    img12=cv2.bitwise_and(img12,img13,mask=None)    
                                                    traverse=dstrX[cnter]-dstrSize[cnter]
                                                    abcd=downhill(traverse,dstrX[cnter]-dstrSize[cnter],dstrX[cnter]+dstrSize[cnter])

                                                if wpn[1]==0:
                                                    if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         scoreVal[1]+=increase[1]
                                                         messgX[1]=posX[0]
                                                         messgY[1]=posY[0]
                                                         while messgY[1]>30:
                                                             screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                           
                                                             screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                             screen.blit(tank[1],(450,posY[1]))
                                                             mssgToScreen(str(increase[1]),[255,255,255],messgX[1],messgY[1]-2)
                                                             messgY[1]-=1
                                                             if sign[1]==1:
                                                                 messgX[1]+=1
                                                             else:
                                                                 messgX[1]-=1
                                                             if messgX[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgX[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             pygame.display.flip()    
                                                             clock.tick(100)


                                                elif wpn[1]==1:
                                                    if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=10
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=20
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=50
                                                         scoreVal[1]+=increase[1]
                                                         messgX[1]=posX[0]
                                                         messgY[1]=posY[0]
                                                         while messgY[1]>30:
                                                             screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                           
                                                             screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                             screen.blit(tank[1],(450,posY[1]))
                                                             mssgToScreen(str(increase[1]),[255,255,255],messgX[1],messgY[1]-2)
                                                             messgY[1]-=1
                                                             if sign[1]==1:
                                                                 messgX[1]+=1
                                                             else:
                                                                 messgX[1]-=1
                                                             if messgX[1]==posX[0]+20:
                                                                 sign[1]=-1
                                                             elif messgX[1]==posX[0]-20:
                                                                 sign[1]=1
                                                             pygame.display.flip()    
                                                             clock.tick(100)


                                                elif wpn[1]==3:
                                                     if abs(posX[1]-projX[1]-posX[0])<50 and abs((posY[1]-projY[1]-2)-posY[0])<50:
                                                         increase[1]=25
                                                         if abs(posX[1]-projX[1]-posX[0])<25 and abs((posY[1]-projY[1]-2)-posY[0])<25:
                                                             increase[1]=50
                                                             if abs(posX[1]-projX[1]-posX[0])<10 and abs((posY[1]-projY[1]-2)-posY[0])<10:
                                                                   increase[1]=100
                                                         scoreVal[1]+=increase[1]
                                                         messgX[1]=posX[0]
                                                         messgY[1]=posY[0]
                                                         while True:
                                                             screen.blit(tux,(0,0))                    #cant reverse the order as it will occupy whole screen and relace down one
                                                            
                                                             if messgY[1]>30:
                                                                 mssgToScreen(str(increase[1]),[255,255,255],messgX[1],messgY[1]-2)
                                                                 messgY[1]-=1
                                                                 if sign[1]==1:
                                                                     messgX[1]+=1
                                                                 else:
                                                                     messgX[1]-=1
                                                                 if messgX[1]==posX[0]+20:
                                                                     sign[1]=-1
                                                                 elif messgX[1]==posX[0]-20:
                                                                     sign[1]=1

                                                             else:
                                                                 msfg[1]=1

                                                             if fl2[1]!=1:
                                                                 if (posY[1]-projYT1[0])<cordy(projXT1[0]+posX[1],img12):
                                                                     if projXT1[0]+posX[1]>580:
                                                                          posX[1]=580
                                                                          projXT1[0]=4
                                                                          projYT1[0]=3
                                                                    
                                                                          fl2[1]=1
                                                                          cntbt[1]=1

                                                                     
                                                                     projYT1[0]=int(projXT1[0]*tan(60*3.142/180)-5*projXT1[0]*projXT1[0]/(30*30*(cos(60*3.142/180)**2)))
                                                                     screen.blit(tank[1],(projXT1[0]+posX[1],(posY[1]-projYT1[0]-17)))
                                                                     projXT1[0]+=1

                                                                 else:
                                                                     posX[1]=projXT1[0]+posX[1]
                                                                     projXT1[0]=4
                                                                     projYT1[0]=3
                                                            
                                                                     fl2[1]=1
                                                                     cntbt[1]=1
                                                             else:
                                                                 screen.blit(tank[1],(posX[1],cordy(posX[1],img12)-17))
                                                                 
                                                             if fl1[1]!=1:
                                                                 if (posY[0]-projYT1[1])<cordy(posX[0]-projXT1[1],img12):
                                                                     

                                                                     
                                                                     projYT1[1]=int(projXT1[1]*tan(60*3.142/180)-5*projXT1[1]*projXT1[1]/(30*30*(cos(60*3.142/180)**2)))
                                                                     screen.blit(tank[0],(posX[0]-projXT1[1],(posY[0]-projYT1[1]-17)))
                                                                     projXT1[1]+=1
                                                                     if posX[0]-projXT1[1]<40:
                                                                          posX[0]=10
                                                                          projXT1[1]=4
                                                                          projYT1[1]=3
                                                                        
                                                                          fl1[1]=1
                                                                          cntbt1[1]=1

                                                                 else:
                                                                     posX[0]=posX[0]-projXT1[1]
                                                                     projXT1[1]=4
                                                                     projYT1[1]=3
                                                            
                                                                     fl1[1]=1
                                                                     cntbt1[1]=1
                                                             else:
                                                                 screen.blit(tank[0],(posX[0],cordy(posX[0],img12)-17))
                                                             if msfg[1]==1 and cntbt1[1]==1 and cntbt[1]==1:
                                                                 break
                                                             pygame.display.flip()   
                                                 
                                                     
                                                     
                                                           
                                                     
                                                projX[1]=4
                                                projY[1]=3
                                        
                                                break
                                pygame.display.flip()
                elif mx>230 and mx<360: 
                    if my>380 and my<410:
                        if plyr==0:
                            while True:
                                screen.fill([200,200,200],rect=(190,190,210,300))
                                screen.fill([100,100,100],rect=(200,200,190,280))
                                screen.fill([200,200,200],rect=(210,170,120,20))
                                mssgToScreen('WEAPONS',[255,255,255],225,172)
                                screen.blit(shwWpn,(215,205))
                                mssgToScreen('BIG SHOT',[255,255,255],265,205)
                                screen.blit(shwWpn2,(215,255))
                                mssgToScreen('SINGLE SHOT',[255,255,255],265,255)
                                screen.blit(shwWpn3,(215,305))
                                mssgToScreen('THREE SHOT',[255,255,255],265,305)
                                screen.blit(shwWpn4,(215,355))
                                mssgToScreen('BACKTRACK',[255,255,255],265,355)
                                screen.blit(shwWpn5,(215,405))
                                mssgToScreen('LASER',[255,255,255],265,405)
                                for event in pygame.event.get():
                                        if event.type==MOUSEBUTTONDOWN:
                                            wpnX[0],wpnY[0]=pygame.mouse.get_pos()
                                            if wpnX[0]>265 and wpnX[0]<455:
                                                if wpnY[0]>205 and wpnY[0]<250:
                                                    wpn[0]=0
                                                    brk[0]=1
                                                    break



                                                elif wpnY[0]>255 and wpnY[0]<300:
                                                    wpn[0]=1
                                                    brk[0]=1


                                                elif wpnY[0]>305 and wpnY[0]<350:
                                                    wpn[0]=2
                                                    brk[0]=1

                                                elif wpnY[0]>355 and wpnY[0]<400:
                                                    wpn[0]=3
                                                    brk[0]=1

                                                elif wpnY[0]>405 and wpnY[0]<450:
                                                    wpn[0]=4
                                                    brk[0]=1    
                
                                pygame.display.flip()
                                if brk[0]==1:
                            
                                    break
                                
                                clock.tick(100)

                        else:
                            while True:
                                screen.fill([200,200,200],rect=(190,190,210,300))
                                screen.fill([100,100,100],rect=(200,200,190,280))
                                screen.fill([200,200,200],rect=(210,170,120,20))
                                mssgToScreen('WEAPONS',[255,255,255],225,172)
                                screen.blit(shwWpn,(215,205))
                                mssgToScreen('BIG SHOT',[255,255,255],265,205)
                                screen.blit(shwWpn2,(215,255))
                                mssgToScreen('SINGLE SHOT',[255,255,255],265,255)
                                screen.blit(shwWpn3,(215,305))
                                mssgToScreen('THREE SHOT',[255,255,255],265,305)
                                screen.blit(shwWpn4,(215,355))
                                mssgToScreen('BACKTRACK',[255,255,255],265,355)
                                screen.blit(shwWpn5,(215,405))
                                mssgToScreen('LASER',[255,255,255],265,405)
                                for event in pygame.event.get():
                                        if event.type==MOUSEBUTTONDOWN:
                                            wpnX[1],wpnY[1]=pygame.mouse.get_pos()
                                            if wpnX[1]>265 and wpnX[1]<455:
                                                if wpnY[1]>205 and wpnY[1]<250:
                                                    wpn[1]=0
                                                    brk[1]=1
                                                    break



                                                elif wpnY[1]>255 and wpnY[1]<300:
                                                    wpn[1]=1
                                                    brk[1]=1


                                                elif wpnY[1]>305 and wpnY[1]<350:
                                                    wpn[1]=2
                                                    brk[1]=1

                                                elif wpnY[1]>355 and wpnY[1]<400:
                                                    wpn[1]=3
                                                    brk[1]=1

                                                elif wpnY[1]>405 and wpnY[1]<450:
                                                    wpn[1]=4
                                                    brk[1]=1        
                     
                
                                pygame.display.flip()
                                if brk[1]==1:
                                
                                    break
                                
                                clock.tick(100)


                        
    mssgToScreen(str(scoreVal[0]),[200,20,100],30,60)
    mssgToScreen(str(scoreVal[1]),[200,20,100],550,60)
    if plyr==0:    
        if mx1[0]>332 and mx1[0]<470:                         
            screen.fill([100,0,0],rect=(327,447,mx1[0]-332,25))
            mssgToScreen(str((mx1[0]-332)*100/136),[0,0,0],440,425)
            vel[0]=(mx1[0]-332)*100/136
    
        elif mx1[0]>470:
            screen.fill([100,0,0],rect=(327,447,136,25))
            vel[0]=100
            mssgToScreen(str(100),[0,0,0],440,425)
            
        elif mx1[0]<332:
            mssgToScreen(str(0),[0,0,0],440,425)
            vel[0]=0
      
        if (prevvel[0]-vel[0])!=0:
            ConnectionListener().Send({"action": "plyr1vel","vel0s":vel[0] })

        if (prevangl[0]-angl[0])!=0:
            ConnectionListener().Send({"action": "plyr1angl","angl0s":angl[0] })     
            
        prevvel[0]=vel[0]
        prevangl[0]=angl[0]
        mssgToScreen(str(angl[0]),[255,255,255],165,460)

    else:
        if mx1[1]>332 and mx1[1]<470:              #ConnectionListener().Send({"action": "plyr1wpn","wpn0s":wpn[0] })           
            screen.fill([100,0,0],rect=(327,447,mx1[1]-332,25))
            mssgToScreen(str((mx1[1]-332)*100/136),[0,0,0],440,425)
            vel[1]=(mx1[1]-332)*100/136
 
        elif mx1[1]>470:
            screen.fill([100,0,0],rect=(327,447,136,25))
            vel[1]=100
            mssgToScreen(str(100),[0,0,0],440,425)
 
        elif mx1[1]<332:
            mssgToScreen(str(0),[0,0,0],440,425)
            vel[1]=0

        if (prevvel[1]-vel[1])!=0:
            ConnectionListener().Send({"action": "plyr0vel","vel1s":vel[1] })

        if (prevangl[1]-angl[1])!=0:
            ConnectionListener().Send({"action": "plyr0angl","angl1s":angl[1] })     
    
            
        prevvel[1]=vel[1]
        prevangl[1]=angl[1]
        mssgToScreen(str(angl[1]),[255,255,255],165,460)
        
    pygame.display.flip()
    clock.tick(200)

