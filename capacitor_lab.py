# capacitor_lab.py
import numpy as np
import matplotlib.pyplot as plt

print("💖 Welcome to the Cute Capacitor Lab! 💖")

V_s = float(input("Enter supply voltage (V, e.g., 5): "))
R = float(input("Enter series resistance (Ω, e.g., 1000): "))
C = float(input("Enter capacitance (F, e.g., 0.001): "))
mode = input("Mode (charge/discharge): ").strip().lower()

t = np.linspace(0, 5*R*C, 100)  # simulate 5 time constants
if mode == "charge":
    V_c = V_s * (1 - np.exp(-t/(R*C)))
elif mode == "discharge":
    V_c = V_s * np.exp(-t/(R*C))
else:
    print("Unknown mode, defaulting to charge.")
    V_c = V_s * (1 - np.exp(-t/(R*C)))

plt.figure(figsize=(8,5))
plt.gca().set_facecolor('mistyrose')
plt.title(f"Capacitor {mode.capitalize()} ", color='deeppink', fontsize=16)
plt.xlabel("Time (s)", color='deeppink')
plt.ylabel("Voltage (V)", color='deeppink')
plt.ylim(0, V_s*1.2)

# Animate
for i in range(len(t)):
    plt.cla()
    plt.gca().set_facecolor('mistyrose')
    plt.title(f"Capacitor {mode.capitalize()} ", color='deeppink', fontsize=16)
    plt.xlabel("Time (s)", color='deeppink')
    plt.ylabel("Voltage (V)", color='deeppink')
    plt.plot(t[:i+1], V_c[:i+1], color='hotpink', linewidth=3)
    for j in range(i+1):
        plt.text(t[j], V_c[j], "♡", fontsize=12, ha='center', va='bottom', color='deeppink')
    plt.pause(0.05)

plt.show()