import streamlit as st
from time import sleep
import random
import pandas as pd
from team_algorithm import generate_fairest_teams
#need to run in terminal "streamlit run webUI.py"
#How/when do I put in the unfairness score?
col_width = 600

def get_teams(all_player_stats_path, players_playing, metric):
    full_stats = pd.read_csv(all_player_stats_path)
    active_players = players_playing

    fairest_teams = generate_fairest_teams(full_stats, active_players, metric)

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

    #Need to pad lists or else from_dict will fail
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

def get_uncs():
    footy_unc_list = pd.read_csv("Simulator Files/uncs.csv").sample(2).reindex()
    footy_unc_list = footy_unc_list
    footy_unc1 = footy_unc_list.iloc[0].to_dict()
    if footy_unc1["Surname"] == None: footy_unc1["Surname"] = footy_unc1["First Name"]
    footy_unc2 = footy_unc_list.iloc[1].to_dict()
    if footy_unc2["Surname"] == None: footy_unc1["Surname"] = footy_unc2["First Name"]
    return[footy_unc1, footy_unc2]




#######BEGIN WEBPAGE######
sponsor = get_sponsor()
st.session_state["sponsor"] = sponsor
st.set_page_config(layout="wide")
st.title(f"Patented Mike Dixon 4most Draw Simulator - Brought to you by {sponsor}")
st.divider()
st.subheader("Player and fairness metric select")
st.write()
metric_choices = list(pd.read_csv("Player Files/Player Stats.csv").columns.values)
metric_choices.remove("Player")
fair_metric = st.selectbox("Select your fairness metric:", metric_choices, width = col_width)

active_players = []
no_players = len(active_players)
cola, colb, colc = st.columns(3, width = col_width)
i=0

st.write("Select the participating players:")
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
    # Get fairest teams in shuffled form.
    randomised_teams = get_teams("Player Files/Player Stats.csv", active_players, fair_metric)
    team_a_score = randomised_teams["Team A Score"]
    team_b_score = randomised_teams["Team B Score"]
    teams_table = pd.DataFrame.from_dict(get_team_df(randomised_teams))

    uncs = get_uncs()
    unc1 = uncs[0]
    unc2 = uncs[1]

    #we want to run all of our procedural dialogue and draw in here
    st.subheader("Draw HQ")
    draw_dialogue = st.empty()
    st.divider()

    with draw_dialogue.container():
        st.write(
            f"""Welcome to this Leeds Office 5s draw everyone, 
            and please put your hands together for our guest {unc1["Name"]}!"""
            )
        sleep(3)
        st.write(f"How are things, Mr. {unc1['Surname']}?")
        sleep(2)
        st.write('"All good thanks, Mike. Let\'s get on with it shall we?"')

    #These cols are where the final team list will go
    col1, col2 = st.columns(2, width = col_width)
    with col1:
        st.subheader("Team A")
    with col2:
        st.subheader("Team B")

    sleep(3)
    
    for x in teams_table.iterrows():
        team_a_draw = x[1].iloc[0]
        team_b_draw = x[1].iloc[1]
        with col1:
            if team_a_draw != "Free spot":
                with draw_dialogue.container(): 
                    #call get_intro(team_a_draw) #st.image() for gif
                    #call get_gif(team_a_draw)
                    st.write(f"{team_a_draw} joins Team A")
                st.write(team_a_draw)
                sleep(3)
        with col2:
            if team_b_draw != "Free spot":
                with draw_dialogue.container():
                    #call get_intro(team_b_draw)
                    #call get_gif(team_b_draw)
                    st.write(f"{team_b_draw} joins Team B")
                st.write(team_b_draw)
                sleep(3)

    st.write(f"Fairest teams generated. Team A score: {team_a_score:.2f}, Team B Score {team_b_score:.2f}.")
    st.write(f"Unfairness rating: {abs(team_a_score - team_b_score):.2f}.")

    # with st.empty():
    #     st.write("this container is used for")
    #     sleep(3)
    #     st.write("overwriting text instead of simply printing downwards")
    # pass