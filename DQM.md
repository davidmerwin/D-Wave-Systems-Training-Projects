
![](https://cdn.mathpix.com/snip/images/K2orjf1gNTzxbmUbb241FX2pSH9mtVLZ07fTjznA-3I.original.fullsize.png)

### Table of Contents

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Optimization Problem](#optimization-problem)
4. [DQM Model](#dqm-model)
5. [Results](#results)
6. [Setup and Installation](#setup-and-installation)
7. [Contributing](#contributing)


### Introduction

In this project, I've applied the power of D-Wave's quantum computing to solve a complex optimization problem. 
This serves both as a portfolio project and a detailed guide for students interested in venturing into the realm of quantum computing.

### Technologies Used

- Python 3.x
- D-Wave Ocean SDK
- NetworkX for graph manipulation

---

### Optimization Problem

#### Objective Function

![](https://cdn.mathpix.com/snip/images/4Odj34grmYbkKswHmc1rkHQUrrria5rbWIPnDK-KpHQ.original.fullsize.png)

I tackled the optimization problem characterized by the following objective function:

\[
\min \sum_{i \in V} x_i+\gamma \sum_{(i, j) \in E}\left(1-x_i-x_j+x_i \cdot x_j\right)
\]

**Mathematical Explanation:**

Here's a breakdown of the objective function:
- \(V\): Set of vertices
- \(E\): Set of edges
- \(x_i\): Binary variable associated with vertex \(i\)
- \( \gamma \): A constant scaling factor

---

### DQM Model

For this project, I've used D-Wave's Discrete Quadratic Model (DQM) to formulate and solve the optimization problem.

```python
# Initialize the DQM object
dqm = DiscreteQuadraticModel()
```

#### Code Explanation

- The Discrete Quadratic Model is initialized using D-Wave's Ocean SDK.
- Variables and their quadratic interactions are then added to the DQM object.

---

### Results

outcomes, results  data visualizations; quantum solutions' efficiency and accuracy.

---

### Setup and Installation

Here are the steps to get this project up and running on your local machine.

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# Install dependencies
pip install dwave-ocean-sdk

# Run the code
python your-main-script.py
```

