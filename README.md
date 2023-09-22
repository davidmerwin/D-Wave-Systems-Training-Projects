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



## Contact Information

- **Email**: davidmerwin1992@gmail.com
- **LinkedIn**: 
  
Feel free to reach out if you have any questions or would like to collaborate!
