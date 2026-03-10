# RLC Circuit Analyzer

A simple Python project for analyzing a series RLC circuit.

This project calculates important circuit properties and simulates:
- Resonant frequency
- Damping condition
- Quality factor
- Step response
- Frequency response magnitude

## Features

- Compute resonant frequency
- Compute damping type (overdamped, critically damped, underdamped)
- Compute quality factor \(Q\)
- Plot frequency response
- Plot transient response

## Equations Used

For a series RLC circuit:

Resonant angular frequency:

\[
\omega_0 = \frac{1}{\sqrt{LC}}
\]

Resonant frequency:

\[
f_0 = \frac{1}{2\pi\sqrt{LC}}
\]

Quality factor:

\[
Q = \frac{1}{R}\sqrt{\frac{L}{C}}
\]

Damping coefficient:

\[
\alpha = \frac{R}{2L}
\]

## Example Values

- \(R = 10\ \Omega\)
- \(L = 0.1\ \text{H}\)
- \(C = 100 \times 10^{-6}\ \text{F}\)

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
