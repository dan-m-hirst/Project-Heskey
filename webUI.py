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

    a_score = fairest_teams["Team A Score"]
    b_score = fairest_teams["Team B Score"]
    return {"Team A": team_a, "Team B": team_b, "Team A Score" : a_score, "Team B Score" : b_score}

def get_team_df(teams_dict):
    team_a = list(teams_dict["Team A"])
    team_b = list(teams_dict["Team B"])

    if len(team_a) < len(team_b):
        team_a += ["Free spot"]*(len(team_b) - len(team_a))
    if len(team_a) > len(team_b):
        team_b += ["Free spot"]*(len(team_a) - len(team_b))
    
    eq_dict = {"Team A" : team_a, "Team B" : team_b}
    teams_table = pd.DataFrame.from_dict(eq_dict)
    
    return(teams_table)


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
cola, colb, colc = st.columns(3)
i=0
#Generate checkboxes in columns
for player in sorted(pd.read_csv("Player Files/Player Stats.csv")["Player"].tolist()):
    i += 1 
    if i <= 6:
        with cola:
            if st.checkbox(f"{player}"):
                active_players.append(player)
                no_players = len(active_players)
    elif i <= 12:
        with colb:
            if st.checkbox(f"{player}"):
                active_players.append(player)
                no_players = len(active_players)
    else:
        with colc:
            if st.checkbox(f"{player}"):
                active_players.append(player)
                no_players = len(active_players)

st.write(f"{no_players} players set to play.")


if st.button("Begin the festivities"):
    # Get fairest teams
    randomised_teams = get_teams("Player Files/Player Stats.csv", active_players)
    team_a_score = randomised_teams["Team A Score"]
    team_b_score = randomised_teams["Team B Score"]
    #we want to run all of our procedural dialogue and draw in here
    st.write("Button active")
    sleep(3)
    st.write("Delay test successful")
    teams_table = pd.DataFrame.from_dict(get_team_df(randomised_teams))
        
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Team A")
    with col2:
        st.subheader("Team B")

    sleep(3)
    
    for x in teams_table.iterrows():
        with col1:
            if x[1].iloc[0] != "Free spot": 
                #call get_intro(x[1][0])
                #call get_gif(x[1][0])
                st.write(x[1].iloc[0])
                sleep(3)
            print(x[1].iloc[0])
        with col2:
            if x[1].iloc[1] != "Free spot":
                #call get_intro(x[1][1])
                #call get_fig(x[1][1])
                st.write(x[1].iloc[1])
                sleep(3)
    
    st.write(f"Fairest teams generated. Team A score: {team_a_score:.2f}, Team B Score {team_b_score:.2f}.")
    st.write(f"Unfairness rating: {abs(team_a_score - team_b_score):.2f}.")

    # with st.empty():
    #     st.write("this container is used for")
    #     sleep(3)
    #     st.write("overwriting text instead of simply printing downwards")
    # pass