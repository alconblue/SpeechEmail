import pyaudio,os
import speech_recognition as sr
import smtplib
import pyttsx
import time

r = sr.Recognizer()
engine = pyttsx.init()

with sr.Microphone(device_index= None) as source:
        r.adjust_for_ambient_noise(source)
        engine.say("Email id")
        engine.runAndWait()
        time.sleep(5)
        audio = r.listen(source)
        time.sleep(3)
        engine.say("Got it!")
        engine.runAndWait()

command = r.recognize_google(audio)
command = command.replace(" ", "")
describe = "Sending message to" + command
engine.say(describe)
engine.runAndWait()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("Your Email ID", "Your password")
with sr.Microphone(device_index= None) as source:
        r.adjust_for_ambient_noise(source)
        engine.say("Message to be sent")
        engine.runAndWait()
        time.sleep(5)
        audio = r.listen(source)
        engine.say("Got it!")
        engine.runAndWait()
msg = r.recognize_google(audio)
print msg
server.sendmail("Your Email ID", command, msg)
server.quit()