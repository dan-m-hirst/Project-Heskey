import streamlit as st
from time import sleep
import random
import pandas as pd
from team_algorithm import generate_fairest_teams
#need to run in terminal "streamlit run webUI.py"
#How/when do I put in the unfairness score?

def get_teams(all_player_stats_path, players_playing_path):
    full_stats = pd.read_csv(all_player_stats_path)
    active_players = pd.read_csv(players_playing_path, header = None)[0]

    fairest_teams = generate_fairest_teams(full_stats, active_players)

    team_a = list(fairest_teams["Team A"])
    random.shuffle(team_a)
    team_b = list(fairest_teams["Team B"])
    random.shuffle(team_b)
    return {"Team A": team_a, "Team B": team_b}

randomised_teams = get_teams("Player Files/Player Stats.csv", "Player Files/Who is playing.csv")

sponsor_list = pd.read_csv("Simulator Files/sponsors.csv", header = None)[0]
sponsor = random.choice(sponsor_list)
footy_unc_list = pd.read_csv("Simulator Files/uncs.csv", header = None)["Name"]

st.title(f"Patented Mike Dixon 4most Draw Simulator - Brought to you by {sponsor}")
st.title(100*"-")
st.write("Hello World!")

st.set_page_config(layout="wide")

if st.button("Begin the festivities"):
    #we want to run all of our procedural dialogue and draw in here
    st.write("Button active")
    sleep(3)
    st.write("Delay test successful")
    with st.empty():
        st.write("this container is used for")
        sleep(3)
        st.write("overwriting text instead of simply printing downwards")
    pass