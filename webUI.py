import streamlit as st
from time import sleep
import random
import pandas as pd
from team_algorithm import generate_fairest_teams
#need to run in terminal "streamlit run webUI.py"
#How/when do I put in the unfairness score?

def get_teams(all_player_stats_path, players_playing):
    full_stats = pd.read_csv(all_player_stats_path)
    active_players = players_playing

    fairest_teams = generate_fairest_teams(full_stats, active_players)

    team_a = list(fairest_teams["Team A"])
    random.shuffle(team_a)
    team_b = list(fairest_teams["Team B"])
    random.shuffle(team_b)
    return {"Team A": team_a, "Team B": team_b}

def get_sponsor():
    if "sponsor" not in st.session_state:
        sponsor_list = pd.read_csv("Simulator Files/sponsors.csv", header = None)[0]
        sponsor = random.choice(sponsor_list)
        return(sponsor)
    return(st.session_state["sponsor"])

while False:
    #have basically dummied this as don't want to focus on procedural dialogue
    #before draw table is done
    footy_unc_list = pd.read_csv("Simulator Files/uncs.csv", header = None)["Name"]


#######BEGIN WEBPAGE######
sponsor = get_sponsor()
st.session_state["sponsor"] = sponsor
st.title(f"Patented Mike Dixon 4most Draw Simulator - Brought to you by {sponsor}")
st.title(100*"-")
st.write("Hello World!")

st.set_page_config(layout="wide")

active_players = []
no_players = len(active_players)
for player in sorted(pd.read_csv("Player Files/Player Stats.csv")["Player"].tolist()):
    if st.checkbox(f"{player}"):
        active_players.append(player)
        no_players = len(active_players)

st.write(f"{no_players} players set to play.")


if st.button("Begin the festivities"):
    # Get fairest teams
    randomised_teams = get_teams("Player Files/Player Stats.csv", active_players)
    #we want to run all of our procedural dialogue and draw in here
    st.write("Button active")
    sleep(3)
    st.write("Delay test successful")
    with st.empty():
        st.write("this container is used for")
        sleep(3)
        st.write("overwriting text instead of simply printing downwards")
    pass