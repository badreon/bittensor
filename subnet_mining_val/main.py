from calculator import calculate_sms

def run_test_cases():
    test_cases = [
        {
            "name": "Baseline Case",
            "params": {
                "raw_emissions": 1000000,
                "raw_profitability": 0.05,
                "std_dev_rewards": 100,
                "mean_rewards": 1000,
                "reward_volatility": 0.1,
                "utility_score": 8,
                "difficulty_score": 6,
                "min_emissions": 100000,
                "max_emissions": 10000000,
                "min_profitability": 0.01,
                "max_profitability": 0.1,
                "max_observed_volatility": 0.5,
                "min_utility_score": 1,
                "max_utility_score": 10,
                "min_difficulty_score": 1,
                "max_difficulty_score": 10,
                "w_e": 1.2, "w_m": 1.5, "w_f": 0.8, "w_r": 1.0, "w_u": 1.3, "w_d": 0.7
            }
        },
        {
            "name": "High Emissions Case",
            "params": {
                "raw_emissions": 9000000,
                "raw_profitability": 0.05,
                "std_dev_rewards": 100,
                "mean_rewards": 1000,
                "reward_volatility": 0.1,
                "utility_score": 8,
                "difficulty_score": 6,
                "min_emissions": 100000,
                "max_emissions": 10000000,
                "min_profitability": 0.01,
                "max_profitability": 0.1,
                "max_observed_volatility": 0.5,
                "min_utility_score": 1,
                "max_utility_score": 10,
                "min_difficulty_score": 1,
                "max_difficulty_score": 10,
                "w_e": 1.2, "w_m": 1.5, "w_f": 0.8, "w_r": 1.0, "w_u": 1.3, "w_d": 0.7
            }
        },
        {
            "name": "Low Profitability Case",
            "params": {
                "raw_emissions": 1000000,
                "raw_profitability": 0.02,
                "std_dev_rewards": 100,
                "mean_rewards": 1000,
                "reward_volatility": 0.1,
                "utility_score": 8,
                "difficulty_score": 6,
                "min_emissions": 100000,
                "max_emissions": 10000000,
                "min_profitability": 0.01,
                "max_profitability": 0.1,
                "max_observed_volatility": 0.5,
                "min_utility_score": 1,
                "max_utility_score": 10,
                "min_difficulty_score": 1,
                "max_difficulty_score": 10,
                "w_e": 1.2, "w_m": 1.5, "w_f": 0.8, "w_r": 1.0, "w_u": 1.3, "w_d": 0.7
            }
        }
    ]

    for case in test_cases:
        sms = calculate_sms(**case["params"])
        print(f"{case['name']} - Subnet Mining Score: {sms:.4f}")

if __name__ == "__main__":
    run_test_cases()
    