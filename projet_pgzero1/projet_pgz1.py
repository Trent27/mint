import pgzrun
HEIGHT = 500
WDTH = 400    

print()
print("avance le baller jusqua l'autre cote de la ligne: w(deplacer a droite),a(continue tout droit). ")

#sprint ballon 
ball = Actor("b-ball.png")
ball.pos=(0,255)
spin=3

def draw():
    """"fonction qui decrit comment pygame zero
    prepare la fenetre"""
   purple = (255,0,255)
   screen.fill("red")
#Rotation du ballon
def update():
  ball.amgle -= spin

 def on_mouse_down(key):
   if key== keys.w:
     ball.y -= 0
    elif key== keys.a:
      ball.x += 255


pgzrun.go()