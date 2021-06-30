import matplotlib.pyplot as plt


def calculateEpsilon(episodes, eps_initial, eps_decay):
    epsilon = eps_initial
    eps_values = []
    for episode in range(episodes):
        eps_values.append(epsilon)
        epsilon = epsilon * eps_decay
    return eps_values


# Initial epsilon values for all
eps_initial = 0.9

# Episodes
episodes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Variables for Strategy 2
eps_decay = [0.55, 0.75, 0.91, 0.945, 0.968, 0.988, 0.994, 0.997, 0.9987]


# Set graph values
fig, axs = plt.subplots(2, tight_layout=True, figsize=(15, 10))
axs[0].set_title("Epsilon decay values", fontname="Times New Roman", fontsize=18, fontweight='bold')
axs[1].set_xlabel("Episode #", fontsize=14)

for i in range(2):
    axs[i].set_ylabel("Epsilon", fontsize=14)
    axs[i].minorticks_on()
    axs[i].grid(which='major', linewidth='1', linestyle='-')
    axs[i].grid(which='minor', linewidth='0.5', linestyle='--')
    axs[i].set_ylim([0, 1])

colours = ['darksalmon', 'tan', 'gold', 'olivedrab', 'plum', 'darkcyan', 'powderblue', 'orange', 'steelblue']


# Calculates epsilon values
eps_values = []
for i in range(len(episodes)):
    strategy_values = calculateEpsilon(episodes[i], eps_initial, eps_decay[i])
    eps_values.append(strategy_values)

# Plot graphs
for iter in range (len(episodes)):
    if iter < 5:
        axs[0].plot([i for i in range(len(eps_values[iter]))], eps_values[iter], label=f"{episodes[iter]} \
                    Episodes - Decay value: {eps_decay[iter]}", color=colours[iter])
    else:
        axs[1].plot([i for i in range(len(eps_values[iter]))], eps_values[iter], label=f"{episodes[iter]} \
                    Episodes - Decay value: {eps_decay[iter]}", color=colours[iter])

axs[0].legend(loc='best')
axs[1].legend(loc='best')
plt.show()
