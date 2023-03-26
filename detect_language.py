#sound/audio modules
from gtts import gTTS
import gtts
from playsound import playsound

#import the operating system
import os

#other modules
import argparse
import numpy
from textblob import TextBlob
import extract
import csv
from textblob import TextBlob
from langdetect import detect
import pycld2 as cld2
# Specifying the language for
# detection

#create a function for the process
def setup_language_processing():
   
    with open('processed/text_detected/text_detected.txt', "r") as f:
        contents = f.read()
        #print (contents)
        the_lang = detect(contents)

        with open('processed/text_detected/language_type.txt', 'w', newline="") as file:
            isReliable, textBytesFound, details, vectors = cld2.detect(
                contents, returnVectors=True
            )
            print(vectors)
            file.write("The output of the languages detected in the given image are as follows;\n " + str(vectors))


    # read the file the output text detected processed is in
    with open('processed/text_detected/language_type.txt', "r") as f:
        contents = f.read()
        #print (contents)
        #save the read file in a variable audio
        audio = contents

        #get the variable and start to process it for the sound output
        tts = gtts.gTTS(audio)

        # save the audio file
        tts.save("processed/audio/audio_detected.mp3")

        # play the audio file
        playsound("processed/audio/audio_detected.mp3")

        # in spanish
        #tts = gtts.gTTS(audio, lang="es")
        #tts.save("processed/audio/spanish_audio_detected.mp3")
        #playsound("processed/audio/spanish_audio_detected.mp3")

        # all available languages along with their IETF tag
        #print(gtts.lang.tts_langs())
        
#if the_lang == 'en':
#            file.write("The output of the language detected is " +the_lang+"glish")
#isReliable, textBytesFound, details, vectors = cld2.detect(
#    the_lang, returnVectors=True
#)
#print(vectors)        

setup_language_processing()