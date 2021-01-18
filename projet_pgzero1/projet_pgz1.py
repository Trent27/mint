import pgzrun
HEIGHT = 500
WDTH = 400    


def draw():
    """"fonction qui decrit comment pygame zero
    prepare la fenetre"""
   purple = (255,0,255)
   screen.fill("red")
 
   screen.blit("ballon",(200,0))
   def update():
   ballon.left += 2
    if ballon.left > WIDTH:
        ballon.right = 0

 def on_mouse_down(pos):
    if ballon.collidepoint(pos):
        print("Eek!") 


pgzrun.go()