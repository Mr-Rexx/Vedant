# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:21:21 2022

@author: Vedan
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 
from gtts import gTTS   

import os 
 
mytext = str("Monty Python is the name of an Anglo-American comedy group known for their TV show Monty Python's Flying Circus (BBC, 1969), as well as films such as Monty Python and the Holy Grail (1975), stage shows, and albums. The group has achieved international popularity, especially among the computer science community. The Python language was named after the group. The term spam, now used for unsolicited email and other unwanted digital communications, also comes from a Monty Python sketch in which a café humorously insists on serving tinned meat (or spam) with everything. Other jokes, scenarios, and names taken from the group are often found in examples and even official Python documentation. So, if you ever encounter strange names or odd situations when going through tutorials, now you know why.")#+text+str(". Welcome to python 3. We highly appreciate you to use spyder 3 for your programming")
 
language = 'en'
   
myobj = gTTS(text=mytext, lang=language, slow=False, tld = 'co.uk') 
    
myobj.save("readin_text.mp3") 
  