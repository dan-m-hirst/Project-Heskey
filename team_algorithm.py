
#Brute force algo for minimising difference in team ratings. May look to add optimisations
#across multiple metrics in a later release.
import pandas as pd
import itertools as it


def calc_avg_score(full_player_stats, player_stats, metric = "Avg Rating"):
    print(full_player_stats["Player"].isin(player_stats))
    return full_player_stats.loc[full_player_stats["Player"].isin(player_stats)][metric].mean()

def calc_team_sizes(player_stats):
    num_players = len(player_stats)
    team_a_size = num_players // 2
    team_b_size = num_players - team_a_size
    return {"Team A": team_a_size, "Team B": team_b_size}


def get_team_combos(full_player_stats, player_stats, size_dict, metric = "Avg Rating"):
    team_a_combo_list = []
    team_b_combo_list = []
    players = player_stats['Player'].tolist()
    team_a_size = size_dict['Team A']
    
    for team_a_combos in it.combinations(players, team_a_size):
        team_a_combo_list.append(team_a_combos)
        team_b_combo_list.append([player for player in players if player not in team_a_combos])
    
    team_a_scores = [calc_avg_score(full_player_stats, team, metric) for team in team_a_combo_list]
    team_b_scores = [calc_avg_score(full_player_stats, team, metric) for team in team_b_combo_list]
    score_diffs = [abs(a - b) for a, b in zip(team_a_scores, team_b_scores)]
    optimal_diff = min(score_diffs)
    optimal_teams_index = score_diffs.index(optimal_diff)

    optimal_teams = {"Team A": team_a_combo_list[optimal_teams_index],
                     "Team B": team_b_combo_list[optimal_teams_index],
                     "Team A Score": team_a_scores[optimal_teams_index],
                     "Team B Score": team_b_scores[optimal_teams_index]
                     }
    print(f"Fairest teams calculated. Average difference of {optimal_diff:.2f} in {metric}.")
    return optimal_teams

def print_team_combo_result(optimised_teams):
    team_a_score = optimised_teams['Team A Score']
    team_b_score = optimised_teams['Team B Score']
    unfairness_metric = abs(team_a_score - team_b_score)
    print("Team A:", optimised_teams['Team A'], f"Score: {team_a_score:.2f}")
    print("Team B:", optimised_teams['Team B'], f"Score: {team_b_score:.2f}")
    print(f"Unfairness score: {unfairness_metric:.2f}")


def generate_fairest_teams(full_player_stats, players_playing, metric = "Avg Rating"):
    active_player_stats = full_player_stats[full_player_stats['Player'].isin(players_playing)]
    team_sizes = calc_team_sizes(active_player_stats)
    team_combos = get_team_combos(full_player_stats, active_player_stats, team_sizes, metric)
    print_team_combo_result(team_combos)
    return team_combos