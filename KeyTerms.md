| Constraint | Penalty Function |
| :---: | :---: |
| $x+y \leq 1$ | $x \cdot y$ |
| $x+y \geq 1$ | $1-x-y+x \cdot y$ |
| $x+y=1$ | $1-x-y+2 \cdot x \cdot y$ |
| $x \leq y$ | $x-x \cdot y$ |
| $x+y+z \leq 1$ | $x \cdot y+x \cdot z+y \cdot z$ |
| $x=y$ | $x+y-2 \cdot x \cdot y$ |

| Concepts | Related terms |
| :--- | :--- |
| Binary Quadratic Models | BQM, Ising, QUBO |
| $\begin{array}{l}\text { Constrained Quadratic } \\\text { Models }\end{array}$ | CQM, constrained quadratic model |
| Constraint Satisfaction | CSP, binary CSP |
| Discrete Quadratic Models | DQM, discrete quadratic model |
| Hybrid | quantum-classical hybrid, Leap's hybrid solvers, hybrid workflows |
| Minor-Embedding | $\begin{array}{l}\text { embedding, mapping logical variables to physical qubits, chains, chain } \\\text { strength }\end{array}$ |
| Penalty Models | Penalty Models |
| Quadratic Models | Quadratic Models |
| QPU Topology | Chimera, Pegasus |
| Samplers and Composites | solver |
| Solutions | samples, sampleset, probabilistic, energy |
| Variables | binary, discrete, integer, real variables |

![](https://cdn.mathpix.com/snip/images/6rhvLXInhSUSMWKbSvY84FCHr65yN5Nx5krDVUEATaU.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/dKdCMBzcgnHFy0Hy9cwK5yJQGIu1TRQ8Ie9W6JEY4lk.original.fullsize.png)


binary quadratic model
BQM
A collection of binary-valued variables (variables that can be assigned two values, for example $-1,1$ ) with associated linear and quadratic biases. Sometimes referred to in other tools as a problem. See a fuller description under Binary Quadratic Models.
![](https://cdn.mathpix.com/snip/images/Gr2COh1oXvVwsMV00dryv7Li8eSWCFFqLz5J3IoRM5k.original.fullsize.png)


Chain
One or more nodes or qubits in a target graph that represent a single variable in the source graph. See embedding. See a fuller description under Minor-Embedding.Chain and Minor-Embedding
In the context of quantum computing, particularly with D-Wave systems, a chain refers to a collection of physical qubits on the quantum processing unit (QPU) that together represent a single logical variable from the problem being solved. Minor-embedding is the process of mapping these logical variables to these chains on the QPU.

![](https://cdn.mathpix.com/snip/images/PAbSFJqPhsWRG5sPYekkogeLag8rWgrdxjVvvFsSunY.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/tpERuvvFfTL56KAjpM-NjFOLtcMQQcifJTkUhPtV3yo.original.fullsize.png)

Chain length
The number of qubits in a Chain. See a fuller description under Minor-Embedding.Chain length refers to the number of physical qubits in a chain that represents a single logical variable in your problem formulation.
![](https://cdn.mathpix.com/snip/images/nKn6H_h_dSrPfqi0V7HZjKu7-dQVJYBYkzbttM8Qm9I.original.fullsize.png)


Chain strength
Magnitude of the negative quadratic bias applied between variables to form a chain. See a fuller description under Minor-Embedding. Chain strength refers to the magnitude of the negative quadratic bias applied between qubits in a chain to enforce that they take on the same value during the quantum annealing process.
![](https://cdn.mathpix.com/snip/images/BXIRjxV4pv0-mS6ZeiG_9QeOf-yYKbGvN6v2lJ0rfOM.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/nasxqGdeEDCaRdWT8fVp53eHI-HzCWklvx4kSfAQQeE.original.fullsize.png)

Chimera
A D-Wave QPU is a lattice of interconnected qubits. While some qubits connect to others via couplers, D-Wave QPUs are not fully connected. For D-Wave 2000Q QPUs, the qubits interconnect in an architecture known as Chimera. See a fuller description under QPU Topology. See also Pegasus and Zephyr. The Chimera topology is one of the qubit interconnection architectures featured in D-Wave systems, specifically in the D-Wave 2000 Q QPUs. 
![](https://cdn.mathpix.com/snip/images/KHZjhN02btUZ6pxSsbMenZecG3S6xya1x3GFThFXPBQ.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/gJ4HdzI64wXt9AaO8h9T4NE0NESlp5heL2Wi11u6z9I.original.fullsize.png)



![](https://cdn.mathpix.com/snip/images/qJgp0OmENwRO9Ewr5C3yiZwmYRjHclSl120YFJZymOU.original.fullsize.png)
The Hamiltonian is the heart of the problem description in quantum systems, encapsulating the energy of the system in terms of its state variables and interactions. D-Wave systems are designed to solve optimization and sampling problems by minimizing a particular Hamiltonian.
![](https://cdn.mathpix.com/snip/images/eTGNycnNU63XHcu5_j8xJCV8E4ID8VGU1z6qsWWlgs0.original.fullsize.png)


![](https://cdn.mathpix.com/snip/images/TMKMxhYMEf_uXsgvjuDjLXpe6Pzdb2gvmUZ9eiM6dtk.original.fullsize.png)


![](https://cdn.mathpix.com/snip/images/O-tVyd5eokUwFnVlwNp_TOuEmDgBmQ2pdXqSgxTREwg.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/DOTWENG9OEiX17zW-mzwEX-CMnLyaLzSFhktsnf1TlY.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/vpXzyFY8G6YDGcN1FzgFB3fjmCtG7RUp-dZUb3PatNs.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/hYj1GGrWw0APiS-BvODeb11mYYLzIFP7Nq1J7M362BA.original.fullsize.png)

Objective function
A mathematical expression of the energy of a system as a function of binary variables representing the qubits.
![](https://cdn.mathpix.com/snip/images/4vyz7pRyOcaW6wnGK-Y3P2Iyx7ZYqryQNhFvADCw3PU.original.fullsize.png)

-------------------------
Math


