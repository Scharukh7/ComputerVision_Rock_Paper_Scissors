#%%
import cv2
from keras.models import load_model
import numpy as np
import random
import time

def keyStart():
    #gameBegins()
    global introScreen, countdown, gameStarted, choices, itsEnd
    if gameStarted == False:
        cv2.putText(frame,"press 'a' to start the game",(120,150), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,0,0), 2)
        if cv2.waitKey(20) == ord ('a'):
            if gameStarted == False:
                introScreen = True
                countdown = current_time + 5
    if gameStarted == True and itsEnd == False:
        cv2.putText(frame, "press 'p' to play another round", (80,150), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,0,0), 2)
        if cv2.waitKey(20) == ord('p'):
            introScreen = True
            choices = False
            countdown = current_time + 5
            initialGameIntro()
        
def playerChoices():
    global playerC

    player_value = np.argmax(prediction)
    playerC = player_value

    if prediction[0][0] > 0.5:
        #print('rock')
        playerC = 'rock'
    elif prediction[0][1] > 0.5:
        #print('paper')
        playerC = 'paper'
    elif prediction[0][2] > 0.5:
        #print('scissors')
        playerC = 'scissors'
    else:
        #print('No Outcome')
        playerC = 'No Outcome'

def computerChoices():
    global options, computerC, choices
    options = ('rock', 'paper', 'scissors')
    computerC = random.choice(options)

def gameWinner(player, computer):
    global player_wins, computer_wins, rounds, update_score, messages
    
    if player == computer:
        messages = 'Draw'
        #return messages
    elif player == 'rock' and computer == 'scissors' or player == 'paper' and computer == 'rock' or player == 'scissors' and computer == 'paper':
        messages= 'Player'
        #return messages
    elif player == 'rock' and computer == 'paper' or player == 'paper' and computer == 'scissors' or player == 'scissors' and computer == 'rock':
        messages = 'Computer'
        #return messages
    elif playerC == 'No Outcome':
        messages = 'Error'
    if update_score == False and messages == 'Player':
        player_wins += 1
        rounds += 1
    elif update_score == False and messages == 'Computer':
        computer_wins += 1
        rounds += 1
    update_score = True
    print(rounds)
    return messages

 
def initialgameScreen():
    playerChoices()
    #gameWinner()
    #creating a text label for the player
    cv2.putText(frame,"Player", (45,380), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    #creating a text label for the computer
    cv2.putText(frame,"Computer", (440,380), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,255),2)
    #creating a versus label in between player and computer
    cv2.putText(frame, "VERSUS", (180,420),cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))
    #text from player
    cv2.putText(frame, str(playerC), (50,420), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

def initialGameIntro():
    #gameBegins()
    playerChoices()
    global introScreen, gameStarted, update_score, choices, options
    update_score = False
    if choices == False:
        computerChoices()
        choices = True
    if introScreen:
        #cv2.rectangle(frame, (10,430), (440, 350), (0,255,255), -1)
        # Player label
        cv2.putText(frame, "Player", (45,380), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        # Computer label
        cv2.putText(frame, "Computer", (440,380), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        # vs separator
        cv2.putText(frame, str(int(countdown-current_time)), (280,420), cv2.FONT_HERSHEY_TRIPLEX, 3, (0,0,255), 2)
        # Create the text of the interpretted choice from the buffer
        cv2.putText(frame, playerC, (20,420), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
        # Create the text of the computer's random choice
        cv2.putText(frame, random.choice(options), (480,420), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
        if int(countdown-current_time) <= 0:
            introScreen = False
            gameStarted = True
            gameBegins()

def gameBegins():
    #keyStart()
    global first, introScreen, gameStarted, itsEnd, update_score, player_wins, computer_wins
    global rounds
    print("Game in progress")
    #creating a text label for the player
    cv2.putText(frame,"Player", (45,380), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    #creating a text label for the computer
    cv2.putText(frame,"Computer", (440,380), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,255),2)
    #creating a versus label in between player and computer
    cv2.putText(frame, "VERSUS", (180,420),cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))
    #choices printing from player
    cv2.putText(frame, str(playerC), (50,420), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    #random choice printing from computer
    cv2.putText(frame, computerC, (440, 420), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

    #winner evaluation and ending the game once the winner is found
    if player_wins == 3:
        itsEnd = True
        introScreen = False
        gameStarted = True
        cv2.putText(frame, "GAMEOVER, Player Wins.", (110,110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        cv2.putText(frame, "Press 'Q' to exit", (210,140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    elif computer_wins == 3:
        itsEnd = True
        gameStarted = True
        introScreen = False
        cv2.putText(frame, "GAMEOVER, Computer Wins.", (110,110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        cv2.putText(frame, "Press 'Q' to exit", (210,140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    else:
        if gameWinner(playerC, computerC) == "Player":
            cv2.putText(frame, "Player Wins", (250,210), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        elif gameWinner(playerC, computerC) == "Computer":
            cv2.putText(frame, "Computer Wins", (250,210), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        elif gameWinner(playerC, computerC) == "Draw":
            cv2.putText(frame, "Draw", (270,210), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(frame, "Failed to choose", (200,210), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)  

#Declaring Variables
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(-1)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#***Declaring all variables***
playerC = ''
#computer
computerC = 'No Outcome'
#choices if they're being used
choices = False
#Game Intro Screen
introScreen = False
#Game started
gameStarted = False
#function to run first
first = True
#player total wins
player_wins = 0
#computer total wins
computer_wins = 0
#number of rounds 
rounds = 1
#update rounds
update_score = False
#countdown start from 5seconds
countdown = False
#end of game
itsEnd = False
#time
current_time = time.time()
#result = messages
while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    #show score and number of rounds on the frame
    message1 = ("Round: " + str(rounds) + " ") 
    message2 = ("Player Score: " + str(player_wins))
    message3 = ("Computer Score: " + str(computer_wins))
    cv2.putText(frame, message1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    cv2.putText(frame, message2, (420,40),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    cv2.putText(frame, message3, (420,70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)

    current_time = time.time()

    #print choices on the terminal
    print(f'Player: {playerC}, vs, Computer: {computerC}')

    #Display in which sequence overlay(functions) of the game will run
    if itsEnd == True:
        pass
    if introScreen == True:
        initialGameIntro()
    elif gameStarted == True and introScreen == False:
        gameBegins()
        keyStart()
    else:
        initialgameScreen()
        keyStart()

    #cv2.namedWindow("Rock Paper Scissors")
    cv2.imshow("Rock Paper Scissors", frame)

    # Press q to close the window
    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #itsEnd = True
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()



# %%
