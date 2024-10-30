# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Welcome to Jenga BD- Reset, Reconnect, Drive.
        
         """)

msgs = ["  Let’s recharge our energies, bond as a team, and thrive together",
" Thrilled to have you here! Together, we’ll recharge, bond, and thrive",
" Welcome aboard! Let’s recharge our spirits, bond closely, and thrive in our goals",
" Excited to start this journey with you! Let’s recharge, bond, and thrive",
"  Ready to recharge, bond, and thrive as a team?",
" Together, we’ll recharge, bond, and thrive",
"  Let’s recharge our creativity, bond over ideas, and thrive in success",
" Happy to have you! Let’s recharge, bond, and thrive together",
"  Let’s recharge our efforts, bond as a team, and thrive in our mission",
" Excited to collaborate with you! Let’s recharge, bond, and thrive",
"  Together, we’ll recharge our strengths, bond, and thrive",
" Let’s recharge our enthusiasm, bond as a team, and thrive",
"  Ready to recharge, bond, and thrive in our journey?",
" Thrilled to have you! Let’s recharge, bond, and thrive together",
"  Let’s recharge our passion, bond over our goals, and thrive",
" Excited to work with you! Let’s recharge, bond, and thrive",
"  Together, we’ll recharge our energies, bond, and thrive",
" Let’s recharge our creativity, bond as a team, and thrive",
"  Ready to recharge, bond, and thrive in our endeavors?",
" Happy to have you here! Let’s recharge, bond, and thrive together",
"  Let’s recharge our efforts, bond closely, and thrive",
" Excited to collaborate! Let’s recharge, bond, and thrive",
"  Together, we’ll recharge our strengths, bond, and thrive",
" Let’s recharge our enthusiasm, bond as a team, and thrive",
"  Ready to recharge, bond, and thrive in our mission?",
" Thrilled to have you! Let’s recharge, bond, and thrive together",
"  Let’s recharge our passion, bond over our goals, and thrive",
" Excited to work with you! Let’s recharge, bond, and thrive",
"  Together, we’ll recharge our energies, bond, and thrive",
" Let’s recharge our creativity, bond as a team, and thrive",
"  Ready to recharge, bond, and thrive in our journey?",
" Happy to have you here! Let’s recharge, bond, and thrive together",
"  Let’s recharge our efforts, bond closely, and thrive",
" Excited to collaborate! Let’s recharge, bond, and thrive",
"  Together, we’ll recharge our strengths, bond, and thrive",
" Let’s recharge our enthusiasm, bond as a team, and thrive",
"  Ready to recharge, bond, and thrive in our endeavors?",
" Thrilled to have you! Let’s recharge, bond, and thrive together",
"  Let’s recharge our passion, bond over our goals, and thrive",
" Excited to work with you! Let’s recharge, bond, and thrive",

        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" ,Karibu. "+msg)
