#Supreme Studios
#Cops & Robbers
#Justin Rodriguez, Thomas Delgado
#Collect a total of 9 keys to leave and escape the Nassau County Jail!!

from gamelib import*#import game library

#objects and initial settings
game = Game (800,600,"Cops & Robbers")
bk = Image("pacman-background-2.jpg",game)
bk.resizeTo(game.width, game.height)
robber = Image("robber.png",game)
robber.resizeBy(-85)
cop = Image("police.png", game)
cop.resizeBy(-90)
key = Image("key.jpg",game)


#Level 1 - game loop

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    robber.draw()
    cop.draw()
    if keys.Pressed[K_UP]:
        robber.y -= 4#
    if keys.Pressed[K_DOWN]:
        robber.y += 4
    if keys.Pressed[K_RIGHT]:
        robber.x += 4
    if keys.Pressed[K_LEFT]:
        robber.x -= 4
    if robber.collidedWith(cop):
        game.over = True

    game.update(30)

game.over = False
#Break in code
while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    robber.draw()
    game.update(30)
    
game.quit()
