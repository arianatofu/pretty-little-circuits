# voltage_divider_lab.py
import numpy as np
import matplotlib.pyplot as plt

print("💖 Welcome to your Cute Voltage Divider Playground! 💖")

# ----- Inputs -----
V_in = float(input("Enter input voltage (V, e.g., 5): "))
R1 = float(input("Enter resistor R1 (Ω, e.g., 1000): "))
R2 = float(input("Enter resistor R2 (Ω, e.g., 2000): "))

# ----- Compute voltages -----
V_out = V_in * R2 / (R1 + R2)
I_total = V_in / (R1 + R2)

print(f"💖 Voltage at midpoint: {V_out:.3f} V")
print(f"💖 Total current: {I_total:.3f} A")

# ----- Prepare animation -----
t = np.linspace(0, 1, 50)
V_mid_wave = V_out * np.sin(np.pi * t)  # simple animated effect

plt.figure(figsize=(8,5))
plt.gca().set_facecolor('mistyrose')
plt.title("Voltage Divider Animation 💖", color='deeppink', fontsize=16)
plt.xlabel("Time (s)", color='deeppink')
plt.ylabel("Voltage (V)", color='deeppink')
plt.ylim(0, max(V_in, V_out)*1.2)

# ----- Animate hearts along voltage curve -----
for i in range(len(t)):
    plt.cla()
    plt.gca().set_facecolor('mistyrose')
    plt.title(f"Voltage at midpoint: {V_mid_wave[i]:.3f} V ", color='deeppink', fontsize=16)
    plt.xlabel("Time (s)", color='deeppink')
    plt.ylabel("Voltage (V)", color='deeppink')
    
    plt.plot(t[:i+1], V_mid_wave[:i+1], color='hotpink', linewidth=3)
    for j in range(i+1):
        plt.text(t[j], V_mid_wave[j], "♡", fontsize=12, ha='center', va='bottom', color='deeppink')
    
    plt.pause(0.05)

plt.show()