# Write your code here :-)
import pgzrun #Load the pygame zero module
import random #Load the random module

# Set up the game screen dimensions
WIDTH = 800
HEIGHT = 600

#Colours used
white = (255,255,255)

#Background
bg = Actor('skyliner')

#character
student = Actor('student')
student.x = 350
student.y = 550

#coin
coin = Actor('coin')
coin.x = random.randint(20,780) #Randomise start position
coin.y = 0

#money
dollars = Actor('dollars')
dollars.x = random.randint(20,780) #Randomise start position
dollars.y = 0

#sign
sign = Actor('sign')
sign.x = random.randint(20,780) #Randomise start position
sign.y = 0

# Set up game variables
score = 0
lives = 3
game_over = False

def update():
    global score
    global lives
    global game_over
    ##### character ###
    # Move ship left and right#
    if keyboard.left:
        student.x = student.x -5
    if keyboard.right:
        student.x = student.x +5
    #Stop character off screen
    if student.x < 60:
        student.x = 60
    if student.x > 740:
        student.x = 740
    ####### COIN ####
    # Move Coin Down
    coin.y += 4 + score / 5
    #reset the coin at the top
    if coin.y > 600:
        coin.x = random.randint(20,780)
        coin.y = 0
    #Coin collision with student
    if coin.colliderect(student):
        sounds.collect.play()
        coin.x = random.randint(20,780)
        coin.y = 0
        score = score + 1


    ##### SIGN
    #Move sign down
    sign.y += 4
    #Reset sign at the top
    if sign.y > 600:
        sign.x = random.randint(20,780)
        sign.y = 0
    #Sign collision with studnet
    if sign.colliderect(student):
        sounds.lose.play()
        sign.x =random.randint(20,780)
        coin.y = 0
        score -= 1
        lives = lives -1

    #End Games at 0 lives
    if lives == 0:
        game_over = True
        coin.y = 0
        sign.y = 0
        dollars.y = 0


    #Money###
    #Bomb down the page
    dollars.y += 5
    #Reset at Top
    if dollars.y > 600:
        dollars.x = random.randint(20,780)
        dollars.y = 0
    # collision with ship
    if dollars.colliderect(student):
        sounds.explosion.play()
        dollars.x = random.randint(20,780)
        dollars.y = 0


def draw():
    bg.draw()

    if game_over:
        screen.draw.text('GAME OVER', (230, 200), color = white, fontname = 'publicpixel', fontsize=30)
        screen.draw.text('FINAL SCORE: ' + str(score), (180, 300), color = white, fontname = 'publicpixel', fontsize=30)
    else:
      student.draw()
    coin.draw()
    dollars.draw()
    sign.draw()
    screen.draw.text('Score: '+ str(score), (15, 10), color=(white), fontname = 'publicpixel', fontsize=15)
    screen.draw.text('Lives: '+ str(lives), (650, 10), color=(white), fontname = 'publicpixel', fontsize=15)
