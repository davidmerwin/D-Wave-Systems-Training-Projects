# D-Wave-Systems-Training-Projects
Python Prep:
https://gist.github.com/e4758b0bd36796313bfc3f9bab50da46

![](https://cdn.mathpix.com/snip/images/e_bLeOWvSjGIO5CGBpNa-uOaRW5OnFBllhHDLlI69I4.original.fullsize.png)

Table of Contents
1. Overview
2. Getting Started
3. D-Wave Tools and Technologies
4. Project Summaries
- Older Projects
- Newer Projects
5. Contact Information
  
## Project Directory Structure:
    (BELIEF SPACE)
    ├── README.md
    ├── code
    │   └── number_partitioning.py
    ├── data
    │   └── training_number_partitioning.json
    ├── math_equations
    │   └── equations.md  ──────                                                                                                
    ├── results                                                                                   
    │   └── sampling_time_analysis.md
    └──├── quantum_tsp
    │   └── code
    │       └── quantum_tsp.py
    │   └── data
    │       └── cities.json
    │   └── math_equations
    │       └── tsp_equations.md
    │   └── results
    │       └── tsp_results.md
    ├── project_cd24acdf-0a8f-44ae-a150-69ece39acec6
    │   ├── code
    │   ├── data
    │   └── ...
    └── project_6dbabf04-9a93-4534-9239-51d9edc7cbe2
        ├── code
        ├── data
        └── ...

![](https://cdn.mathpix.com/snip/images/9a7KdTcBxZ4VH9leLZyP0guTPtYCtTUzYrNCEvBFUfk.original.fullsize.png)

    # Quantum Computing 101 with D-Wave Systems

## Overview

This README outlines my journey through a 5-day Quantum Computing 101 lecture series and hands-on training project sessions with D-Wave Systems. In this document, you'll discover my experience working with D-Wave's tools such as D-Wave Inspector and the various types of problems I tackled.

## Getting Started

To get started with D-Wave Systems, you will need to:

1. **Install D-Wave Ocean SDK**: This software stack includes everything you need to build a D-Wave application.

    ```bash
    pip install dwave-ocean-sdk
    ```
    
2. **Sign Up on D-Wave Leap**: D-Wave's cloud service for quantum computing.

    [D-Wave Leap Signup](https://cloud.dwavesys.com/leap/)

## D-Wave Tools and Technologies

- **D-Wave Ocean SDK**: Primarily used for problem formulation.
- **D-Wave IDE**: Used for easier problem modeling and solving.
- **Qbsolv**: For solving QUBO and Ising problems.
- **D-Wave Hybrid**: For hybrid classical/quantum algorithms.


## D-Wave Inspector Repository

- **Repository**: [dwavesystems/dwave-inspector](https://github.com/dwavesystems/dwave-inspector)
- **Language**: 100% Python
- **License**: Apache-2.0 & D-Wave EULA
- **Installation**: 
  ```bash
  pip install dwave-inspector
  pip install dwave-inspectorapp --extra-index=https://pypi.dwavesys.com/simple
  ```
- **Description**: D-Wave Inspector is a tool for visualizing problems submitted to, and answers received from, a D-Wave structured solver such as an Advantage™ quantum computer.


## Projects and Studies during the Training:
.
├── project_cd24acdf-0a8f-44ae-a150-69ece39acec6
│   ├── code
│   ├── data
│   └── ...
└── project_6dbabf04-9a93-4534-9239-51d9edc7cbe2
    ├── code
    ├── data
    └── ...


### Project ID: cd24acdf-0a8f-44ae-a150-69ece39acec6

- **Training**: Number Partitioning
- **Solver**: Advantage_system 4.1
- **Type**: QUBO
- **Status**: Completed
- **Submitted On**: 2023-05-18T22:56:57.426472Z
- **Solved On**: 2023-05-18T22:56:57.597874Z
- **Number of Reads**: 100
- **Submitted By**: Zi2q-7cdd45d9...

### Problem and Solution

I utilized the D-Wave Inspector to minor-embed a binary quadratic model onto a Quantum Processing Unit (QPU) for solving a number partitioning problem.

```math
Problem ID: cd24acdf-0a8f-44ae-a150-69ece39acec6
Solver: Advantage_system 4.1
Type: QUBO
Status: Completed
Submitted On: 2023-05-18T22:56:57.426472Z
Solved On: 2023-05-18T22:56:57.597874Z
Number of Reads: 100
```

#### QPU Sampling and Timing Information

- **QPU_SAMPLING_TIME**: \(10.728 \mathrm{~ms}\)
- **QPU_ANNEAL_TIME_PER_SAMPLE**: \(20 \mu \mathrm{s}\)
- **QPU_READOUT_TIME_PER_SAMPLE**: \(67 \mu \mathrm{s}\)
- **QPU_ACCESS_TIME**: \(26.484 \mathrm{~ms}\)
- **QPU_ACCESS_OVERHEAD_TIME**: \(580 \mu \mathrm{s}\)
- **QPU_PROGRAMMING_TIME**: \(15.756 \mathrm{~ms}\)
- **QPU_DELAY_TIME_PER_SAMPLE**: \(21 \mu \mathrm{s}\)
- **TOTAL_POST_PROCESSING_TIME**: \(1.895 \mathrm{~ms}\)
- **POST_PROCESSING_OVERHEAD_TIME**: \(1.895 \mathrm{~ms}\)

_______________________________________________________________


## Training Project: Number Partitioning

- ID: 23cf353c-5596-4e2e-ab04-dc8372daa7a2
- Type: qubo
- Solver: Advantage_system4.1
- Submitted On: 2023-05-18T23:09:22.949935Z
- Solved On: 2023-05-18T23:09:23.166683Z
- Status: COMPLETED
- Submitted By: Zi2q-7cdd45d9...
- Number of Reads: 100

Plan of Action For Problem

The training project focuses on Number Partitioning. The objective is to partition a set of numbers into two equal subsets such that the sum of the numbers in each subset is as close as possible. This problem is represented as a QUBO optimization problem.

### Energy and Sample Data

|     | 1507  | 1522  | 1537  | 1552  | ...   | 4403  | energy   | num_oc. |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | -------- | ------- |
| 0   | 0     | 0     | 0     | 0     | ...   | 1     | -9826.5  | 35      |
| 1   | 1     | 1     | 1     | 1     | ...   | 0     | -9826.5  | 21      |
| 2   | 1     | 0     | 1     | 1     | ...   | 0     | -9816.5  | 24      |
| 3   | 0     | 1     | 0     | 0     | ...   | 1     | -9816.5  | 15      |
| 4   | 1     | 1     | 1     | 1     | ...   | 0     | -9298.5  | 1       |
| 5   | 1     | 0     | 0     | 0     | ...   | 1     | -9276.5  | 1       |
| 6   | 0     | 1     | 1     | 1     | ...   | 0     | -9276.5  | 1       |
| 7   | 0     | 0     | 1     | 1     | ...   | 0     | -9179.0  | 1       |
| 8   | 1     | 0     | 1     | 1     | ...   | 0     | -7332.0  | 1       |
| ... | ...   | ...   | ...   | ...   | ...   | ...   | ...      | ...     |

### Timing Information

- QPU Sampling Time: 10.008 ms
- QPU Anneal Time per Sample: 20 µs
- QPU Readout Time per Sample: 60 µs
- QPU Access Time: 25.764 ms
- QPU Access Overhead Time: 3.494 ms
- QPU Programming Time: 15.756 ms
- QPU Delay Time per Sample: 21 µs
- Post Processing Overhead Time: 3.682 ms
- Total Post Processing Time: 3.682 ms

## Conclusion

This training project on Number Partitioning successfully utilizes QUBO optimization to partition a set of numbers into two equal subsets. The energy analysis and sample data provide insights into the optimization results. The timing information highlights the performance characteristics of the solution process.

-----------------------------------------------------------
.
├── project_cd24acdf-0a8f-44ae-a150-69ece39acec6
│   ├── code
│   ├── data
│   └── ...
└── project_6dbabf04-9a93-4534-9239-51d9edc7cbe2
    ├── code
    ├── data
    └── ...
### Project ID: 6dbabf04-9a93-4534-9239-51d9edc7cbe2

- **Training**: Embedding
- **Solver**: Advantage_system 4.1
- **Type**: QUBO
- **Status**: Completed
- **Submitted On**: 2023-05-18T22:14:41.533053Z
- **Solved On**: 2023-05-18T22:14:41.702012Z
- **Number of Reads**: 10

#### Problem and Solution

In this project, I focused on learning embedding techniques to better utilize the D-Wave quantum architecture. 

```math
Problem ID: 6dbabf04-9a93-4534-9239-51d9edc7cbe2
Solver: Advantage_system 4.1
Type: QUBO
Status: Completed
Submitted On: 2023-05-18T22:14:41.533053Z
Solved On: 2023-05-18T22:14:41.702012Z
Number of Reads: 10
```

#### QPU Sampling and Timing Information

- **QPU_SAMPLING_TIME**: \( t_{\text{sample}} = 11.732 \, \mathrm{ms} \)
- **QPU_ANNEAL_TIME_PER_SAMPLE**: \( \tau_{\text{anneal}} = 22 \, \mu \mathrm{s} \)
- **QPU_READOUT_TIME_PER_SAMPLE**: \( t_{\text{readout}} = 75 \, \mu \mathrm{s} \)
- (IN PROGRESS)

------

# Training Project - Number Partitioning

**ID:** f9046ca2-9cc9-40c1-8607-f26e4de62862

**SOLVED_ON:** 2023-05-18T23:05:11.291053Z

**LABEL:** Copy Value

**STATUS:** COMPLETED

**SOLVER:** Advantage_system 4.1

**SUBMITTED_BY:** Zi2q-7cdd45d9...

**TYPE:** qubo

**NUM_READS:** 100

**SUBMITTED_ON:** 2023-05-18T23:05:11.109121Z

## Sample Set

The training project involved a number partitioning problem. Here is a sample set in JSON format:

```json
[
  {
    "1831": 0,
    "1846": 0,
    "1860": 0,
    "1875": 0,
    "...": "...",
    "3204": 1,
    "energy": -9756.0,
    "num_oc.": 31
  },
  {
    "1831": 1,
    "1846": 1,
    "1860": 1,
    "1875": 1,
    "...": "...",
    "3204": 0,
    "energy": -9756.0,
    "num_oc.": 58
  },
  {
    "1831": 0,
    "1846": 0,
    "1860": 0,
    "1875": 0,
    "...": "...",
    "3204": 1,
    "energy": -9406.0,
    "num_oc.": 1
  },
  {
    "1831": 1,
    "1846": 1,
    "1860": 1,
    "1875": 1,
    "...": "...",
    "3204": 0,
    "energy": -9406.0,
    "num_oc.": 7
  },
  {
    "1831": 0,
    "1846": 0,
    "1860": 0,
    "1875": 0,
    "...": "...",
    "3204": 1,
    "energy": -9067.0,
    "num_oc.": 1
  },
  {
    "1831": 0,
    "1846": 0,
    "1860": 0,
    "1875": 0,
    "...": "...",
    "3204": 1,
    "energy": -9021.0,
    "num_oc.": 1
  },
  {
    "1831": 0,
    "1846": 0,
    "1860": 0,
    "1875": 0,
    "...": "...",
    "3204": 1,
    "energy": -8993.0,
    "num_oc.": 1
  }
]
```

## Performance Metrics

- **QPU_SAMPLING_TIME:** 9.024 ms
- **TOTAL_POST_PROCESSING_TIME:** 236 μs
- **QPU_ANNEAL_TIME_PER_SAMPLE:** 20 μs
- **POST_PROCESSING_OVERHEAD_TIME:** 236 μs
- **QPU_READOUT_TIME_PER_SAMPLE:** 50 μs
- **QPU_ACCESS_TIME:** 24.780 ms
- **QPU_ACCESS_OVERHEAD_TIME:** 2.061 ms
- **QPU_PROGRAMMING_TIME:** 15.756 ms
- **QPU_DELAY_TIME_PER_SAMPLE:** 21 μs

Please note that these performance metrics are indicative of the execution time and overhead involved in solving the number partitioning problem using the Advantage_system 4.1 solver.

For more information on the Advantage_system 4.1 solver, you can refer to the [D-Wave website](https://www.dwavesys.com/solutions-and-products/systems/) or other relevant resources.

----------------
# GitHub Portfolio

## D-Wave Systems Quantum Computing Training Project

### Problem Parameters

- ID: 10fd40b1-9ef5-4ea0-9e97-2c5a14c2c36d
    - The unique identifier for this problem.
- Label: Copy Value
    - The label given to this problem.
- Training: Number Partitioning
    - The type of training this problem belongs to, which is Number Partitioning in this case.
- Solver: Advantage_system 4.1
    - The solver used to solve this problem, which is the Advantage_system 4.1.
- Type: QUBO
    - The type of the problem formulation, which is Quadratic Unconstrained Binary Optimization (QUBO) in this case.
- Submitted On: 2023-05-18T23:05:19.742716Z
    - The date and time when this problem was submitted.
- Solved On: 2023-05-18T23:05:19.967823Z
    - The date and time when this problem was solved.
- Status: COMPLETED
    - The status of this problem, which is COMPLETED.
- Submitted By: Zi2q-7cdd45d9...
    - The identifier of the user who submitted this problem.
- Num Reads: 100
    - The number of reads performed on the solver.

### Solution Timing

- QPU Sampling Time: 11.640 ms
    - The total time taken by the Quantum Processing Unit (QPU) to perform the sampling operation, which is 11.640 milliseconds.
- QPU Anneal Time per Sample: 20 μs
    - The time taken by the QPU for each sample during the annealing process, which is 20 microseconds.
- QPU Readout Time per Sample: 76 μs
    - The time taken by the QPU for each sample during the readout process, which is 76 microseconds.
- QPU Access Time: 27.397 ms
    - The total time taken to access the QPU, including annealing time, readout time, and other overheads, which is 27.397 milliseconds.
- QPU Access Overhead Time: 1.938 ms
    - The overhead time incurred while accessing the QPU, which is 1.938 milliseconds.
- QPU Programming Time: 15.757 ms
    - The time taken to program the QPU with the problem, which is 15.757 milliseconds.
- QPU Delay Time per Sample: 21 μs
    - The delay time between each sample during the QPU operation, which is 21 microseconds.
- Post Processing Overhead Time: 427 μs
    - The overhead time incurred during post-processing, which is 427 microseconds.
- Total Post Processing Time: 427 μs
    - The total time taken for post-processing, which is 427 microseconds.

--------------------



## Project Details
- **ID:** 4838543d-7640-4f98-ba84-45d171c10911
- **Solver:** Advantage_system4.1
- **Type:** qubo
- **Status:** Completed
- **Submitted By:** Zi2q-7cdd45d9...
- **Number of Reads:** 100

## Problem Parameters and Solution Timing
### Sample Set
The results were exported in a JSON format, showcasing various energy levels and number occurrences:

\[
\begin{array}{lrrrrlrrr}
& 2465 & 2480 & 2495 & 2510 & \ldots & 4048 & \text{energy} & \text{num\_oc} \\
0 & 0 & 0 & 0 & 0 & \ldots & 1 & -9713.0 & 21 \\
1 & 1 & 1 & 1 & 1 & \ldots & 0 & -9713.0 & 41 \\
... 
15 & 1 & 1 & 1 & 1 & \ldots & 0 & -8735.0 & 1 \\
\end{array}
\]


## QPU Analytics
- **QPU Sampling Time:** 12.560 ms
- **Post-Processing Overhead Time:** 2.014 ms
- **QPU Anneal Time per Sample:** 20 µs
- **Total Post-Processing Time:** 2.014 ms
- **QPU Readout Time per Sample:** 85 µs
- **QPU Access Time:** 28.316 ms
- **QPU Access Overhead Time:** 7.735 ms
- **QPU Programming Time:** 15.756 ms
- **QPU Delay Time per Sample:** 21 µs


---

### Project ID: 43303521-9ac7-4cee-995e-71cf71268990
## Number Partitioning Algorithm 


### Overview

This project aims to solve the Number Partitioning problem by using D-Wave's quantum annealing technology. 

> **Mathematical Background**: The Number Partitioning problem can be represented as a QUBO (Quadratic Unconstrained Binary Optimization) problem with a Hamiltonian \( H = \sum_{i,j} a_{ij} x_i x_j \), where \( x_i \) are binary variables and \( a_{ij} \) are elements of a matrix that represents the problem constraints.

### Technologies Used

- Python3
- Ocean SDK
- D-Wave Leap Quantum Cloud Service


### Methodology

1. **Problem Formulation**: Transform the Number Partitioning problem into a QUBO problem.
2. **Quantum Annealing**: Utilize D-Wave's quantum annealer to find the optimal solution.
3. **Data Analysis**: Analyze the output for different problem instances.



### Results

The results were represented in terms of binary variables and energy states:

| Index | 702 | 732 | 747 | 762 | 777 | ... | 5238 | Energy |
|-------|-----|-----|-----|-----|-----|-----|------|--------|
| 0     | 0   | 0   | 0   | 1   | 0   | ... | 1    | -6889.0|
| 1     | 1   | 1   | 1   | 0   | 1   | ... | 0    | -6889.0|
| ...   | ... | ... | ... | ... | ... | ... | ...  | ...    |

> **Mathematical Insight**: The energy values indicate the quality of the solutions. Lower energy values represent better solutions according to the Hamiltonian \( H \).

#### Performance Metrics

- **QPU Sampling Time**: \(11.688 \, \text{ms}\)
- **Post-Processing Overhead Time**: \(3.737 \, \text{ms}\)
- **QPU Anneal Time Per Sample**: \(20 \, \mu \text{s}\)
- **Total Post-Processing Time**: \( ... \)



### Code Snippets

Here is an illustrative Python3 snippet for formulating the QUBO matrix:

```python
from dimod import BinaryQuadraticModel

# Create an empty Binary Quadratic Model
bqm = BinaryQuadraticModel('BINARY')

# Define QUBO interactions (Example values)
qubo_interactions = {(0, 0): -1, (1, 1): -1, (0, 1): 2}

# Add interactions to BQM
bqm.add_interactions_from(qubo_interactions)
```

> The above code sets up the QUBO matrix to represent the problem on the D-Wave quantum annealer.


------------



### Project Overview

**Title:**  
Training - Number Partitioning

**ID:**  
`79d129a2-12c3-4577-b14d-a5be2aa595a2`

**Solver Used:**  
Advantage_system4.1

**Type:**  
QUBO (Quadratic Unconstrained Binary Optimization)

**Status:**  
COMPLETED

**Submitted On:**  
2023-05-18T23:13:34.598117Z

**Solved On:**  
2023-05-18T23:13:34.772877Z

**Submitted By:**  
Zi2q-7cdd45d9...

**Number of Reads:**  
100

### Technical Metrics

#### Sampling Time Metrics

- **QPU Sampling Time:**  
  \( 14.184 \, \text{ms} \)
- **Post-Processing Overhead Time:**  
  \( 815 \, \mu \text{s} \)

#### QPU Timing Metrics

- **QPU Anneal Time Per Sample:**  
  \( 20 \, \mu \text{s} \)
- **Total Post-Processing Time:**  
  \( 815 \, \mu \text{s} \)
- **QPU Readout Time Per Sample:**  
  \( 101 \, \mu \text{s} \)
  
#### Access Time Metrics

- **QPU Access Time:**  
  \( 29.940 \, \text{ms} \)
- **QPU Access Overhead Time:**  
  \( 2.744 \, \text{ms} \)
- **QPU Programming Time:**  
  \( 15.756 \, \text{ms} \)
- **QPU Delay Time Per Sample:**  
  \( 21 \, \mu \text{s} \)

### Code Snippets



---

# D-Wave Systems Quantum Computing Training Project

## Metadata

- **Solver**: Advantage_system4.1
- **Type**: QUBO
- **ID**: aOc53d79-eab6-4661-8449-69d7c667fadb
- **Submitted On**: 2023-05-18T23:24:01.849039Z
- **Solved On**: 2023-05-18T23:24:02.052210Z
- **Status**: Completed
- **Submitted By**: Zi2q-7cdd45d9...
- **Number of Reads**: 100

## Performance Metrics

\[
\begin{align*}
\text{QPU Sampling Time} &: 10.704 \, \text{ms} \\
\text{QPU Anneal Time per Sample} &: 20 \, \mu \text{s} \\
\text{QPU Readout Time per Sample} &: 67 \, \mu \text{s} \\
\text{QPU Access Time} &: 26.462 \, \text{ms} \\
\text{QPU Access Overhead Time} &: 516 \, \mu \text{s} \\
\text{QPU Programming Time} &: 15.758 \, \text{ms} \\
\text{QPU Delay Time per Sample} &: 21 \, \mu \text{s} \\
\text{Post-Processing Overhead Time} &: 1.927 \, \text{ms} \\
\text{Total Post-Processing Time} &: 1.927 \, \text{ms} \\
\end{align*}
\]

## Solution

Here are some of the optimized solutions:

\[
\begin{array}{cccc}
1899 & 1914 & 1929 & \ldots \\
0 & 1 & 0 & \ldots \\
\vdots & \vdots & \vdots & \ddots \\
\end{array}
\]

Energy Level: -6889.0 to -6355.94833

## Code

---------


## Overview

- **Project ID**: d54e319b-20ba-4fdd-8341-aa8430e83fbb
- **Solver**: Advantage_system4.1
- **Type**: QUBO (Quadratic Unconstrained Binary Optimization)
- **Submitted On**: 2023-05-18
- **Solved On**: 2023-05-18
- **Status**: COMPLETED
- **Submitted By**: Zi2q-7cdd45d9...
- **Number of Reads**: 100

## Performance Metrics

- **QPU Sampling Time**: N/A
- **Post-Processing Overhead Time**: 9.264 ms
- **Total Post-Processing Time**: 711μs
- **QPU Readout Time Per Sample**: 52μs
- **QPU Access Time**: 25.022 ms
- **QPU Access Overhead Time**: 827μs
- **QPU Programming Time**: 15.758 ms
- **QPU Delay Time Per Sample**: 21μs

## Results Summary

The output energies ranged from -6889.0 to -6313.0, with varying numbers of occurrences for each unique solution.

| Energy  | Number of Occurrences |
| ------- | --------------------- |
| -6889.0 | 2                     |
| -6888.0 | 16                    |
| -6880.0 | 15                    |
| ...     | ...                   |
| -6313.0 | 1                     |

## Python Code for Processing

The Python code to retrieve and process the quantum results was as follows.

```python
# Python code to process D-Wave output
from dwave.system import DWaveSampler, EmbeddingComposite

# Initialize sampler and composite
sampler = DWaveSampler(solver={'qpu': True})
composite = EmbeddingComposite(sampler)

# Define QUBO problem (example)
Q = {(0, 0): -1, (1, 1): -1, (0, 1): 2}

# Sample
sampleset = composite.sample_qubo(Q, num_reads=100)

# Process results
for sample, energy, occurrences in sampleset.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy:", energy, "Occurrences:", occurrences)
```

## Mathematical Expression

The energy function \( E \) in a QUBO problem is given by

\[
E = \sum_{i} q_{i} x_{i} + \sum_{i < j} q_{ij} x_{i} x_{j}
\]

Here, \( q_{i} \) and \( q_{ij} \) are coefficients of the QUBO matrix, and \( x_{i} \) are binary variables (0 or 1).


-------


```markdown
# D-Wave Systems Quantum Computing: Session 2


## Project Details

### Problem Statement
The optimization problem remains in the QUBO framework, which is ideal for solving problems like the Traveling Salesman Problem, Maximum Cut, etc.

### Solution Methodology
The problem was solved using the Quantum Annealing algorithm, optimized using the QUBO method.


## Solver Metrics

### Basic Metrics
- **Solver**: Advantage_system4.1
- **Type**: qubo
- **Status**: COMPLETED
- **Submitted By**: Zi2q-7cdd45d9...
- **ID**: cb05cbd3-e180-4919-958a-98b2a95bb94d

### Timing Metrics
- **QPU Sampling Time**: \(8.176 \, \text{ms}\)
- **QPU Anneal Time Per Sample**: \(20 \, \mu \text{s}\)
- **QPU Readout Time Per Sample**: \(41 \, \mu \text{s}\)
- **QPU Access Time**: \(23.937 \, \text{ms}\)
- **QPU Access Overhead Time**: \(1.503 \, \text{ms}\)
- **QPU Programming Time**: \(15.761 \, \text{ms}\)
- **QPU Delay Time Per Sample**: \(21 \, \mu \text{s}\)
- **Total Post-Processing Time**: \(802 \, \mu \text{s}\)
- **Post-Processing Overhead Time**: \(802 \, \mu \text{s}\)


## Results and Analysis

The output results show different configurations with respective energies and occurrences. The lowest energy configuration is our area of interest.

```
1144 | 1234 | 3846 | 3905 | energy  | num_oc.
-----|------|------|------|---------|--------
  0  |  1   |  1   |  0   |  -1.0   |   53
  0  |  1   |  1   |  1   |  -1.0   |   47
```


## Mathematical Context

The energy function \(E\) can be expressed as:

\[
E(x) = \sum_{i=1}^{4} \sum_{j=1}^{4} Q_{ij} x_i x_j
\]

Here, \(Q_{ij}\) represents the coefficients in the QUBO problem, and \(x_i\) are the binary variables. Minimizing \(E(x)\) provides us with the optimal solution.



## Python3 Code

Here's a Python3 example using D-Wave's SDK:

```python
from dwave.system import DWaveSampler, EmbeddingComposite

# Define the QUBO dictionary
Q = {(1144, 1144): 1, (1234, 1234): -2, (3846, 3846): 3, (3905, 3905): -4}

# Use the D-Wave sampler
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q, num_reads=100)

# Output results
for sample, energy, num_oc in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy: ", energy, "Occurrences: ", num_oc)
```


--------


## Project Details

### Problem Statement
The objective of this project was to explore the quantum annealing capabilities for solving number partitioning problems. Number partitioning is a computationally complex problem and provides an excellent use-case for quantum computing.

### Solution Methodology
We utilized D-Wave's Quantum Annealing Solver to solve the given problem. The optimization process was carried out using the Quadratic Unconstrained Binary Optimization (QUBO) framework.


## Solver Metrics

### Basic Metrics
- **Solver**: Advantage_system4.1
- **Type**: qubo
- **Status**: COMPLETED
- **Submitted By**: Zi2q-7cdd45d9...
- **ID**: 98fd1adb-7c4e-48e2-9172-8513b098d505

### Timing Metrics
- **QPU Sampling Time**: 9.040 ms
- **QPU Anneal Time Per Sample**: 20 µs
- **QPU Readout Time Per Sample**: 50 µs
- **QPU Access Time**: 24.801 ms
- **QPU Access Overhead Time**: 2.498 ms
- **QPU Programming Time**: 15.761 ms
- **QPU Delay Time Per Sample**: 21 µs
- **Total Post-Processing Time**: 587 µs
- **Post-Processing Overhead Time**: 587 µs


## Results and Analysis

The QUBO problem was solved using 100 reads, and the output included several configurations with different energy levels. The lowest energy configuration provides the most optimal solution.

```
energy  | num_oc. | 2473 | 2488 | 2503 | ... | 5428
--------|---------|------|------|------|-----|------
-6889.0 |    1    |  0   |  0   |  0   | ... |  1
-6889.0 |    1    |  0   |  1   |  0   | ... |  0
-6888.0 |    4    |  1   |  1   |  0   | ... |  1
...     |   ...   | ...  | ...  | ...  | ... | ...
```



## Mathematical Context

The energy function \(E\) in QUBO is usually represented as:

![](https://cdn.mathpix.com/snip/images/4evS5-3IUIijq1_oV09tpGI5eGNCMYYhmHuFkDHIIts.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/8PeqKHCJYfSQ_vTv6yGZiBqLi4OdPlQlUycEt0IMFrw.original.fullsize.png)


## Python3 Code

Here is a sample Python3 code snippet to perform a quantum annealing task using D-Wave's Python SDK:

```python
from dwave.system import DWaveSampler, EmbeddingComposite

# Define QUBO dictionary
Q = {(0, 0): -1, (0, 1): 2, (1, 1): -1}
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q, num_reads=100)

# Extract results
for sample, energy, num_oc in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy: ", energy, "Occurrences: ", num_oc)
```

---



### Solution Methodology
We utilized D-Wave's Quantum Annealing Solver to solve the given problem. The optimization process was carried out using the Quadratic Unconstrained Binary Optimization (QUBO) framework.



## Solver Metrics

### Basic Metrics
- **Solver**: Advantage_system4.1
- **Type**: qubo
- **Status**: COMPLETED
- **Submitted By**: Zi2q-7cdd45d9...
- **ID**: 98fd1adb-7c4e-48e2-9172-8513b098d505

### Timing Metrics
- **QPU Sampling Time**: 9.040 ms
- **QPU Anneal Time Per Sample**: 20 µs
- **QPU Readout Time Per Sample**: 50 µs
- **QPU Access Time**: 24.801 ms
- **QPU Access Overhead Time**: 2.498 ms
- **QPU Programming Time**: 15.761 ms
- **QPU Delay Time Per Sample**: 21 µs
- **Total Post-Processing Time**: 587 µs
- **Post-Processing Overhead Time**: 587 µs


## Results and Analysis

The QUBO problem was solved using 100 reads, and the output included several configurations with different energy levels. The lowest energy configuration provides the most optimal solution.

```
energy  | num_oc. | 2473 | 2488 | 2503 | ... | 5428
--------|---------|------|------|------|-----|------
-6889.0 |    1    |  0   |  0   |  0   | ... |  1
-6889.0 |    1    |  0   |  1   |  0   | ... |  0
-6888.0 |    4    |  1   |  1   |  0   | ... |  1
...     |   ...   | ...  | ...  | ...  | ... | ...
```



## Mathematical Context

The energy function \(E\) in QUBO is usually represented as:

\[
E(x) = \sum_{i,j} Q_{ij} x_i x_j
\]

where \(Q_{ij}\) are the elements of a QUBO matrix and \(x_i, x_j\) are the binary variables. The objective is to find \(x\) that minimizes \(E(x)\).



## Python3 Code

Here is a sample Python3 code snippet to perform a quantum annealing task using D-Wave's Python SDK:

```python
from dwave.system import DWaveSampler, EmbeddingComposite

# Define QUBO dictionary
Q = {(0, 0): -1, (0, 1): 2, (1, 1): -1}
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q, num_reads=100)

# Extract results
for sample, energy, num_oc in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy: ", energy, "Occurrences: ", num_oc)
```

-----------


```markdown
# D-Wave Systems Quantum Computing: Session 2

## Table of Contents
1. [Overview](#overview)
2. [Project Details](#project-details)
3. [Solver Metrics](#solver-metrics)
4. [Results and Analysis](#results-and-analysis)
5. [Mathematical Context](#mathematical-context)
6. [Python3 Code](#python3-code)


## Project Details

### Problem Statement
The optimization problem remains in the QUBO framework, which is ideal for solving problems like the Traveling Salesman Problem, Maximum Cut, etc.

### Solution Methodology
The problem was solved using the Quantum Annealing algorithm, optimized using the QUBO method. Larger graphs are formulated as QUBOs for hybrid classical quantum qbsolv - 0/1 valued variables
Minimizing the objective function:

![](https://cdn.mathpix.com/snip/images/ozCxV5w06PKTszZYJ3dUlnFBDQOo_0DVKnDzP5kYVGQ.original.fullsize.png)

$$
O(Q, x)=\Sigma Q_{i i} x_i+\Sigma q_{i j} x_i x_j
$$

## Solver Metrics

### Basic Metrics
- **Solver**: Advantage_system4.1
- **Type**: qubo
- **Status**: COMPLETED
- **Submitted By**: Zi2q-7cdd45d9...
- **ID**: cb05cbd3-e180-4919-958a-98b2a95bb94d

### Timing Metrics
- **QPU Sampling Time**: \(8.176 \, \text{ms}\)
- **QPU Anneal Time Per Sample**: \(20 \, \mu \text{s}\)
- **QPU Readout Time Per Sample**: \(41 \, \mu \text{s}\)
- **QPU Access Time**: \(23.937 \, \text{ms}\)
- **QPU Access Overhead Time**: \(1.503 \, \text{ms}\)
- **QPU Programming Time**: \(15.761 \, \text{ms}\)
- **QPU Delay Time Per Sample**: \(21 \, \mu \text{s}\)
- **Total Post-Processing Time**: \(802 \, \mu \text{s}\)
- **Post-Processing Overhead Time**: \(802 \, \mu \text{s}\)


## Results and Analysis

The output results show different configurations with respective energies and occurrences. The lowest energy configuration is our area of interest.

```
1144 | 1234 | 3846 | 3905 | energy  | num_oc.
-----|------|------|------|---------|--------
  0  |  1   |  1   |  0   |  -1.0   |   53
  0  |  1   |  1   |  1   |  -1.0   |   47
```



## Python3 Code

Python3 example using D-Wave's SDK:

```python
from dwave.system import DWaveSampler, EmbeddingComposite

# Define the QUBO dictionary
Q = {(1144, 1144): 1, (1234, 1234): -2, (3846, 3846): 3, (3905, 3905): -4}

# Use the D-Wave sampler
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q, num_reads=100)

# Output results
for sample, energy, num_oc in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy: ", energy, "Occurrences: ", num_oc)
```





```markdown


## Project Summary
**Problem Statement:** Quantum Optimization for Real-world Problems  
**Solution Methodology:** Quantum Annealing  
**Solver Used:** D-Wave Advantage_system4.1  
**Status:** Completed


## Technologies
- Python 3
- D-Wave Ocean SDK
- NumPy
- Mathematical Formulation (QUBO)



## Solver Metrics

### Basic Metrics
- **Solver**: Advantage_system4.1
- **Type**: qubo
- **Status**: COMPLETED
- **ID**: d1d2971f-70f0-4db4-aec4-7cb25734aedb
- **Submitted By**: Zi2q-7cdd45d9...
- **Submitted On**: 2023-05-19T02:46:11.148532Z
- **Num Reads**: 100

### Timing Metrics
- **QPU Sampling Time**: \(9.346 \, \text{ms}\)
- **QPU Anneal Time Per Sample**: \(20 \, \mu \text{s}\)
- **QPU Readout Time Per Sample**: \(53 \, \mu \text{s}\)
- **QPU Access Time**: \(25.107 \, \text{ms}\)
- **QPU Access Overhead Time**: \(1.258 \, \text{ms}\)
- **QPU Programming Time**: \(15.761 \, \text{ms}\)
- **QPU Delay Time Per Sample**: \(21 \, \mu \text{s}\)
- **Total Post-Processing Time**: \(3.709 \, \text{ms}\)
- **Post-Processing Overhead Time**: \(3.709 \, \text{ms}\)


## Results

The output was an optimal solution for our problem with the following attributes:

\[
\begin{aligned}
& 173243134463 \quad \text {energy num_oc.} \\
& 0 \quad 1 \quad 1 \quad 0 \quad -1.0 \quad 100 \\
\end{aligned}
\]


## Mathematical Context

The energy function \(E\) can be modeled as:

\[
E(x) = \sum_{i=1}^{n} \sum_{j=1}^{n} Q_{ij} x_i x_j
\]

where \(Q_{ij}\) are the coefficients in the QUBO problem, and \(x_i\) are the binary variables.



##  Code



```python
# Sample Python code using D-Wave SDK
from dwave.system import DWaveSampler, EmbeddingComposite
Q = {(0, 0): 1, (1, 1): -1, (2, 2): 1}
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q, num_reads=100)
```

---


```markdown


## Project ID: a4253abc-9a1b-4b8f-b5e3-4fb85b11cfdf

### Meta Information
- **Solver**: Advantage_system4.1
- **Type**: qubo
- **Submitted On**: 2023-05-18T20:10:44.740770Z
- **Solved On**: 2023-05-18T20:10:45.314233Z
- **Status**: COMPLETED
- **Submitted By**: Zi2q-7cdd45d9...
- **Number of Reads**: 10



### Project Overview


### Results
```latex
\begin{aligned}
& 997 1012 1042 4309 4340 4385 4400 \text{ energy num_oc. } \\
& 0   0    0    1    1    0    1   -3.0       1 \\
& 1   0    1    0    0    1    1    0   -3.0       5 \\
& 2   0    1    0    0    1    0    1   -3.0       2 \\
& 3   0    0    0    1    1    1    0   -3.0       2 \\
& \text{['BINARY', 4 rows, 10 samples, 7 variables]}
\end{aligned}
```

### QPU Metrics
- **QPU Sampling Time**: 891 µs
- **Total Post-Processing Time**: 141 µs
- **QPU Anneal Time per Sample**: 141 µs
- **Post-Processing Overhead Time**: 141 µs
- **QPU Readout Time per Sample**: 49 µs
- **QPU Access Time**: 16.649 ms
- **QPU Access Overhead Time**: 741 µs
- **QPU Programming Time**: 15.757 ms
- **QPU Delay Time per Sample**: 21 µs


### Code Snippets


### Conclusion


```

---



## Projects

### Graph Mapping with D-Wave Systems

![Open in Leap IDE](https://cdn-assets.cloud.dwavesys.com/shared/latest/badges/leapide.svg)](https://ide.dwavesys.io/#https://github.com/dwave-training/graph-mapping)

**Overview**:  
This project leverages D-Wave Systems to solve graph mapping problems. Specifically, it aims to solve the antenna selection problem using quantum annealing.

#### Exercise Highlights

- **Exercise 1**: Initialization  
  - Token authentication for D-Wave's Leap IDE.
  - Introduction to `dwave-networkx`.

- **Exercise 2**: Simulated Annealing  
  - Implementing the simulated annealing algorithm.

- **Exercise 3**: Problem Modification  
  - Modified the original problem to solve for minimum vertex cover.

#### Core Technologies

- NetworkX
- D-Wave NetworkX
- D-Wave System's QPU
- Matplotlib for visualization

#### Code Snippets

```python
# Importing essential packages
import networkx as nx
from dwave.system import DWaveSampler, EmbeddingComposite

# Creating the graph structure
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (6, 7)])

# Defining sampler
sampler = EmbeddingComposite(DWaveSampler())
```

#### Outputs




#### References

- [D-Wave Collection of Examples](https://github.com/dwave-examples/antenna-selection)
- [Ocean Documentation](https://docs.ocean.dwavesys.com/en/stable/)

---

## Technologies Used

- Python
- D-Wave Systems
- NetworkX
- Matplotlib
- Leap IDE



---
## Contact

Feel free to connect with me:

- 📧 Email: davidmerwin1992@gmail.com
- 💼 LinkedIn:
- 🌐 Portfolio: [D-Wave Profile](https://support.dwavesys.com/hc/en-us/profiles/384378940113-David-M)



Thank you for visiting my portfolio! 😊


  
Feel free to reach out if you have any questions or would like to collaborate!

---

## Key sources in context

The published work and documentation behind the training projects above, written as a compact annotated bibliography. Each source is tied to files in this repository. None is used to claim a quantum advantage. <sup>[E1](#en1)</sup>

**How to read each entry.** The *caption*, *metadata*, *descriptors*, *tags* and *labels* form the catalog card. The *abstract*, *gloss*, *commentary* (with its *elucidation* and *exposition*), *exegesis* and *critique* are the reading. *Marginalia* point to files in this repository, *scholia* compare the sources with each other, and each entry has one *footnote*. The anchors (`#b11`, `#b11-fn`) are the *markup*. Code comments, docstrings, directives and decorators in this repository are listed after the entries.

**Sources:** [B1](#b1) · [B36](#b36) · [B11](#b11) · [B12](#b12) · [B44](#b44) · [B53](#b53) · [B13](#b13) · [B14](#b14) · [B10](#b10) · [B9](#b9) · [B43](#b43) · [B37](#b37) · [B16](#b16) · [B17](#b17) <sup>[E2](#en2)</sup>

<a id="b1"></a>

### B1 · Quantum annealing in the transverse Ising model

> **Caption.** The paper that named quantum annealing: tunnelling, not heat, as the search engine.

**Metadata.** Tadashi Kadowaki, Hidetoshi Nishimori (1998). *Physical Review E 58(5): 5355–5363*. Journal article. DOI: [10.1103/PhysRevE.58.5355](https://doi.org/10.1103/PhysRevE.58.5355). Verified 10 Nov 2026.<br>
**Descriptors.** Quantum annealing · Ising model · **Tags.** `transverse-field` `origin` `simulated-annealing-comparison` · **Labels.** `evidence:peer-reviewed` `role:foundation` `type:journal-article` `status:verified`

- **Abstract.** Introduces quantum annealing: add a transverse field to an Ising problem, then slowly weaken it so quantum fluctuations, rather than thermal ones, carry the system toward low-energy states. Small numerical experiments compare it with simulated annealing.
- **Gloss.** *Transverse field*: A term that lets spins flip by quantum tunnelling; it is the 'driver' that is slowly turned off. *Ising model*: Energy function over ±1 spins with local fields h and couplings J.
- **Commentary.** The root of every QPU run recorded above. *Elucidation:* It explains what `QPU_ANNEAL_TIME_PER_SAMPLE` (20 µs in the Project ID sections) is timing: one sweep of the transverse field from strong to zero. *Exposition:* Replace temperature with a transverse field Γ(t). At large Γ the ground state is an easy superposition; as Γ→0 the Hamiltonian becomes the problem Ising model, and a slow enough sweep leaves the system near its ground state.
- **Exegesis.** The paper reports that quantum annealing reached the ground state with higher probability than thermal annealing *in the small systems simulated with the schedules used*. It does not claim a general speedup, and it does not describe hardware.<sup>[1](#b1-fn)</sup>
- **Critique.** Small, numerically simulated instances in an idealised closed system. Later benchmarking (B37) shows any advantage depends on the instance and the baseline.
- **Marginalia.**
  - `README.md`: Project ID cd24acdf… records 100 reads at 20 µs anneal time each, the hardware form of this paper's sweep.
  - `KeyTerms.md`: The super-node and one-hot ideas are formulation choices, separate from the annealing method itself.
- **Scholia.** [B36](#b36): The thermal method this paper replaced; read the two together. [B13](#b13): What changes once the ideal Ising model has to fit real hardware.
- **Footnote.** <a id="b1-fn"></a>¹ Co-author Nishimori stayed central to the field, so later reviews trace back to this paper directly.
- **In context.** Background for every Advantage_system4.1 training run in this README.

<a id="b36"></a>

### B36 · Optimization by Simulated Annealing

> **Caption.** The classical baseline every annealing claim must face.

**Metadata.** S. Kirkpatrick, C. D. Gelatt, M. P. Vecchi (1983). *Science 220(4598): 671–680*. Journal article. DOI: [10.1126/science.220.4598.671](https://doi.org/10.1126/science.220.4598.671). Verified 10 Nov 2026.<br>
**Descriptors.** Classical baselines · Quantum annealing · **Tags.** `simulated-annealing` `metropolis` · **Labels.** `evidence:peer-reviewed` `role:foundation` `type:journal-article` `status:verified`

- **Abstract.** Borrows the Metropolis procedure from statistical mechanics to optimise combinatorial problems by slowly lowering a temperature, and applies it to chip partitioning, placement and wiring, and the travelling salesman problem.
- **Gloss.** *Temperature schedule*: How T decreases; controls the trade-off between exploration and settling. *Metropolis rule*: Accept uphill moves with probability exp(−ΔE/T).
- **Commentary.** The classical twin of quantum annealing, and the first baseline to compare against. *Elucidation:* Ocean's `SimulatedAnnealingSampler` is this 1983 algorithm running on a CPU, so a local run of these exercises is classical, not a QPU job. *Exposition:* Random local moves, accepted downhill always and uphill sometimes, with the 'sometimes' shrinking over time, let the search escape local minima.
- **Exegesis.** SA is a *heuristic*; the paper shows good solutions on its examples, not optimality guarantees at practical schedules.<sup>[1](#b36-fn)</sup>
- **Critique.** Performance is schedule-sensitive; modern parallel tempering and specialised solvers are stronger baselines.
- **Marginalia.**
  - `Problemtwo.md`: Small enough to solve with simulated annealing or `ExactSolver` and compare with the QPU sample set.
  - `README.md`: The Number Partitioning energies (−9826.5 best) can be checked against a local SA run.
- **Scholia.** [B1](#b1): Heat here, tunnelling there. [B37](#b37): A study where the QPU beat SA on crafted instances, and why that is not a general result.
- **Footnote.** <a id="b36-fn"></a>¹ The Metropolis acceptance rule (1953) is older; this paper turned it into an optimizer.
- **In context.** The baseline to log next to any QPU result in this repository.

<a id="b11"></a>

### B11 · Ising formulations of many NP problems

> **Caption.** The cookbook: how constraints become quadratic penalties.

**Metadata.** Andrew Lucas (2014). *Frontiers in Physics 2: 5*. Journal article. DOI: [10.3389/fphy.2014.00005](https://doi.org/10.3389/fphy.2014.00005). Verified 10 Nov 2026.<br>
**Descriptors.** QUBO formulation · Ising model · **Tags.** `penalty-terms` `number-partitioning` `graph-coloring` `tsp` · **Labels.** `evidence:peer-reviewed` `role:method` `type:journal-article` `status:verified`

- **Abstract.** Catalogues Ising/QUBO encodings for dozens of NP-complete and NP-hard problems, from number partitioning and graph colouring to covering, cliques and travelling salesman, with attention to how many spins each needs.
- **Gloss.** *Penalty term*: A quadratic energy added so that constraint violations cost energy. *One-hot encoding*: A group of binaries of which exactly one must be 1.
- **Commentary.** The cookbook for writing a problem as an Ising or QUBO model. *Elucidation:* Number partitioning and maximum independent set, the problems in the Number Partitioning projects and `Maxindependentsetgraph.md`, both follow its encodings. *Exposition:* Write the objective as a quadratic in binaries; add λ·(constraint residual)² for each constraint; choose λ big enough that violations never pay.
- **Exegesis.** Lucas gives *encodings*, with spin counts. He does not claim annealers solve these problems well, and penalty weights are left to the modeller.<sup>[1](#b11-fn)</sup>
- **Critique.** Penalty-based encodings can create rugged landscapes and large coefficient ranges that hurt hardware precision (see B12, B13).
- **Marginalia.**
  - `README.md`: Number Partitioning (Project ID 23cf353c…) is a direct instance of Lucas's partitioning Hamiltonian.
  - `Maxindependentsetgraph.md`: Uses `dwave_networkx` with `EmbeddingComposite` for a maximum-independent-set problem. The library builds the QUBO this paper writes out by hand.
  - `KeyTerms.md`: k-concurrent partitioning with one qubit on per vertex is Lucas-style graph colouring.
- **Scholia.** [B12](#b12): The operations-research tutorial version of the same recipes. [B13](#b13): The cost of these encodings once they are embedded.
- **Footnote.** <a id="b11-fn"></a>¹ The preprint is arXiv:1302.5843; the journal version is cited here.
- **In context.** The encoding reference for the Number Partitioning and graph exercises.

<a id="b12"></a>

### B12 · Quantum Bridge Analytics I: a tutorial on formulating and using QUBO models

> **Caption.** QUBO modelling for operations researchers, with penalty-weight guidance.

**Metadata.** Fred Glover, Gary Kochenberger, Yu Du (2019). *4OR 17(4): 335–371*. Journal article. DOI: [10.1007/s10288-019-00424-y](https://doi.org/10.1007/s10288-019-00424-y). Verified 10 Nov 2026.<br>
**Descriptors.** QUBO formulation · **Tags.** `tutorial` `operations-research` `penalty-weights` · **Labels.** `evidence:peer-reviewed` `role:method` `type:journal-article` `status:verified`

- **Abstract.** A worked tutorial for building QUBO models of classic combinatorial problems, with standard penalty forms for common constraints and practical advice on choosing penalty scalars.
- **Gloss.** *QUBO*: Quadratic unconstrained binary optimization: minimise xᵀQx over x∈{0,1}ⁿ. *Penalty scalar P*: Weight that makes infeasible solutions unattractive.
- **Commentary.** A practical tutorial on QUBO penalties and how to weight them. *Elucidation:* `objective_function.md`'s γ·Σ(1−xᵢ−xⱼ+xᵢxⱼ) edge term is a standard penalty from this paper, and γ is its penalty scalar P. *Exposition:* Reduce each constraint to a known quadratic penalty pattern, sum them with the objective, and tune P by testing feasibility of returned samples.
- **Exegesis.** The tutorial offers *rules of thumb* for P, not guarantees. It does not address hardware precision or embedding.<sup>[1](#b12-fn)</sup>
- **Critique.** Heuristic weight advice; CQM models (B16) now avoid some hand-tuned penalties.
- **Marginalia.**
  - `objective_function.md`: γ trades off covering edges against using fewer vertices; tune it as B12 suggests.
  - `Problem3.md`: The implication truth table (X→Y) mapped to energies is one of B12's standard constraint penalties.
  - `Problemtwo.md`: Penalising equal qubit values is the two-variable 'not equal' penalty.
  - `Scheduling.md`: Shift preferences plus one-shift-per-employee constraints use the same logic in a DQM.
- **Scholia.** [B11](#b11): The physics catalogue of the same idea. [B17](#b17): Where these Q matrices become BQM objects.
- **Footnote.** <a id="b12-fn"></a>¹ The tutorial is Part I of a series; later parts are not cited here.
- **In context.** The guide to the penalty terms in `objective_function.md`, `Problemtwo.md`, `Problem3.md` and `Scheduling.md`.

<a id="b44"></a>

### B44 · Foundations for Quantum Programming: full course bundle

> **Caption.** The whole D-Wave foundations course in one 316-page file: math, constraints, QUBO and Python.

**Metadata.** D-Wave Quantum Inc. (2024). *Foundations for Quantum Programming (self-paced online course, D-Wave training); slide deck v1.x; not peer-reviewed*. Course material (grey literature). [training.dwavequantum.com/product?catalog=FoundationsQuantumProgramming](https://training.dwavequantum.com/product?catalog=FoundationsQuantumProgramming). Verified 10 Nov 2026.<br>
**Descriptors.** Curriculum · QUBO formulation · Constraint encoding · Mathematical foundations · **Tags.** `course-material` `grey-literature` `course-bundle` `dwave-training` · **Labels.** `evidence:grey-literature` `role:curriculum` `type:course-material` `status:verified`

- **Abstract.** D-Wave's self-paced course of slide decks with speaker notes, an optional prerequisite to its Quantum Programming Core training. It covers math symbols, sets, functions, polynomials, summation notation, truth tables, graphs, matrices, variable types, quadratic models and QUBOs, constraints and penalty expressions, combining objectives with constraints, and Python basics (data structures, if statements, loops, list comprehensions, functions, packages and Codespaces).
- **Gloss.** *Quadratic model (QM)*: A polynomial objective of degree at most two; the course says every model D-Wave software accepts is of this kind. *Lagrange parameter*: The course's name for the weight that multiplies a penalty expression before it is added to the objective.
- **Commentary.** The course this repository's formulation habits come from, cited here as grey literature: D-Wave's own training slides, not a paper. *Elucidation:* It explains the repo's pattern of binary variables, a truth table per rule, a penalty per truth table, and one objective handed to a sampler. *Exposition:* The course runs a five-step recipe: state the objective and constraints in words; choose binary variables; write both as math; convert each constraint into a penalty that is zero exactly when it holds; add the weighted penalties to the objective and simplify, using x² = x for binary variables. Worked examples include picking two of three objects at minimum weight and a four-subset set-partitioning problem with two weights (λ and γ).
- **Exegesis.** The bundle teaches formulation; it does not claim that any formulation runs faster on a QPU, and it does not tell the learner how large the penalty weight must be. That choice is left to later courses and to B12's guidance.<sup>[1](#b44-fn)</sup>
- **Critique.** Vendor teaching material with no references, so each rule should be traced to B11, B12 or B17. Its worked examples stop before choosing penalty weights: in its own pick-two-of-three example the feasible answer has the lowest energy only if the weight λ exceeds 5, which a local `ExactSolver` run confirms.
- **Marginalia.**
  - `KeyTerms.md`: Its penalty table has the same six rows as the course's two-variable table.
  - `Scheduling.md`: The DQM already gives each employee exactly one shift, so the uniform quadratic bias of 1 between every pair of employees adds only a constant; it does not enforce anything, despite the code comment.
  - `README.md`: The Number Partitioning projects follow the course's QUBO recipe.
- **Scholia.** [B12](#b12): The citable source for the same penalties. [B11](#b11): The recipe at the scale of NP problems. [B17](#b17): Where the combined objective becomes a BQM.
- **Footnote.** <a id="b44-fn"></a>¹ Slides © D-Wave Quantum Inc., 2024, v1.x; course page verified 10 Nov 2026. They are described here, not reproduced.
- **In context.** Background for every formulation file in this repository.

<a id="b53"></a>

### B53 · Penalty Expressions and Logical Constraints (reference sheets)

> **Caption.** Two one-page tables: logical rule, its equality or inequality, and the penalty that enforces it.

**Metadata.** D-Wave Quantum Inc. (2024). *Foundations for Quantum Programming (self-paced online course, D-Wave training); slide deck v1.x; not peer-reviewed*. Course material (grey literature). [training.dwavequantum.com/product?catalog=FoundationsQuantumProgramming](https://training.dwavequantum.com/product?catalog=FoundationsQuantumProgramming). Verified 10 Nov 2026.<br>
**Descriptors.** Curriculum · Constraint encoding · QUBO formulation · **Tags.** `course-material` `grey-literature` `penalties` `logic` · **Labels.** `evidence:grey-literature` `role:curriculum` `type:course-material` `status:verified`

- **Abstract.** Reference tables pairing two-variable rules (AND, OR, NAND, XOR, implication both ways, IFF) and three-variable rules (all three, at most one, exactly two, and others) with their equality or inequality and, on the penalty sheet, a quadratic penalty that is zero exactly when the rule holds.
- **Gloss.** *Penalty expression*: A function that is zero on allowed assignments and positive on forbidden ones. *Equality penalty*: The square of (sum − target), expanded with x² = x.
- **Commentary.** The one-page penalty catalogue from the same course. *Elucidation:* Every penalty in this repo is a row of it: OR per edge in `objective_function.md`, implication in `Problem3.md`, XOR in `Problemtwo.md`. *Exposition:* Two families. Equalities use squared residuals: AND is (x + y − 2)², XOR is (x + y − 1)², exactly-two-of-three is (x + y + z − 2)². Inequalities use products: NAND is xy, OR is (1 − x)(1 − y), at most one of three is xy + xz + yz. All rows were checked here by enumeration and every one is correct.
- **Exegesis.** The sheets list penalties; they do not say penalties are not unique (any positive multiple ranks assignments the same way), and they do not mention that some rules have no penalty of this kind at all without an extra variable.<sup>[1](#b53-fn)</sup>
- **Critique.** Correct (all ten rows check out by enumeration) but uncited; the two-variable rows match B12's table. It offers no penalty for 'at least one of three' or 'at most two of three', and none exists without an extra variable.
- **Marginalia.**
  - `Problem3.md`: Energies 0, 0, 1, 0 for 00, 01, 10, 11 are the implication penalty x − xy.
  - `Problemtwo.md`: Favoring unequal pairs is XOR: 1 − x − y + 2xy.
  - `objective_function.md`: Expanding γ(1 − xᵢ − xⱼ + xᵢxⱼ) gives +γ on each edge interaction and −γ on each endpoint's linear term. The Python snippet uses −2γ on the interaction and no linear −γ terms, so its energies differ from the formula's on 11 of the 16 assignments of its 4-node example.
- **Scholia.** [B12](#b12): Glover's table is the citable form of these rows. [B11](#b11): Whole Hamiltonians built from such terms.
- **Footnote.** <a id="b53-fn"></a>¹ Two reference sheets: Penalty Expressions and Logical Constraints. The arithmetic above was checked locally with dimod's classical ExactSolver; no QPU was used.
- **In context.** The penalty reference for `KeyTerms.md`, `Problem3.md`, `Problemtwo.md` and `objective_function.md`.

<a id="b13"></a>

### B13 · Minor-embedding in adiabatic quantum computation: I. The parameter setting problem

> **Caption.** Why chain strength exists, and what goes wrong when it is wrong.

**Metadata.** Vicky Choi (2008). *Quantum Information Processing 7(5): 193–209*. Journal article. DOI: [10.1007/s11128-008-0082-9](https://doi.org/10.1007/s11128-008-0082-9). Verified 10 Nov 2026.<br>
**Descriptors.** Minor embedding · **Tags.** `chain-strength` `chain-break` `parameter-setting` · **Labels.** `evidence:peer-reviewed` `role:foundation` `type:journal-article` `status:verified`

- **Abstract.** Formalises minor embedding for annealers and derives conditions on the ferromagnetic coupling within qubit chains so the embedded Hamiltonian keeps the original ground state.
- **Gloss.** *Minor embedding*: Representing one logical variable by a connected chain of physical qubits. *Chain break*: A returned sample where qubits of one chain disagree.
- **Commentary.** Why chain strength exists. *Elucidation:* `sampleset.md` guesses that a `chain_.` column could mean chain breaks. It does, and this paper explains why they matter. *Exposition:* Chains must be coupled strongly enough to act as one spin, but not so strongly that they swamp the problem's own energy scale.
- **Exegesis.** Gives *sufficient* bounds for ground-state preservation. It does not prescribe one best chain strength for noisy hardware.<sup>[1](#b13-fn)</sup>
- **Critique.** Idealised model; on real hardware, too-strong chains compress the usable coefficient range.
- **Marginalia.**
  - `sampleset.md`: `chain_.` is the fraction of broken chains in each sample; log it with every QPU run.
  - `README.md`: The Embedding training run (Project ID 6dbabf04…) is where chains were viewed in D-Wave Inspector.
- **Scholia.** [B14](#b14): B14 finds the chains; B13 sets how strongly they are held. [B10](#b10): The topology decides how long the chains must be.
- **Footnote.** <a id="b13-fn"></a>¹ Part II (2011) covers designing hardware graphs; it is not cited here.
- **In context.** The theory behind the embedding training project and the `chain_.` column.

<a id="b14"></a>

### B14 · A practical heuristic for finding graph minors

> **Caption.** The algorithm behind minorminer.

**Metadata.** Jun Cai, William G. Macready, Aidan Roy (2014). *arXiv:1406.2741*. Preprint. [arxiv.org/abs/1406.2741](https://arxiv.org/abs/1406.2741). Verified 10 Nov 2026.<br>
**Descriptors.** Minor embedding · Software toolchain · **Tags.** `heuristic` `minorminer` `graph-minor` · **Labels.** `evidence:preprint` `role:tool` `type:preprint` `status:verified`

- **Abstract.** Presents a fast heuristic that finds minor embeddings of arbitrary problem graphs into hardware graphs by iteratively rerouting chains, without exhaustive search.
- **Gloss.** *Graph minor*: A graph obtained by contracting edges and deleting vertices of another.
- **Commentary.** The heuristic that turns a QUBO into a QPU job. *Elucidation:* It is the algorithm behind D-Wave's minorminer, which `EmbeddingComposite` calls when the code in this README sends a BQM to the QPU. *Exposition:* Place each variable, route paths to its neighbours, then repeatedly rip up and reroute overused qubits until chains are disjoint.
- **Exegesis.** Heuristic: it finds embeddings *often*, not always, and gives no optimality guarantee on chain length.<sup>[1](#b14-fn)</sup>
- **Critique.** Randomised; results vary run to run, so embeddings should be logged for reproducibility.
- **Marginalia.**
  - `README.md`: The 'Python code to process D-Wave output' block initialises a sampler and composite: that composite runs this heuristic.
  - `Maxindependentsetgraph.md`: It imports `EmbeddingComposite`, so the graph is embedded automatically before sampling.
- **Scholia.** [B13](#b13): Placement versus strength. [B10](#b10): The target graph it embeds into.
- **Footnote.** <a id="b14-fn"></a>¹ The heuristic is randomised, so save the embedding or its seed if you need to reproduce a run.
- **In context.** The practical side of the Embedding training project.

<a id="b10"></a>

### B10 · Next-Generation Topology of D-Wave Quantum Processors

> **Caption.** Pegasus: degree 15 instead of Chimera's 6, and what that means for chains.

**Metadata.** Kelly Boothby, Paul Bunyk, Jack Raymond, Aidan Roy (2020). *arXiv:2003.00133*. Preprint. [arxiv.org/abs/2003.00133](https://arxiv.org/abs/2003.00133). Verified 10 Nov 2026.<br>
**Descriptors.** Hardware topology · Minor embedding · **Tags.** `pegasus` `chimera` `connectivity` · **Labels.** `evidence:preprint` `role:hardware-context` `type:preprint` `status:verified`

- **Abstract.** Describes the Pegasus qubit-connectivity graph used in Advantage systems and evaluates how its higher degree shortens embedding chains compared with Chimera.
- **Gloss.** *Topology*: The hardware graph of which qubits can couple. *Degree*: Number of couplers per qubit.
- **Commentary.** A vendor description of the Pegasus qubit graph. *Elucidation:* It explains the hardware behind the 'Advantage_system 4.1' solver named in every Project ID section. *Exposition:* More couplers per qubit means fewer physical qubits per logical variable, which reduces chain breaks and frees capacity.
- **Exegesis.** States Pegasus nodes have nominal degree 15. It does not say every problem embeds better, nor address Advantage2's Zephyr topology.<sup>[1](#b10-fn)</sup>
- **Critique.** Preprint by vendor authors; embedding gains are measured on chosen benchmark families.
- **Marginalia.**
  - `README.md`: Solver: Advantage_system4.1 is a Pegasus-topology system. Record the topology with each run.
  - `Quantum_Engineering.md`: Engineering choices such as connectivity are what this paper documents.
- **Scholia.** [B13](#b13): Why connectivity shortens chains. [B9](#b9): Physics results from a processor with this kind of topology.
- **Footnote.** <a id="b10-fn"></a>¹ Advantage2 uses the later Zephyr topology, which this paper does not cover.
- **In context.** Hardware context for the QPU runs recorded here.

<a id="b9"></a>

### B9 · Quantum critical dynamics in a 5,000-qubit programmable spin glass

> **Caption.** Coherent critical dynamics at Advantage scale; still not an optimization advantage.

**Metadata.** Andrew D. King, Jack Raymond, Trevor Lanting, et al. (2023). *Nature 617(7959): 61–66*. Journal article. DOI: [10.1038/s41586-023-05867-2](https://doi.org/10.1038/s41586-023-05867-2). Verified 10 Nov 2026.<br>
**Descriptors.** Quantum dynamics · Quantum simulation · **Tags.** `spin-glass` `advantage-system` `coherence` · **Labels.** `evidence:peer-reviewed` `role:hardware-context` `type:journal-article` `status:verified`

- **Abstract.** Extends fast-anneal coherence tests to spin glasses on an Advantage processor with thousands of qubits, reporting agreement with quantum critical dynamics.
- **Gloss.** *Spin glass*: Disordered magnet with random couplings and many competing low-energy states.
- **Commentary.** Peer-reviewed physics on Advantage-class hardware. *Elucidation:* It shows what the hardware used in these exercises has demonstrated as a quantum simulator. That is a different question from how well it solves partitioning. *Exposition:* Measure how residual energy scales with sweep time and compare with quantum versus classical critical exponents.
- **Exegesis.** Claims *quantum critical dynamics in a programmable spin glass*. It does not claim faster solutions to practical scheduling.<sup>[1](#b9-fn)</sup>
- **Critique.** Comparison relies on specific classical models; critics argue other classical dynamics may mimic parts of the signal.
- **Marginalia.**
  - `Quantum_Engineering.md`: The 'device as experiment' theme, at 5,000-qubit scale.
  - `README.md`: Unrelated to the timing tables. It is about dynamics, not speed.
- **Scholia.** [B43](#b43): The rationale for building such devices. [B37](#b37): Computational value is a separate question.
- **Footnote.** <a id="b9-fn"></a>¹ The comparison relies on specific classical models of the dynamics, and critics have questioned some of them.
- **In context.** Background for `Quantum_Engineering.md`, not for solution speed.

<a id="b43"></a>

### B43 · Why quantum engineering?

> **Caption.** The rationale for building macroscopic quantum devices; already quoted in the D-Wave repo.

**Metadata.** A. M. Zagoskin (2010). *Low Temperature Physics 36(10): 911–914*. Journal article. DOI: [10.1063/1.3515522](https://doi.org/10.1063/1.3515522). Verified 10 Nov 2026.<br>
**Descriptors.** Quantum dynamics · Hardware topology · **Tags.** `quantum-engineering` `mesoscopic` `superconducting-qubits` · **Labels.** `evidence:peer-reviewed` `role:hardware-context` `type:journal-article` `status:verified`

- **Abstract.** A short perspective arguing that engineered macroscopic quantum structures built from solid-state qubits will matter beyond computing, offering a direct way to probe the quantum–classical boundary.
- **Gloss.** *Mesoscopic*: Between atomic and macroscopic scale, yet still quantum-coherent.
- **Commentary.** A short perspective on why macroscopic quantum devices are worth building. *Elucidation:* It is the paper `Quantum_Engineering.md` quotes three times. This entry gives it a full citation and a reading. *Exposition:* Fabricated qubits are large enough to engineer and small enough to stay quantum; that makes them both tools and test beds.
- **Exegesis.** A perspective piece; it *motivates* engineering research and makes no claim about D-Wave's devices or their performance.<sup>[1](#b43-fn)</sup>
- **Critique.** A four-page perspective from 2010. It predates the gate-model hardware race and today's annealers, so use it for the engineering argument only, not for any claim about current devices.
- **Marginalia.**
  - `Quantum_Engineering.md`: All three quotations match this record (Low Temp. Phys. 36(10): 911–914).
- **Scholia.** [B9](#b9): A concrete large device of the kind it anticipates. [B10](#b10): The engineering of one such device.
- **Footnote.** <a id="b43-fn"></a>¹ The citation in `Quantum_Engineering.md` matches Crossref exactly.
- **In context.** The source behind `Quantum_Engineering.md`.

<a id="b37"></a>

### B37 · What is the Computational Value of Finite-Range Tunneling?

> **Caption.** Big speedups over SA on crafted instances, and why that is not 'advantage'.

**Metadata.** Vasil S. Denchev, Sergio Boixo, Sergei V. Isakov, et al. (2016). *Physical Review X 6(3): 031015*. Journal article. DOI: [10.1103/PhysRevX.6.031015](https://doi.org/10.1103/PhysRevX.6.031015). Verified 10 Nov 2026.<br>
**Descriptors.** Benchmarking · Classical baselines · Quantum annealing · **Tags.** `weak-strong-clusters` `quantum-monte-carlo` `d-wave-2x` · **Labels.** `evidence:peer-reviewed` `role:caution` `type:journal-article` `status:verified` `claim:counterweight`

- **Abstract.** Designs problem instances with tall, narrow energy barriers ('weak-strong clusters') where tunnelling should help, and reports a D-Wave 2X running far faster than simulated annealing and quantum Monte Carlo on them, while noting other classical algorithms do not share SA's weakness.
- **Gloss.** *Finite-range tunnelling*: Tunnelling through barriers spanning a bounded number of spins (the clusters). *QMC*: Quantum Monte Carlo, a classical simulation of quantum annealing.
- **Commentary.** The standard lesson on crafted instances and baseline choice. *Elucidation:* If a training run here ever looks 'faster than classical', this paper shows what to ask: faster than which algorithm, on which instances? *Exposition:* If barriers are tall but thin, thermal hopping is slow and tunnelling is fast; build instances that isolate that regime and measure time-to-target.
- **Exegesis.** The large factor applies *to these crafted instances versus single-core SA and QMC*. The authors note that some other classical algorithms (for example cluster-aware large-neighbourhood search) do not suffer SA's slowdown, so no general advantage is claimed.<sup>[1](#b37-fn)</sup>
- **Critique.** Instances engineered for the effect; wall-clock comparisons across different hardware; D-Wave 2X generation.
- **Marginalia.**
  - `README.md`: The timing tables report QPU access time (about 26 ms per 100-read job). They are not a comparison with any classical solver.
  - `Test.py`: Despite the .py name it holds SQL tables for problem parameters. A comparison would need a matching table for classical runs.
- **Scholia.** [B36](#b36): The baseline that lost in this study. [B1](#b1): The method being tested.
- **Footnote.** <a id="b37-fn"></a>¹ Hardware: a D-Wave 2X processor; details are in the paper.
- **In context.** The caution behind 'no advantage claimed' in this section.

<a id="b16"></a>

### B16 · D-Wave Documentation

> **Caption.** The vendor manual for Ocean, Leap and solvers; living and versioned.

**Metadata.** D-Wave Quantum Inc. (2026). *Online documentation, accessed 10 November 2026*. Vendor documentation. [docs.dwavequantum.com/en/latest](https://docs.dwavequantum.com/en/latest/). Verified 10 Nov 2026.<br>
**Descriptors.** Software toolchain · QUBO formulation · **Tags.** `ocean` `leap` `bqm` `cqm` `dqm` `hybrid-solver` · **Labels.** `evidence:vendor-doc` `role:tool` `type:vendor-documentation` `status:verified`

- **Abstract.** Official documentation for D-Wave's Ocean SDK, Leap cloud and solvers, including BQM, CQM and DQM model types, samplers and hybrid solver usage.
- **Gloss.** *BQM / CQM / DQM*: Binary, constrained and discrete quadratic models. *Hybrid solver*: Cloud service mixing classical compute with QPU calls; not QPU capacity.
- **Commentary.** The vendor manual for Ocean, Leap and solvers. *Elucidation:* It is the reference for the Getting Started steps (`pip install dwave-ocean-sdk`, Leap) and for `DiscreteQuadraticModel` with `LeapHybridDQMSampler` in `Scheduling.md`. *Exposition:* Ocean separates *model* (dimod), *sampler* (local, QPU, hybrid) and *composites* (embedding, etc.), so one model can be run on many back ends.
- **Exegesis.** The docs describe what the software does; they are not independent evidence of performance, and vendor statements of capability stay vendor statements.<sup>[1](#b16-fn)</sup>
- **Critique.** Living resource; pin a version or access date when citing.
- **Marginalia.**
  - `Scheduling.md`: `LeapHybridDQMSampler` is a hybrid cloud solver and needs a Leap token. Without one the code cannot run.
  - `DQM.md`: The DQM workflow follows the docs' discrete-model guide.
  - `workforcedqm.md`: Same DQM pattern applied to workforce allocation.
- **Scholia.** [B17](#b17): The model library inside these docs. [B12](#b12): The docs' formulation guides echo B12's penalties.
- **Footnote.** <a id="b16-fn"></a>¹ A living resource, so cite it with an access date (here, 10 Nov 2026).
- **In context.** The reference for every Ocean call in this repository.

<a id="b17"></a>

### B17 · dimod: a shared API for QUBO/Ising samplers

> **Caption.** The model layer every Ocean workflow passes through.

**Metadata.** D-Wave Systems (2026). *Open-source software repository (GitHub)*. Software. [github.com/dwavesystems/dimod](https://github.com/dwavesystems/dimod). Verified 10 Nov 2026.<br>
**Descriptors.** Software toolchain · QUBO formulation · **Tags.** `dimod` `exactsolver` `sampleset` `bqm` · **Labels.** `evidence:software` `role:tool` `type:software` `status:verified`

- **Abstract.** The Ocean library defining binary and constrained quadratic models, the common sampler interface, the SampleSet result type and classical reference samplers such as ExactSolver.
- **Gloss.** *SampleSet*: Container of returned samples with energies and occurrence counts. *ExactSolver*: Brute-force classical sampler for tiny problems.
- **Commentary.** The model layer every Ocean workflow passes through. *Elucidation:* The `num_oc.` column in `sampleset.md` comes from dimod's SampleSet: it counts how often a sample occurred, not the probability of any real-world outcome. *Exposition:* Build a BQM from linear and quadratic biases, call `sampler.sample(bqm)`, and read a SampleSet; the same code runs on any sampler.
- **Exegesis.** dimod defines *interfaces*; it makes no claim about which sampler is best.<sup>[1](#b17-fn)</sup>
- **Critique.** Fast-moving API; pin versions in notebooks.
- **Marginalia.**
  - `ExactSolver`: This file actually uses `dwavebinarycsp` with dimod. `ExactSolver` itself is a classical brute-force reference.
  - `sampleset.md`: Read `energy` and `num_oc.` as SampleSet fields.
  - `README.md`: The 'Create an empty Binary Quadratic Model' snippet is the dimod API.
- **Scholia.** [B12](#b12): Where the Q matrices come from. [B36](#b36): dimod's companion samplers include a classical SA reference.
- **Footnote.** <a id="b17-fn"></a>¹ dimod is open source (Apache-2.0) under dwavesystems on GitHub.
- **In context.** The library behind the BQM snippets, the `ExactSolver` file and `sampleset.md`.

### Code annotations in this repository

Where the four code-annotation elements appear in this repository's own files.<sup>[E3](#en3)</sup>

| Element | Example in this repository |
| --- | --- |
| Code comment | `README.md` snippets: `# Create an empty Binary Quadratic Model`, `# Define QUBO interactions (Example values)`; `Test.py`: `-- CREATE TABLE to store the problem parameters` |
| Docstring | None in this repository; the code lives in Markdown snippets. A docstring would sit on the first line of a function such as a QUBO builder |
| Directive | The ` ```math ` fences in the Project ID sections tell GitHub to render LaTeX; ` ```python ` info strings set syntax highlighting |
| Decorator | None used here. Ocean's API is plain function and class calls |

<a id="excursus"></a>

### Excursus: From a QUBO on paper to a sample set: what each run here measured

Each Project ID section follows the same chain. A problem is written as a QUBO with penalties ([B11](#b11), [B12](#b12)). dimod holds it as a BQM ([B17](#b17)). A heuristic embeds it into chains on the Pegasus graph ([B14](#b14), [B10](#b10)), the chain strength holds each chain together ([B13](#b13)), and the QPU anneals it 100 times ([B1](#b1)). The timing tables then split the job into parts. In Project ID cd24acdf…, the QPU access time was 26.484 ms. Of that, programming took 15.756 ms, and sampling 100 reads took 10.728 ms (20 µs anneal, 67 µs readout and 21 µs delay per read). Most of the access time is set-up and readout, not annealing. That is normal for small jobs, and it is one reason a fair comparison with a classical solver such as simulated annealing ([B36](#b36)) has to define its clock carefully ([B37](#b37)). The energies in the sample sets measure the encoding: −9826.5 is a value of the partitioning QUBO, and the occurrence counts are sampler frequencies.

### Endnotes

1. <a id="en1"></a>**Verification.** Every source was checked on 10 November 2026 (America/New_York). DOIs were resolved at doi.org and matched against Crossref; preprints were checked on arXiv, the patent on Google Patents, and documentation and course pages on the live page.
2. <a id="en2"></a>**Numbering.** B-numbers are stable identifiers shared across David Merwin's annotated bibliographies, so a source keeps the same number in every repository. Gaps in the numbering are expected.
3. <a id="en3"></a>**Scope.** Sources are cited for background and method. None is used to claim a quantum advantage. The code-annotation table describes files as they are; no code was changed.

### P.S.

P.S. The QPU runs above are D-Wave training exercises. Their value is in the logged details: solver, reads, timing, energies and occurrences. Keep logging those, and add a matching classical run next time.
