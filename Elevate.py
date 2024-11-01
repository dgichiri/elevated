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

msgs = [ "Together, we can build something incredible. Let's foster a spirit of collaboration and see how far we can go. #TeamBuilding. Lucille",
"Unity is strength. When we work together, we can move mountains. Let's leverage our unique strengths for the greater good. #Bonding. Lucille",
"Remember, we're not just colleagues, we're a team. And as a team, we thrive. Let's make every day count. #Collaboration. Lucille",
"In the face of challenges, we stand stronger together. Let's turn obstacles into opportunities. #TeamBuilding. Lucille",
"Diversity is our strength. Let's celebrate our unique perspectives and work together to create a harmonious workspace. #Collaboration. Lucille",
"The whole is greater than the sum of its parts. Let's combine our skills and talents to achieve greatness. #TeamBuilding. Lucille",
"Let's break down barriers and build bridges. Together, we can create a workspace that thrives on collaboration and mutual respect. #Bonding. Lucille",
"Remember, we're all in this together. Let's support each other and work towards our common goals. #TeamBuilding. Lucille",
"Our success is intertwined. Let's help each other grow and thrive in a collaborative environment. #Collaboration. Lucille",
"Let's turn our differences into strengths. Together, we can create a dynamic and thriving team. #Bonding. Lucille",
"The power of collaboration is endless. Let's work together to create a workplace that inspires and motivates us. #TeamBuilding. Lucille",
"Unity in diversity is our strength. Let's celebrate our unique perspectives and work together towards our common goals. #Collaboration. Lucille",
"Remember, we're not just a team, we're a family. And like a family, we should support and uplift each other. #Bonding. Lucille",
"Let's foster a culture of collaboration and mutual respect. Together, we can achieve great things. #TeamBuilding. Lucille",
"Our success is a reflection of our teamwork. Let's work together to create a workplace that thrives on collaboration and unity. #Collaboration. Lucille",
"Let's break down silos and build bridges. Together, we can create a workspace that encourages collaboration and innovation. #Bonding. Lucille",
                     
        ]

f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write("Dear" name +" , Karibu. "+msg)
