import random
import os
import streamlit as st
import pandas as pd

core_folder = os.getcwd()
sim_folder = os.path.join(core_folder, "Simulator Files")
dialogue_file_path = os.path.join(sim_folder, "dialogue.csv")
gif_folder = os.path.join(sim_folder, "GIFs")

dialogue_file = pd.read_csv(dialogue_file_path, header = None)

def call_intro(player):
    player_first_name = player.split(" ")[0]
    player_second_name = player.split(" ")[1]
    titles =[
        player_first_name,
        f"Mr. {player_second_name}",
        f"Young {player_first_name}",
        f"Big {player_first_name}",
        f"the GOAT {player_second_name}"
    ]
    chosen_title = random.choice(titles)
    dialogue = str(dialogue_file.sample(1)).replace("[Player]",chosen_title)
    return(dialogue)

def show_gif(player):
    player_gif_folder = os.path.join(gif_folder,player)
    gif = random.choice(os.listdir(player_gif_folder))
    return(st.image(gif))