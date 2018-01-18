
from tkinter import *
from math import *
import time

Fenetre = Tk()
Fenetre.title("Bounce")
Fenetre.configure(width=1200, height=680)

Game = Canvas(Fenetre, bg="#E2FFEE", width=1200, height=680)
Game.grid()

Game.create_rectangle(585, 325, 615, 355, fill="#873831", outline="#873831", tags="player")
Game.create_rectangle(5, 650, 1197, 600, fill="#009E48", outline="#009E48", tags="land")

# *** variable physique ***
# réglage de la vitesse d'actualisation
time_ms = 10 ## en millisecondes
time_s = time_ms / 1000 ## en secondes
# accélération en x et y
## px/s/frame
aX = 0
aY = 0
# pesanteur
## px/s/frame
g = 1
# vitesses en x et y
## px/s/frame
vX = 0
vY = 0

# *** variable game play ***
# effet des controles sur l'accélération
a = 5 ## px/s/frame
# nombre de rebond à effectuer
bouncy = 3 ## nombre de rebond
# nombre de rebond
bouncy_nbr = 0 ##compteur
# seuil de vitesse pour effectuer les rebonds
seuil_rebond = 1
# indiquateur de position au sol au en l'air
landed = False

def acc_on(evt) :

    global aY, aX, landed, bouncy_nbr
    key = evt.keysym

    if(key == "Right") :
        aY = a
    if(key == "Left") :
        aY = -a
    if(key == "Up") :
        aX = a
        landed = False
        bouncy_nbr = 0
    if(key == "Down") :
        aX = -a
    if(key == "a") :
        Game.coords("player", 585, 325, 615, 355)
        vX = 0
        vY = 0
        aX = 0
        aY = 0

def acc_off(evt) :

    global aY, aX

    key = evt.keysym

    if(key == "Right") :
        aY = 0
    if(key == "Left") :
        aY = 0
    if(key == "Up") :
        aX = 0
    if(key == "Down") :
        aX = 0


def calcule_distance(a, b) :
    return sqrt((a-b) * (a-b))

def collision() :

    global vY, landed, bouncy_nbr

    if(landed == False and Game.coords("player")[3] >= 600) :
        if(bouncy_nbr < bouncy and vY <= seuil_rebond) :
            vY = -vY / 5
            bouncy_nbr += 1
        else :
            vY = 0
            landed = True


def MoinsVitesse(evt) :

    global vY, vX

    vY = 0
    vX = 0

Fenetre.bind('<KeyPress>', acc_on)
Fenetre.bind('<KeyRelease>', acc_off)



def Deplacement() :

    global aX, aY, vX, vY

    collision()

    vY += (aX - g) * time_s
    vX += aY * time_s

    print(vY)
    if(landed == False) :
        Game.move("player", vX * time_ms, -vY * time_ms) ## -vx car l'axe des y est orienté vers le bas
    Fenetre.after(time_ms, Deplacement)

Deplacement()

Fenetre.mainloop()