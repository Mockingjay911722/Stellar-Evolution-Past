import matplotlib.pyplot as plt
import numpy as np


def mass_evolution_of_gas_1(G, S, steps, current_step=0, G_values=None, S_values = None):
    # Initialize the array if it's not provided
    if G_values is None:
        G_values = [0] * steps
    if S_values is None:
        S_values = [0] * steps

    # Store the current value of G in the array
    G_values[current_step] = G
    S_values[current_step] = S

    # Base case: if we've reached the desired number of steps, return the array and final G and S
    if current_step == steps - 1:
        return G_values, S_values, G, S

    # Update G and S by 1% of the current G
    G_new = G * (1 - 0.01)
    S_new = S + (G * 0.01)

    # Recursively call the function for the next step
    return mass_evolution_of_gas_1(G_new, S_new, steps, current_step + 1, G_values, S_values)

# Example usage:
steps = 1000
G_values, S_values, final_G, final_S = mass_evolution_of_gas_1(1, 0, steps)
print(G_values)
print(S_values)

# PLOT OF G(T), G(S) AND S(T)
t_1d = np.arange(1000)
plt.plot(t_1d, G_values, linewidth=4, color='#0077be',label = r'Gas')
plt.title(r'G(t)')
plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Gas')
plt.legend()
plt.show()

plt.plot(t_1d, S_values,linewidth = 4, label = r'S_total')
plt.title(r'S(t)')
plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Total Stars')
plt.legend()
plt.show()
