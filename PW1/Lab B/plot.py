"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""
import numpy as np
import matplotlib.pyplot as plt

t , observed = np.loadtxt("decay_observed.csv", delimiter=",",skiprows=1, unpack=True)

NO = observed[0]
LAMBDA = 0.3
analytical = NO * np.exp(-LAMBDA * t)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4),sharex=True, sharey=True)

ax1.scatter(t, observed, color="blue", label="observed")
ax1.set_title("Observed decay data")
ax1.set_xlabel("time")
ax1.set_ylabel("atom count")

ax2.plot(t, analytical, color="red", label="analytical")
ax2.set_title("Analytical decay law")
ax2.set_xlabel("time")

plt.tight_layout()

plt.savefig("figure.png")