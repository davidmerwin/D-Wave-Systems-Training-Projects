# D-Wave-Systems-Training-Projects

Table of Contents
1. Overview
2. Getting Started
3. D-Wave Tools and Technologies
4. Project Summaries
- Older Projects
- Newer Projects
5. Contact Information
  
## Project Directory Structure
    .
    ├── README.md
    ├── code
    │   └── number_partitioning.py
    ├── data
    │   └── training_number_partitioning.json
    ├── math_equations
    │   └── equations.md
    ├── results
    │   └── sampling_time_analysis.md
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


## Projects and Studies during the Training

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








## Contact Information

- **Email**: davidmerwin1992@gmail.com
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/your-profile)
  
Feel free to reach out if you have any questions or would like to collaborate!
