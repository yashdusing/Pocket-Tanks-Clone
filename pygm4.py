import PodSixNet.Channel
import PodSixNet.Server
from time import sleep,time

player1=0
chncnt=0
mov=[0,0]
f=[0,0]
wpn=[-1,-1]
f1=[0,0]
f11=[0,0]
f111=[0,0]
angl=[-1,-1]
vel=[-1,-1]
class ClientChannel(PodSixNet.Channel.Channel): #this is for recieving from client
    def Network(self, data):
        print 'a'
        print data

    def Network_plyr0mv(self, data):
        global f
        print 'b'
        #deconsolidate all of the data from the dictionary
     
        #horizontal or vertical?
        mov[0] = data["mov0s"]
        #x of placed line
        print mov[0]
        f[0]=1
     
        #y of placed line
        
     
        #player number (1 or 0
     
        #id of game given by server at start of gam
        #tells server to place line

    def Network_plyr1mv(self, data):
        global f
        print 'b'
        #deconsolidate all of the data from the dictionary
     
        #horizontal or vertical?
        
        #x of placed line
        mov[1] = data["mov1s"]
        print mov[1]
        f[1]=1

    def Network_plyr1wpn(self,data):
         global wpn
         wpn[0]=data["wpn0s"]
         print time()
         print wpn[0]
         f1[0]=1
         

    def Network_plyr0wpn(self,data):
         global wpn
         wpn[1]=data["wpn1s"]
         print wpn[1]
         f1[1]=1

    def Network_plyr1angl(self,data):
         global angl
         angl[0]=data["angl0s"]
         print angl[0]
         f11[0]=1

    def Network_plyr0angl(self,data):
         global angl
         angl[1]=data["angl1s"]
         print angl[1]
         f11[1]=1

    def Network_plyr1vel(self,data):
         global vel
         vel[0]=data["vel0s"]
         print vel[0]
         f111[0]=1

    def Network_plyr0vel(self,data):
         global vel
         vel[1]=data["vel1s"]
         print vel[1]
         f111[1]=1        

         

      

class BoxesServer(PodSixNet.Server.Server):
    
    channelClass = ClientChannel   #wen do this all function of this class gets executed
 
    def Connected(self, channel, addr):
       global chncnt
       
       print 'fuckoff'
       print 'new connection:', channel
       if chncnt==1:
           self.player10=self.player11
       self.player11=channel
       channel.Send({"action":"player","plyrno":chncnt})
       chncnt+=1

       
       

    def h(self):
       global mov
       self.player10.Send({"action":"mov0rv","mov1r":mov[1]})
       mov[1]=0

    def h1(self):
       global mov
       self.player11.Send({"action":"mov1rv","mov0r":mov[0]})
       mov[0]=0                   

    def h20(self):
        global wpn
        self.player10.Send({"action":"plyr0wpnrv","wpn1rv":wpn[1]})

    def h21(self):
        global wpn
        self.player11.Send({"action":"plyr1wpnrv","wpn0rv":wpn[0]})

    def h30(self):
        global angl
        self.player10.Send({"action":"plyr0anglrv","angl1rv":angl[1]})

    def h31(self):
        global angl
        self.player11.Send({"action":"plyr1anglrv","angl0rv":angl[0]})

    def h40(self):
        global vel
        self.player10.Send({"action":"plyr0velrv","vel1rv":vel[1]})

    def h41(self):
        global vel
        self.player11.Send({"action":"plyr1velrv","vel0rv":vel[0]})    
        
        
        
           

    
        
        
 
print "STARTING SERVER ON LOCALHOST"
host, port='', 80
boxesServe=BoxesServer(localaddr=((host),int(port)))
while True:
    if f[0]==1:
        boxesServe.h1()
        f[0]=0                  
                          
    if f[1]==1:
        boxesServe.h()
        f[1]=0

    if f1[0]==1:
        boxesServe.h21()
        f1[0]=0

    if f1[1]==1:
        boxesServe.h20()
        f1[1]=0

    if f11[0]==1:
        boxesServe.h31()
        f11[0]=0

    if f11[1]==1:
        boxesServe.h30()
        f11[1]=0

    if f111[0]==1:
        boxesServe.h41()
        f111[0]=0

    if f111[1]==1:
        boxesServe.h40()
        f111[1]=0     
        
    boxesServe.Pump()
    sleep(0.01)
    
