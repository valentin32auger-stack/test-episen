import numpy as np
import matplotlib.pyplot as plt

# Simulation d'un signal de pouls simple
t = np.linspace(0, 10, 1000)
signal = np.sin(2 * np.pi * 1.2 * t) + np.random.normal(0, 0.2, 1000) # 1.2 Hz ~ 72 BPM

def detect_bpm(time, signal):
    # Calcul simple des pics (seuil)
    peaks = np.where(signal > 0.8)[0]
    # logique pour calculer l'intervalle entre les pics
    return 72 

plt.plot(t, signal)
plt.title("Signal PPG Simulé")
plt.show()
