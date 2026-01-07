import random
import os
import streamlit as st
import pandas as pd

core_folder = os.getcwd()
sim_folder = os.path.join(core_folder, "Simulator Files")
dialogue_file_path = os.path.join(sim_folder, "player_dialogue.csv")
banter_file_path = os.path.join(sim_folder, "guest_dialogue.csv")
banter_file = pd.read_csv(banter_file_path, header = None)

gif_folder = os.path.join(sim_folder, "GIFs")

dialogue_file = pd.read_csv(dialogue_file_path)


def call_intro(player):
    player_first_name = player.split(" ")[0]
    player_second_name = player.split(" ")[1]
    titles =[
        player,
        player_first_name,
        f"Mr. {player_second_name}",
        f"Young {player}",
        f"Big {player}",
        f"the GOAT, {player}"
    ]
    chosen_title = random.choice(titles)
    dialogue = random.choice(dialogue_file["Dialogue"]).replace("[Player]",chosen_title)
    return(st.write('"' + dialogue + '"'))

def show_gif(player):
    player_gif_folder = os.path.join(gif_folder,player)
    gif = (
        player_gif_folder + "/" + random.choice(os.listdir(player_gif_folder))
    )
    print(gif)
    return(st.image(gif,width = 500))

def introduce_player(player):
    call_intro(player)
    show_gif(player)

def call_guest_banter(guest):
    #need to randomise
    st.write('"Haha, screw you too, Buddy."')
    pass

def call_guest_intro(guest):
    #need to randomise?
    return(st.write(f"Please put your hands together for our guest {guest["Name"]}!"))