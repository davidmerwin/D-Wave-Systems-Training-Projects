![](https://cdn.mathpix.com/snip/images/ZJDWGBlZD5vQIomx1ALyOCrrBk6R1L1Qxk2U8zJmVok.original.fullsize.png)

## D-Wave Systems Quantum Computing Project
### Workforce Optimization with DQM

#### Table of Contents
1. [Objective](#objective)
2. [DQM Implementation](#dqm-implementation)

#### Objective
Optimizing workforce distribution using Discrete Quadratic Models (DQM) on D-Wave Systems.

#### DQM Implementation

##### Initialize DQM Object
```python
from dimod import DiscreteQuadraticModel
dqm = DiscreteQuadraticModel()
```

##### Add Variables for Employees
```python
for name in employees:
    dqm.add_variable(num_shifts, label=name)
```

##### Set Employee Preferences
```python
dqm.set_linear("Anna", [1,2,3,4])
dqm.set_linear("Bill", [3,2,1,4])
dqm.set_linear("Chris", [4,2,3,1])
dqm.set_linear("Diane", [4,1,2,3])
```

##### Run
```bash
python main.py
```


![](https://cdn.mathpix.com/snip/images/QZIP4DAWqABcVZeKBioHxrDOtcvZ5bhO2hlvYw9evJs.original.fullsize.png)
