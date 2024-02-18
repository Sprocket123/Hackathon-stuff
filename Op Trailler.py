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


def update():
    global score
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

        sign.x =random.randint(20,780)
        coin.y = 0
        score = score -1


def draw():
    bg.draw()
    student.draw()
    coin.draw()
    dollars.draw()
    sign.draw()
    screen.draw.text('Score: '+ str(score), (15, 10), color=(white), fontname = 'publicpixel', fontsize=15)

