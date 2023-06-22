import matplotlib.pyplot as plt
import numpy as np

# Generate data for x-axis
x = np.linspace(1, 10, 100)  # Adjust the range and number of points as needed

# Generate data for y-axis (logarithmic values)
y = np.log10(x)  # Change the base or function as desired (e.g., np.log(), np.log2())

# Create the line graph
plt.plot(x, y, '-', label='this Function')  # Add label to the plot

# Add a legend
plt.legend()

plt.xlabel('X')
plt.ylabel('Logarithmic Y')
plt.title('Logarithmic Function')
plt.grid(True)

# Display the graph
plt.tight_layout()
plt.show()