# D-Wave-Systems-Training-Projects

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


## Table of Contents
- [Project Details](#project-details)
- [Problem Parameters and Solution Timing](#problem-parameters-and-solution-timing)
- [QPU Analytics](#qpu-analytics)
- [Installation and Usage](#installation-and-usage)
- [License](#license)

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
Creating a professional GitHub portfolio involves not only showcasing your code and projects but also making it easy for others to understand the significance and methodology of your work. Given your interest in D-Wave Systems and quantum computing, you can use Markdown to create an organized and visually appealing portfolio. Below is an example Markdown text to add to your `README.md` or project-specific `README.md` file on GitHub.

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


---

## Contact Information

- **Email**: davidmerwin1992@gmail.com
- **LinkedIn**: 
  
Feel free to reach out if you have any questions or would like to collaborate!
