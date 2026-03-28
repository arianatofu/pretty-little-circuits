import matplotlib.pyplot as plt
import numpy as np
import time as tm

# ----- Inputs -----
print("💖 Welcome to your Cute Interactive Electronics Lab! 💖")
voltage_type = input("Choose voltage type (constant/ramp/AC): ").strip().lower()
voltage_value = float(input("Enter voltage value (V, e.g., 3.3): "))
resistance = float(input("Enter resistance (Ω, e.g., 1000): "))

# ----- Prepare time -----
t = np.linspace(0, 1, 100)  # 1 second
current_wave = np.zeros_like(t)

# ----- Compute current based on voltage type -----
if voltage_type == "constant":
    current_wave = np.ones_like(t) * (voltage_value / resistance)
elif voltage_type == "ramp":
    voltage_wave = np.linspace(0, voltage_value, len(t))
    current_wave = voltage_wave / resistance
elif voltage_type == "ac":
    voltage_wave = voltage_value * np.sin(2 * np.pi * 5 * t)  # 5 Hz AC
    current_wave = voltage_wave / resistance
else:
    print("Unknown voltage type. Defaulting to constant.")
    current_wave = np.ones_like(t) * (voltage_value / resistance)

# ----- Set up plot -----
plt.figure(figsize=(8,5))
plt.gca().set_facecolor('mistyrose')  # cute pink background
plt.title("Current Through Resistor ", color='deeppink', fontsize=16)
plt.xlabel("Time (s)", color='deeppink')
plt.ylabel("Current (A)", color='deeppink')
plt.ylim(0, max(current_wave)*1.2 + 0.1)

# ----- Animate hearts -----
for i in range(len(t)):
    plt.cla()  # clear axes
    plt.gca().set_facecolor('mistyrose')
    plt.title(f"Current: {current_wave[i]:.3f} A ", color='deeppink', fontsize=16)
    plt.xlabel("Time (s)", color='deeppink')
    plt.ylabel("Current (A)", color='deeppink')
    plt.plot(t[:i+1], current_wave[:i+1], color='hotpink', linewidth=3)
    
    # draw hearts at each point
    for j in range(i+1):
        plt.text(t[j], current_wave[j], ".", fontsize=12, ha='center', va='bottom')
    
    plt.pause(0.05)  # pause for animation effect

plt.show()