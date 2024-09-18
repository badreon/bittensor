import math
from normalization import normalize

def calculate_emissions(raw_emissions, min_emissions, max_emissions):
    return normalize(math.log(raw_emissions + 1), 
                     math.log(min_emissions + 1), 
                     math.log(max_emissions + 1))

def calculate_profitability(raw_profitability, min_profitability, max_profitability):
    return normalize(raw_profitability, min_profitability, max_profitability)

def calculate_flatness(std_dev_rewards, mean_rewards):
    return 1 - (std_dev_rewards / mean_rewards)

def calculate_stability(reward_volatility, max_observed_volatility):
    return 1 - (reward_volatility / max_observed_volatility)

def calculate_utility(utility_score, min_utility_score, max_utility_score):
    return normalize(utility_score, min_utility_score, max_utility_score)

def calculate_difficulty(difficulty_score, min_difficulty_score, max_difficulty_score):
    return normalize(difficulty_score, min_difficulty_score, max_difficulty_score)