import wolframalpha
import wikipedia
import PySimpleGUI as sg
import speech_recognition as sr
import pyttsx3

app_id= "733LGE-PXLKW2YXGA"
client= wolframalpha.Client(app_id)

def initialization():
    while(True):
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                chunk_size = chunk_size) as source: 
            r.adjust_for_ambient_noise(source) 
            SpeakText("Yes what do you want to know?")
            audio = r.listen(source) 
                  
            try: 
                text = r.recognize_google(audio) 
                print ("you said: " + text) 
                SpeakText(text)
                gui(text)
            #error occurs when google could not understand what was said 
              
            except sr.UnknownValueError: 
                SpeakText("Google Speech Recognition could not understand audio") 
              
            except sr.RequestError as e: 
                SpeakText("Could not request results from Google"  
                                         "Speech Recognition service; {0}".format(e)) 


def gui(text):
    sg.theme('DefaultNoMoreNagging')	# Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Hello I am JARVIS, Your virtual Assistant. How can I help you?')],
                [sg.Text('Enter your curiousity: '), sg.Text(text)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('JARVIS, The Virtual Assistant!', layout)
    event,value=window.read()
    if event in (None,'Cancel'):
        exit()
    else:
        answer(text)
    print("Inside gui")
    window.close()


def answer(curiosity):
    try:
        res=client.query(curiosity)        
        wol_res=next(res.results).text
        wiki_res=wikipedia.summary(curiosity, sentences=2)
        sg.PopupNonBlocking("Wolframalpha: ",wol_res,"Wikipedia: ",wiki_res)
        SpeakText(wol_res)
        SpeakText(wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        res=client.query(curiosity)        
        wol_res=next(res.results).text
        sg.PopupNonBlocking(wol_res)
        SpeakText(wol_res)
    except wikipedia.exceptions.PageError:
        res=client.query(curiosity)        
        wol_res=next(res.results).text
        sg.PopupNonBlocking(wol_res)
        SpeakText(wol_res)
    except:
        wiki_res=wikipedia.summary(curiosity, sentences=2)
        sg.PopupNonBlocking(wiki_res)
        SpeakText(wiki_res)


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


#enter the name of usb microphone that you found 
mic_name = "Microsoft Sound Mapper - Input"
#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer() 

#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 
#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 

#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone
#is not working, an error will pop up saying "device_id undefined"

with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                            chunk_size = chunk_size) as source: 
#wait for a second to let the recognizer adjust the
#energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source) 
    SpeakText("Say Something")
#listens for the user's input 
    audio = r.listen(source)
    initial_speech = r.recognize_google(audio)
    initial_speech = initial_speech.lower()
    print(initial_speech)
    if initial_speech == "hello":
        initialization()
        


    



