
#Brute force algo for minimising difference in team ratings. May look to add optimisations
#across multiple metrics in a later release.
import pandas as pd
import itertools as it

all_player_stats = pd.read_csv('Player Files/Player Stats.csv')

whos_playing = ['Mike',
                'James K',
                'Jamie',
                'Jacob',
                'Toby',
                'Olly',
                'Dan H',
                'Steven',
                'Callum',
                'Rory',
                'Mark'
                ]

player_stats = all_player_stats[all_player_stats['Player'].isin(whos_playing)]

def calc_avg_score(player_list, metric="Avg Rating"):
    return all_player_stats[all_player_stats['Player'].isin(player_list)][metric].mean()

def calc_team_sizes(player_stats):
    num_players = len(player_stats)
    team_a_size = num_players // 2
    team_b_size = num_players - team_a_size
    return {"Team A": team_a_size, "Team B": team_b_size}


def get_team_combos(player_stats, size_dict, metric = "Avg Rating"):
    team_a_combo_list = []
    team_b_combo_list = []
    players = player_stats['Player'].tolist()
    team_a_size = size_dict['Team A']
    team_b_size = size_dict['Team B']
    
    for team_a_combos in list(it.combinations(players, team_a_size)):
        team_a_combo_list.append(team_a_combos)
        team_b_combo_list.append([player for player in players if player not in team_a_combos])
    
    team_a_scores = [calc_avg_score(team, metric) for team in team_a_combo_list]
    team_b_scores = [calc_avg_score(team, metric) for team in team_b_combo_list]
    score_diffs = [abs(a - b) for a, b in zip(team_a_scores, team_b_scores)]
    optimal_diff = min(score_diffs)
    optimal_teams_index = score_diffs.index(optimal_diff)

    optimal_teams = {"Team A": team_a_combo_list[optimal_teams_index],
                     "Team B": team_b_combo_list[optimal_teams_index],
                     "Team A Score": team_a_scores[optimal_teams_index],
                     "Team B Score": team_b_scores[optimal_teams_index]
                     }
    print(f"Fairest teams caclulated. Average difference of {optimal_diff:.2f} in {metric}.")
    return optimal_teams

size_dict = calc_team_sizes(player_stats)

optimal_teams = get_team_combos(player_stats, size_dict, metric="Avg Rating")
print("Team A:", optimal_teams['Team A'], f"Score: {optimal_teams['Team A Score']:.2f}")
print("Team B:", optimal_teams['Team B'], f"Score: {optimal_teams['Team B Score']:.2f}")