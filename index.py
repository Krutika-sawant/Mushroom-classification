

import base64
from distutils.log import fatal
from pickletools import optimize
import streamlit as st
# from array import array;
import pandas as pd
import numpy as np
import pickle
import sklearn
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
# st.image(mush.png, width=100)

st.set_page_config(
    page_title="Mushroom Classification",
    page_icon="🍄",
)

with st.sidebar:
    choose = option_menu("Mushroom classification", ["Home", "Prediction", "Contact"],
                         icons=['house', 'clipboard-data',
                                'person lines fill'],
                         menu_icon="app-indicator", default_index=1,
                         styles={"container": {"padding": "5!important", "background-color": "#0E1117"},
                                 "icon": {"color": "orange", "font-size": "25px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#262730"},
                                 "nav-link-selected": {"background-color": "#FF4B4B"},
                                 }
                         )

if choose == "Home":
    st.title("Mushroom Classification 🍄")
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("let's find out whether your mushroom is edible😋 or poisonous🤮?")
    st.write(" **👉This WebApp will help you to predict whether your mushroom is poisonous or edible.**")
    st.write(" **👉Enter the correct features of your mushroom in input section.**")
    st.write(" **👉After you will get the predicted result whether your mushroom is edible or poisonous.**")
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("    ")


if choose == "Prediction":
    st.title("Mushroom Classification 🍄")
    col1, col2, col3 = st.columns(3)
    with col1:
        cap_surface = st.selectbox(
            "Select Cap Surface", ("Fibrous", "Grooves", "Scaly", "Smooth"))

        bruises = st.selectbox(
            "Select Bruises", ("True", "False"))

        odor = st.selectbox("Select Odor", ("Almond", "Anise",
                                            "Creosote", "Fishy", "Foul", "Musty", "None", "Pungent", "Spicy"))

        gill_spacing = st.selectbox(
            "Select  Gill Spacing", ("close", "crowded", "distant"))

        gill_size = st.selectbox(
            "Select Gill size", ("broad", "narrow"))

    with col2:

        gill_color = st.selectbox("Select  Gill Color", ("black", "brown", "buff",
                                                         "chocolate", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"))

        stalk_root = st.selectbox("Select Stalk root ", (
            "bulbous", "club", "cup", "equal", "rhizomorphs", "rooted", "missing"))

        stalk_surface_above_ring = st.selectbox(
            "Select  Stalk surface above ring ", ("fibrous", "scaly", "silky", "smooth"))

        stalk_surface_below_ring = st.selectbox(
            "Select Stalk surface below ring ", ("fibrous", "scaly", "silky", "smooth"))

        ring_type = st.selectbox("Select Ring type ", ("cobwebby", "evanescent",
                                                       "flaring", "large", "none", "pendant", "sheathing", "zone"))

    with col3:
        stalk_color_above_ring = st.selectbox("Select Stalk color above ring", (
            "brown", "buff", "cinnamon", "gray", "orange", "pink", "red", "white", "yellow"))

        stalk_color_below_ring = st.selectbox("Select Stalk color below ring", (
            "brown", "buff", "cinnamon", "gray", "orange", "pink", "red", "white", "yellow"))

        spore_print_color = st.selectbox("Select Spore print color", (
            "black", "brown", "buff", "chocolate", "green", "orange", "purple", "white", "yellow"))

        population = st.selectbox("Select Population", ("abundant",
                                                        "clustered", "numerous", "scattered", "several", "solitary"))

        habitat = st.selectbox("Select Habitat", (
            "grasses", "leaves", "meadows", "paths", "urban", "waste", "woods"))

    if cap_surface == "f":
        _cap_surface = 0
    elif cap_surface == "g":
        _cap_surface = 1
    elif cap_surface == "s":
        _cap_surface = 2
    else:
        _cap_surface = 3

    if bruises == "f":
        _bruises = 0
    else:
        _bruises = 1

    if odor == "a":
        _odor = 0
    elif odor == "c":
        _odor = 1
    elif odor == "f":
        _odor = 2
    elif odor == "l":
        _odor = 3
    elif odor == "m":
        _odor = 4
    elif odor == "n":
        _odor = 5
    elif odor == "p":
        _odor = 6
    elif odor == "s":
        _odor = 7
    else:
        _odor = 8

    if gill_spacing == "c":
        _gill_spacing = 0
    elif gill_spacing == "d":
        _gill_spacing = 1
    else:
        _gill_spacing = 2

    if gill_size == "b":
        _gill_size = 0
    else:
        _gill_size = 1

    if gill_color == "b":
        _gill_color = 0
    elif gill_color == "e":
        _gill_color = 1
    elif gill_color == "g":
        _gill_color = 2
    elif gill_color == "h":
        _gill_color = 3
    elif gill_color == "k":
        _gill_color = 4
    elif gill_color == "n":
        _gill_color = 5
    elif gill_color == "o":
        _gill_color = 6
    elif gill_color == "p":
        _gill_color = 7
    elif gill_color == "r":
        _gill_color = 8
    elif gill_color == "u":
        _gill_color = 9
    elif gill_color == "w":
        _gill_color = 10
    else:
        _gill_color = 11

    if stalk_root == "b":
        _stalk_root = 0
    elif stalk_root == "c":
        _stalk_root = 1
    elif stalk_root == "e":
        _stalk_root = 2
    elif stalk_root == "r":
        _stalk_root = 3
    elif stalk_root == "u":
        _stalk_root = 4
    elif stalk_root == "z":
        _stalk_root = 5
    else:
        _stalk_root = 6

    if stalk_surface_above_ring == "f":
        _stalk_surface_above_ring = 0
    elif stalk_surface_above_ring == "k":
        _stalk_surface_above_ring = 1
    elif stalk_surface_above_ring == "s":
        _stalk_surface_above_ring = 2
    else:
        _stalk_surface_above_ring = 3

    if stalk_surface_below_ring == "f":
        _stalk_surface_below_ring = 0
    elif stalk_surface_below_ring == "k":
        _stalk_surface_below_ring = 1
    elif stalk_surface_below_ring == "s":
        _stalk_surface_below_ring = 2
    else:
        _stalk_surface_below_ring = 3

    if stalk_color_above_ring == "b":
        _stalk_color_above_ring = 0
    elif stalk_color_above_ring == "c":
        _stalk_color_above_ring = 1
    elif stalk_color_above_ring == "e":
        _stalk_color_above_ring = 2
    elif stalk_color_above_ring == "g":
        _stalk_color_above_ring = 3
    elif stalk_color_above_ring == "n":
        _stalk_color_above_ring = 4
    elif stalk_color_above_ring == "o":
        _stalk_color_above_ring = 5
    elif stalk_color_above_ring == "p":
        _stalk_color_above_ring = 6
    elif stalk_color_above_ring == "w":
        _stalk_color_above_ring = 7
    else:
        _stalk_color_above_ring = 8

    if stalk_color_below_ring == "b":
        _stalk_color_below_ring = 0
    elif stalk_color_below_ring == "c":
        _stalk_color_below_ring = 1
    elif stalk_color_below_ring == "e":
        _stalk_color_below_ring = 2
    elif stalk_color_below_ring == "g":
        _stalk_color_below_ring = 3
    elif stalk_color_below_ring == "n":
        _stalk_color_below_ring = 4
    elif stalk_color_below_ring == "o":
        _stalk_color_below_ring = 5
    elif stalk_color_below_ring == "p":
        _stalk_color_below_ring = 6
    elif stalk_color_below_ring == "w":
        _stalk_color_below_ring = 7
    else:
        _stalk_color_below_ring = 8

    if ring_type == "c":
        _ring_type = 0
    elif ring_type == "e":
        _ring_type = 1
    elif ring_type == "f":
        _ring_type = 2
    elif ring_type == "l":
        _ring_type = 3
    elif ring_type == "n":
        _ring_type = 4
    elif ring_type == "p":
        _ring_type = 5
    elif ring_type == "s":
        _ring_type = 6
    else:
        _ring_type = 7

    if spore_print_color == "b":
        _spore_print_color = 0
    elif spore_print_color == "h":
        _spore_print_color = 1
    elif spore_print_color == "k":
        _spore_print_color = 2
    elif spore_print_color == "n":
        _spore_print_color = 3
    elif spore_print_color == "o":
        _spore_print_color = 4
    elif spore_print_color == "r":
        _spore_print_color = 5
    elif spore_print_color == "u":
        _spore_print_color = 6
    elif spore_print_color == "w":
        _spore_print_color = 7
    else:
        _spore_print_color = 8

    if population == "a":
        _population = 0
    elif population == "c":
        _population = 1
    elif population == "n":
        _population = 2
    elif population == "s":
        _population = 3
    elif population == "v":
        _population = 4
    else:
        _population = 5

    if habitat == "d":
        _habitat = 0
    elif habitat == "g":
        _habitat = 1
    elif habitat == "l":
        _habitat = 2
    elif habitat == "m":
        _habitat = 3
    elif habitat == "p":
        _habitat = 4
    elif habitat == "u":
        _habitat = 5
    else:
        _habitat = 6


    inputs = np.array([[_cap_surface, _bruises, _odor, _gill_spacing, _gill_size, _gill_color, _stalk_root, _stalk_color_above_ring,
                  _stalk_surface_below_ring, _stalk_color_above_ring, _stalk_color_below_ring, _ring_type, _spore_print_color, _population, _habitat]])

    with open('model.pickle', 'rb') as h:
      model = pickle.load(h)

      prediction = model.predict(inputs)
      if prediction == 0:
        _prediction = "Mushroom is Edible ✔️"
      else:
         _prediction = "Mushroom is Poisonous ✖️"

      if st.button('Predict'):
        st.write(_prediction)

if choose == "Contact":
    st.title("Contact")

    st.write("    ")
    st.write("    ")


    st.write(":point_right: [GitHub](https://github.com/Krutika-sawant)")
    st.write("    ")

    st.write(":point_right: [Linkedin](https://www.linkedin.com/in/krutika-chudji-sawant)")
