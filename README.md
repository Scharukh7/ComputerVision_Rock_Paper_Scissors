# Computer Vision (Rock, Paper, Scissors Game) - Documentation Guideline
 "run cvproject.ipynb or attempt6.py script to play the game"

## Milestone 1: Create the model

- Image project model with four different classes: Rock, Paper, Scissors, Nothing was created using Teachable-Machine website. Website helps creats the model. 

- The model was downloaded from the website using the "Tensorflow" tab.

>This is how the code looks like when downloaded:

"""python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('YOUR_MODEL.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break      
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()"""

## Milestone 2: Install the dependencies

- All the dependencies were installed required to work with the project such as opencv-python, tensorflow and ipykernel as the code was worked on Visual Studio Code in Linux.

## Milestone 3: Create Rock-Paper-Scissors Game

- The game was created where a user input is required for two players to play the game.
- Player and Computer varaibles were created and both required int(input "message"). For computer random() was imported to generate the random choices.
- a game was coded using if-elif-else statement to determine the winner.
- Then, a function was created to simulate the whole game.

"""python
def Choices():
	player = int(input('Rock', 'Paper', 'Scissors')
	computer = random.choices('Rock','Paper','Scissors')
def Game(player, computer):
	if player == computer:
        messages = 'Draw'
        #return messages
    elif player == 'rock' and computer == 'scissors' or player == 'paper' and computer == 'rock' or player == 'scissors' and computer == 'paper':
        messages= 'Player'
        #return messages
    elif player == 'rock' and computer == 'paper' or player == 'paper' and computer == 'scissors' or player == 'scissors' and computer == 'rock':
        messages = 'Computer'
        #return messages
    else:
        messages = 'Error'
return messages"""


## Milestone 4: Use the camera to play Rock-Paper-Scissors

- The code was combined to use the webcam with the function that ask the user for an input. The manual input was replaced by the computer vision model prediction.
using the argmax as it returns the argument for the target function that returns the max value from the targe function.

"""python
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
"""

- the countdown was added to the game so it gives the user a bit of time to decide on their choice. For this task, time function was imported. and time.time() was used as the current time. 
  an intial time for the game was also created as a boolean, "first = True". To know if the game has started "gameStarted = False".
- Introduction menu was created using opencv, cv2.putText:

"""python
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
    """
- as well as for the ingame screen cv2.putText along with the if statement for introScreen with the countdown was coded, as soon as the countdown = 0, the choices are shown

"""python
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
    """        
- and the ending screen along with the results of the game where the winner is concluded and shows on the screen

"""python
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
   """         
- the score and player, computer point were also printed on the screen using cv2.putText inside the while loop

"""python
    message1 = ("Round: " + str(rounds) + " ") 
    message2 = ("Player Score: " + str(player_wins))
    message3 = ("Computer Score: " + str(computer_wins))
    cv2.putText(frame, message1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    cv2.putText(frame, message2, (420,40),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    cv2.putText(frame, message3, (420,70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
"""

- finally the game overlay was ran in a sequence inside the while loop:

"""python
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
"""
## Conclusions

In my conclusion, I have learnt to have a good use my functions and split the code into various parts so it is easier to detect if there is an issue or if any change is needed. What I would like to improve is the use of globals, as there's been alot of use of globals in the code, it would be better to find an alternate way to work with the code and keep it DRY without too much of globals. This project helped me understand the various way anything can be worked on with the machine vision using openCV as well as the use of tensorflow and to work around with the data models.

