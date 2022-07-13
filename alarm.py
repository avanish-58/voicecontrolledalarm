#import library
# import libraries(datetime,time,pyttsx3)
import time,pyttsx3
from datetime import datetime

import speech_recognition as sr



print("Hello, welcome to my alarming interface...")
print("It is based on 24 hours clock format...")

Name = input("Enter your name: ")

# printing the current time 
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is: ", current_time)

# Enter the time(Hours and minute)
print("Say the time (HH24:MM): ")


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

    try:
        # using google speech recognition
        Time = r.recognize_google(audio_text)
    except:
         print("Sorry, I did not get that")


# starting the loop
while True:
    # Getting the standard time with the
    # help of datetime module
    Standard_time=datetime.now().strftime("%H:%M")
    # sleep the program for about 1 sec
    time.sleep(1)
    # if condition to check wether the input 
    # time has matched or not
    if Time==Standard_time:
        count=0
        while count<=10:
            count=count+1
            # creating a engine for voice mode
            engine=pyttsx3.init()
            # setting the voice
            engine.say("Wake up"+Name)
            engine.runAndWait()
        print("Thankyou For using the Interface")
        break
