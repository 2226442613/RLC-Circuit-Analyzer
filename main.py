import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os


def resonant_frequency(L: float, C: float) -> float:
    """Return resonant frequency in Hz."""
    return 1 / (2 * np.pi * np.sqrt(L * C))


def quality_factor(R: float, L: float, C: float) -> float:
    """Return quality factor Q for a series RLC circuit."""
    return (1 / R) * np.sqrt(L / C)


def damping_coefficient(R: float, L: float) -> float:
    """Return damping coefficient alpha."""
    return R / (2 * L)


def natural_angular_frequency(L: float, C: float) -> float:
    """Return natural angular frequency omega_0."""
    return 1 / np.sqrt(L * C)


def damping_type(R: float, L: float, C: float) -> str:
    """Classify the circuit damping behavior."""
    alpha = damping_coefficient(R, L)
    omega_0 = natural_angular_frequency(L, C)

    if np.isclose(alpha, omega_0):
        return "Critically damped"
    elif alpha < omega_0:
        return "Underdamped"
    else:
        return "Overdamped"


def transfer_function_series_rlc(R: float, L: float, C: float):
    """
    Return transfer function for output across capacitor:
        H(s) = 1 / (LC s^2 + RC s + 1)
    """
    numerator = [1]
    denominator = [L * C, R * C, 1]
    return signal.TransferFunction(numerator, denominator)


def plot_frequency_response(system, output_dir="plots"):
    """Plot magnitude response."""
    os.makedirs(output_dir, exist_ok=True)

    w = np.logspace(1, 5, 1000)  # rad/s
    w, mag, phase = signal.bode(system, w=w)

    plt.figure(figsize=(8, 5))
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency (rad/s)")
    plt.ylabel("Magnitude (dB)")
    plt.title("Frequency Response")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "frequency_response.png"))
    plt.show()


def plot_step_response(system, output_dir="plots"):
    """Plot step response."""
    os.makedirs(output_dir, exist_ok=True)

    t, y = signal.step(system)

    plt.figure(figsize=(8, 5))
    plt.plot(t, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Response")
    plt.title("Step Response")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "step_response.png"))
    plt.show()


def main():
    # Example component values
    R = 10.0          # ohms
    L = 0.1           # henries
    C = 100e-6        # farads

    f0 = resonant_frequency(L, C)
    Q = quality_factor(R, L, C)
    alpha = damping_coefficient(R, L)
    dtype = damping_type(R, L, C)

    print("=== Series RLC Circuit Analysis ===")
    print(f"R = {R} ohms")
    print(f"L = {L} H")
    print(f"C = {C} F")
    print(f"Resonant frequency: {f0:.2f} Hz")
    print(f"Quality factor Q: {Q:.3f}")
    print(f"Damping coefficient alpha: {alpha:.3f}")
    print(f"Damping type: {dtype}")

    system = transfer_function_series_rlc(R, L, C)
    plot_frequency_response(system)
    plot_step_response(system)


if __name__ == "__main__":
    main()
