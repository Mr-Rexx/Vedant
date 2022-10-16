# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:53:26 2022

@author: Vedan
"""
from gtts import gTTS   

import os 
 
mytext = str("")
 
language = 'en'
   
myobj = gTTS(text=mytext, lang=language, slow=False, tld = 'co.uk') 
    
myobj.save("readin_text.mp3") 