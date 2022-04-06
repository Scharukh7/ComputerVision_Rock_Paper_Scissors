#%%
import cv2
from keras.models import load_model
import numpy as np
import random
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(-1)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def gameWinner(player, computer):
    global message
    if player == computer:
        message = 'Draw'
        return message
    elif player == 'rock' and computer == 'scissors':
        message = 'Player'
        return message
    elif player == 'paper' and computer == 'rock':
        message = 'Player'
        return message
    elif player == 'scissors' and computer == 'paper':
        message = 'Player'
        return message
    if player == 'rock' and computer == 'paper':
        message = 'Computer'
        return message
    elif player == 'paper' and computer == 'scissors':
        message = 'Computer'
        return message
    elif player == 'scissors' and computer == 'rock':
        message = 'Computer'
        return message
    else:
        message = 'No Outcome'
        return message
 

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)

    #computer predicting choices
    options = ('rock','paper','scissors')
    #using data predictions as user inputs by returnig the indices of the max element of the array
    player_value = np.argmax(prediction)
    #assigned player_value to player for choices
    player = player_value
    #computer using random choices
    computer = random.choice(options)
    

    if prediction[0][0] > 0.5:
        print('rock')
        player = 'rock'
    elif prediction[0][1] > 0.5:
        print('paper')
        player = 'paper'
    elif prediction[0][2] > 0.5:
        print('scissors')
        player = 'scissors'
    else:
        print('nothing')
    
    message = gameWinner(player, computer)
    print(f'Player: {player}, vs, Computer: {computer}, message: {message}')

    # Press q to close the window
    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


# %%
