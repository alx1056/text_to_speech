 
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 

#Gets the Operating System invovled
import os 

#will return name of user on computer
name = os.getlogin() 

# The text that you want to convert to audio 
mytext = 'Hello ' + name + ', I have been up to doing a lot of productive yet unproductive things in your absence.....'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("talk_back.mp3") 
  
# Playing the converted file 
os.startfile("talk_back.mp3") 
