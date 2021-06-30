import math

import numpy as np
import matplotlib.pyplot as plt


episodes = 1000

# Initial epsilon values for all strategies
eps_initial = 0.9

# Variables for Strategy 1
eps_final = 0.00000000001
eps_delta = (eps_initial - eps_final)/episodes

# Variables for Strategy 2
eps_decay_1 = 0.995

# Variables for Strategy 3
eps_tail = 0.3
eps_slope = 0.1
eps_stepness = 0.2

# Set graph values
fig, ax = plt.subplots(1, 1, tight_layout=True, figsize=(15, 5))
ax.set_title("Epsilon decay strategies", fontname="Times New Roman", fontsize=18, fontweight='bold')
ax.set_ylabel("Epsilon", fontsize=14)
ax.set_xlabel("Episode #", fontsize=14)
ax.minorticks_on()
ax.grid(which='major', linewidth='1', linestyle='-')
ax.grid(which='minor', linewidth='0.5', linestyle='--')
ax.set_ylim([0, 1])

eps_values_1 = []
eps_values_2 = []
eps_values_3 = []

# Strategy 1 - Linear decay
epsilon = eps_initial
for episode in range(episodes):
    eps_values_1.append(epsilon)
    epsilon -= eps_delta

# Strategy 2 - Exponential decay
epsilon = eps_initial
for episode in range(episodes):
    eps_values_2.append(epsilon)
    epsilon = epsilon * eps_decay_1

# Strategy 3 - Stretched Exponential Decay
epsilon = eps_initial
for episode in range(episodes):
    eps_values_3.append(epsilon)
    standardized_eps = (episode-eps_tail*episodes)/(eps_slope*episodes)
    cosh = np.cosh(math.exp(-standardized_eps))
    epsilon = 1.2-(1/cosh+(episode*eps_stepness/episodes))
    if epsilon > eps_initial:
        epsilon = eps_initial

plt.plot([i for i in range(len(eps_values_1))], eps_values_1,
         label="Strategy 1 - Linear decay", color='orange')
plt.plot([i for i in range(len(eps_values_2))], eps_values_2,
         label="Strategy 2 - Exponential decay", color='blue')
plt.plot([i for i in range(len(eps_values_3))], eps_values_3,
         label="Strategy 3 - Stretched exponential decay", color='red')

plt.legend(loc='best')
plt.show()
