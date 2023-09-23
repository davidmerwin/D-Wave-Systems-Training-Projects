![](https://cdn.mathpix.com/snip/images/SG6NfcWUoxpdpro9d8MUu0ah1dvk0_u9WREp6I3OQzE.original.fullsize.png)

## D-Wave Systems Quantum Computing Training Project

### Workforce Optimization Using Discrete Quadratic Models (DQM)

![D-Wave Quantum Computer](https://github.com/your-username/your-repo-name/raw/main/images/dwave_quantum_computer.jpg)

---

### Table of Contents

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Objective](#objective)
4. [DQM Implementation](#dqm-implementation)
5. [Setup & Installation](#setup--installation)
6. [Results](#results)

---

### Introduction

This repository is a showcase of a project focused on optimizing workforce distribution using Discrete Quadratic Models (DQM) via D-Wave Systems Quantum Computing.

---

### Technologies Used

- Python 3.x
- D-Wave Ocean SDK

---

### Objective

The primary aim of this project is to utilize D-Wave's Discrete Quadratic Models for workforce optimization, which involves the efficient allocation of employees to different shifts.

---

### DQM Implementation

The crux of the project revolves around the implementation of D-Wave's Discrete Quadratic Model (DQM).

```python
from dimod import DiscreteQuadraticModel

# Initialize the DQM object
dqm = DiscreteQuadraticModel()
```

#### Adding Variables for Employees

To build the DQM, we start by adding variables for each employee's name. 

```python
# Add variables to DQM for each employee
for name in employees:
    dqm.add_variable(num_shifts, label=name)
```

**Explanation**: Here `dqm.add_variable(num_shifts, label=name)` adds a variable representing each employee to the DQM. 
The variable has as many possible values as there are shifts (`num_shifts`), and it's labeled with the employee's name for identification.

---

### Setup & Installation

To get started, clone this repository and install the D-Wave Ocean SDK.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install dwave-ocean-sdk
```

Then, run the main Python script:

```bash
python main.py
```

---

### Results

results, efficiency, and visualizations

--- 
