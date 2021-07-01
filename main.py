from random import *

# Vars
trial_results_scen1 = []
trial_guesses_scen1 = []
trial_results_scen2 = []
trial_guesses_scen2 = []
scenario_1_results = []
scenario_2_results = []
number_of_trials = 1000000

# Main function
def main():
    # Scenario 1 (outsider)
    for i in range(0, number_of_trials):
        trial = randint(0, 1)
        
        if trial == 0:
            trial_results_scen1.append(0)
        else:
            intra_trial = randint(0, 1)

            if intra_trial == 0:
                trial_results_scen1.append(1)
            else:
                trial_results_scen1.append(2)


        guess = randint(0, 2)
        trial_guesses_scen1.append(guess)
    
    for i in range(0, (len(trial_results_scen1) - 1)):
        if trial_guesses_scen1[i] == trial_results_scen1[i]:
            scenario_1_results.append(trial_guesses_scen1[i])

    print("Scenario 1: " + str(round((len(scenario_1_results) / len(trial_results_scen1)), 2)))

    # Scenario 2 (insider)
    for i in range(0, number_of_trials):
        trial = randint(0, 1)

        if trial == 0:
            trial_results_scen2.append(0)
            trial_guesses_scen2.append(randint(0, 2))
        else:
            trial_results_scen2.append(1)
            trial_guesses_scen2.append(randint(0, 2))
            trial_results_scen2.append(2)
            trial_guesses_scen2.append(randint(0, 2))

    for i in range(0, (len(trial_results_scen2) - 1)):
        if trial_guesses_scen2[i] == trial_results_scen2[i]:
            scenario_2_results.append(trial_guesses_scen2[i])

    print("Scenario 2: " + str(round((len(scenario_2_results) / len(trial_results_scen2)), 2)))

if __name__ == '__main__':
    main()