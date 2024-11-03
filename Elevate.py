# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Welcome to CO Fun Fest in Diani
        
         """)

msgs = [ "Welcome to the CO Fun Fest! Let's reconnect, rejuvenate and shine together
          We also call ourselves team eagle
          We soar high",

                     
        ]

f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write("Dear", name +" , Karibu. "+msg)
