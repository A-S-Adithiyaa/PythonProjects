import time
import pyttsx3


engine = pyttsx3.init()

def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1


time_splits = [20, 20, 10, 10, 10, 10, 20, 20]
exercises = ["Normal Plank", "Elbow Plank", "Right-leg Raised Plank", "Left-leg Raised Plank", "Right Slant Plank", "Left Slant Plank", "Normal Plank", "Elbow Plank"]

for i in range(len(time_splits)):
    print("5 Second to change the exercise...")
    engine.say("5 Second to change the exercise...")
    engine.runAndWait()
    time.sleep(5)
    print("You are now performing,", exercises[i])
    engine.say("You are now performing," + exercises[i])
    engine.runAndWait()
    countdown(time_splits[i])
    
