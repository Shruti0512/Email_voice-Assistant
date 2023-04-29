# We use libraries 
# 1- SpeechRecognition lib which used to record audio through your microphone and we are going to give real time audio input to this program
# 2- yagmail lib which is used to automate the gmail using SMTP Protocol 
# 3- pyaudio lib is supporting library for speechrecognition means we are connecting the microphone with a laptop for recording real time audio

import speech_recognition as sr
import yagmail

recognizer=sr.Recognizer()
#this statement means that we are converting our microphone as a source
with sr.Microphone() as source:
    print('Clearing Background noise:')
#there may be some background noises due to which accuracy can be decreased so to clear background voices for this script so it is necessary to clear noises
    recognizer.adjust_for_ambient_noise(source,duration=2)
    print('waiting for your message:')
# now we are going to record audio from our microphone
    recordedaudio=recognizer.listen(source)
    print('Done Recording:')
# now we will convert this audio in english , instead of typing we can type audio directly into text
# here we are using google's API to convert into english for sending the text
try:
       print('Printing the message: ')
       text=recognizer.recognize_google(recordedaudio,language='en-US')

       print('Your Message: {}',format(text))

except Exception as ex:
        print(ex)

# automating emails

# in this we will type receiver's email address 
print('to whom u want to send')
receiver=str(input())
message=text
# in this sender's space we will type our email address
sender=yagmail.SMTP('chaturvedishruti2001@gmail.com') 
# now send the mail from sender's end
sender.send(to=receiver,subject='This is a second  automated mails',contents=message)
# for smtp protocol use app password to access our own gmail.
# and for chaturvedishruti2001@gmail.com password is saved in keyring.

