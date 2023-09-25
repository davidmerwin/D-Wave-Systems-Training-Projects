# Mind Map: Quantum Lagrangian Simulation

## Mathematical Expression

- **Classical Lagrangian**
  - Captures the dynamics of the system.
  - Involves an electromagnetic wave and qubits.

## Python3 Script

- **Simulation of Lagrangian System**
  - Solves a simplified version of the Lagrangian system using Python.
  - Simulates the evolution of $$\Phi_n$$ over time.

### Constants

- $$c$$ (Speed of light)
- $$L$$ (Inductance)
- $$n_{\text{points}}$$ (Number of qubits)

### State Initialization

- $$\Phi_n$$, $$\dot{\Phi}_n$$, $$\Psi_n$$, $$\dot{\Psi}_n$$

### Time Evolution Parameters

- $$dt$$ (Time step)
- $$time_{\text{steps}}$$ (Number of time steps)

### Lagrangian Terms Computation

- Kinetic term: $$\left(\frac{{\dot{\Phi}_n}}{{2c}}\right)^2$$
- Potential term: $$\frac{{(\Phi_n - \Phi_{n-1} - \tilde{\Psi}_n)^2}}{{2L}}$$

### Update of $$\Phi$$ and $$\Psi$$ based on Dynamics

- Update $$\dot{\Phi}_n$$ by adding random noise
- Update $$\Phi_n$$ and $$\Psi_n$$ based on their derivatives

### Storage of History for Plotting

- Store the values of $$\Phi_n$$ at each time step

### Plotting

- Plot the evolution of $$\Phi_n$$ over time

# Mind Map: Why Quantum Engineering?

## Abstract

- Progress in experimental and theoretical fields.
- Quantum coherent solid-state qubits as building blocks.
- Explores quantum-classical boundary.

## Introduction

- Distinct from nanotechnology and quantum computing.
- Addresses the quantum effects in engineering.

## Background

- **Miniaturization and Nanotechnology**
  - Momentum behind nanotechnology from miniaturization.
  - Quantum effects important in mesoscopic physics.

- **Quantum Computing**
  - Algorithms like Shor's and Grover's.
  - DiVincenzo criteria for scalable quantum computer.

## Physical Aspects

- **Criteria for Quantum Computer**
  - Initialize qubit states.
  - Long decoherence times.
  - Universal quantum gates.
  - Qubit-specific measurements.

- **Solid-State Devices**
  - Superconducting devices and quantum dots.
  - Decoherence times and scalability.

## Recent Developments

- **Macroscopic Schrödinger Cat States**
  - Testing the limits of quantum mechanics.

- **Quantum Engineering as a Branch**
  - Large systems of interacting qubits.
  - Quantum coherence in large systems
