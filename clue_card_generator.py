import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# gray, black, blue, red
palette = ["#d9d9d9", "#000000", "#08519c", "#cb181d"]

# decide if red or blue dominates
blue_or_red = np.random.choice([0,1])

# construct the list of colors to be used
# when blue dominates
if blue_or_red == 0:
    color_list = [0]*4 + [1] + [2]*8 + [3]*7
    
# when red dominates    
if blue_or_red == 1:
    color_list = [0]*4 + [1] + [2]*7 + [3]*8

# shuffle colors and arrange in a grid
np.random.shuffle(color_list)
color_array = np.array(color_list).reshape(5,4)

# plotting and styling
sns.heatmap(color_array,
            xticklabels=False, 
            yticklabels=False, 
            cmap=palette,
            cbar=False,
            square=True,
            linewidths=2,
            linecolor='k')

plt.title("TOP", fontsize=20);

plt.savefig("clue_card.png")