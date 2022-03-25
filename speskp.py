import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser
import os



engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wish():
    hr=int(datetime.datetime.now().hour)
    mint=int(datetime.datetime.now().minute)
    #print(hr,mint)

    if hr==0 and hr<12:
        speak("good morning")
        print("Good Morning")

    elif hr>=12 and hr<18:
        speak("good afternoon")
        print("Good Afternoon")

    elif hr>=18 and hr<=20:
        speak("good evening")
        print("Good Evening")

    print("hi gourav, how may i help you")
    speak("hi gourav, how may i help you")

def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"you said : {query}\n")

    except Exception as e:
        print("say that again")
        return "None"

    return query



if __name__ == '__main__':
     wish()
while True :

#if 1:
    query=takecmd().lower()
    #print(query)

    if 'wikipedia' in query :
        speak("Searching wikipedia")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("wikipedia say ...")
        print("Wikipedia Say -",result)
        speak(result)
    elif "break" in query:
        break
    elif "open youtube" in query:
        webbrowser.open("youtube.com")

    elif "open google" in query:
        speak("opening google")
        webbrowser.open("google.com")

    elif 'open chrome'in query:
        path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"
        speak("opening chrome")
        os.startfile(path)
    elif 'time'in query:
        curtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {curtime}")

    elif 'add' or 'addition' in query:
        sum=0
        query=query.replace("addition of","")
        query=query.replace('add','')
        numbers=query.split("and")
        try:
          mapno=map(int,numbers)
          numbers1=list(mapno)
          for no in range(len(numbers1)):
            print(no)
            sum=sum+numbers1[no]
          print(f"sum of the number is{sum}")
          speak(f"sum of the no is {sum}")
        except :
           print("cannot recognize your command sir")
           speak("cannot recognize your command sir")

    '''elif 'subtract' in query :
        sub=0
        query=query.replace("subtraction","")
        numbers=query.split("and")
        try:
          mapn=map(int,numbers)
          no1=list(mapn)
          for no in range(len(no1)):
              sub=no1[no]-sub
    else:
        print("Sorry ,say another command sir")
        speak("Sorry ,say another command sir")'''




