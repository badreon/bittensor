import math
from components import *
from components import calculate_emissions

def calculate_sms(raw_emissions, raw_profitability, std_dev_rewards, mean_rewards,
                  reward_volatility, utility_score, difficulty_score,
                  min_emissions, max_emissions, min_profitability, max_profitability,
                  max_observed_volatility, min_utility_score, max_utility_score,
                  min_difficulty_score, max_difficulty_score,
                  w_e=1, w_m=1, w_f=1, w_r=1, w_u=1, w_d=1):
    
    E = calculate_emissions(raw_emissions, min_emissions, max_emissions)
    M = calculate_profitability(raw_profitability, min_profitability, max_profitability)
    F = calculate_flatness(std_dev_rewards, mean_rewards)
    R = calculate_stability(reward_volatility, max_observed_volatility)
    U = calculate_utility(utility_score, min_utility_score, max_utility_score)
    D = calculate_difficulty(difficulty_score, min_difficulty_score, max_difficulty_score)
    
    numerator = (w_e * math.log(E + 1) + 
                 w_m * M + 
                 w_f * F + 
                 w_r * R + 
                 w_u * U)
    denominator = w_d * D
    
    return numerator / denominator if denominator != 0 else float('inf')