![](https://cdn.mathpix.com/snip/images/jjJdYdS-P8NhH-1f1QBBxB_rB7j71M6e2n1IPSVaOZM.original.fullsize.png)

To address the scheduling problem for the 4 employees and 4 shifts based on their preferences, you can use a Discrete Quadratic Model (DQM) to find the optimal assignment. 

### Python3 Code for D-Wave DQM

```python
from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler

# Initialize DQM object
dqm = DiscreteQuadraticModel()

# Employee names and their shift preferences
employees = {
    "Anna": [1, 2, 3, 4],
    "Bill": [3, 2, 1, 4],
    "Chris": [4, 2, 3, 1],
    "Diane": [4, 1, 2, 3]
}

# Number of shifts
num_shifts = 4

# Add variables and preferences
for name, prefs in employees.items():
    dqm.add_variable(num_shifts, label=name)
    dqm.set_linear(name, prefs)

# Quadratic terms to enforce one shift per employee
for name1 in employees:
    for name2 in employees:
        if name1 != name2:
            biases = {(i, j): 1 for i in range(num_shifts) for j in range(num_shifts)}
            dqm.set_quadratic(name1, name2, biases)

# Sample
sampler = LeapHybridDQMSampler()
sampleset = sampler.sample_dqm(dqm)
best_solution = sampleset.first.sample

# Show best shift assignment
for name, shift in best_solution.items():
    print(f"{name} is assigned to shift {shift+1}")
```

### Mathematical Equation

![](https://cdn.mathpix.com/snip/images/a6oMcuFu2sPFyF2fQyNvbQ1kn6JEHfLqJa21M27Jx-o.original.fullsize.png)

The optimization problem can be mathematically expressed as:

\[
\min \sum_{i \in \text{employees}} \text{prefs}_i(x_i) + \lambda \sum_{i \neq j} \delta(x_i, x_j)
\]

Where \( \text{prefs}_i(x_i) \) is the preference of employee \( i \) for shift \( x_i \), and \( \delta(x_i, x_j) \) is the Kronecker delta function that penalizes if employees \( i \) and \( j \) are assigned the same shift. The parameter \( \lambda \) balances the importance of the penalty term.

This code should output the best assignment of employees to shifts according to their preferences.


--------

### Python3 Code for D-Wave DQM

#### 1. Initialize the DQM Object
```python
from dimod import DiscreteQuadraticModel

# Initialize DQM object
dqm = DiscreteQuadraticModel()
```

#### 2. Add Variables with Cases
In our case, each employee can take one of the four shifts. Therefore, each variable (employee) will have four cases (shifts).

```python
# Employee names
employee_names = ["Anna", "Bill", "Chris", "Diane"]

# Number of shifts
num_shifts = 4

# Add variables
for name in employee_names:
    dqm.add_variable(num_shifts, label=name)
```

#### 3. Add Linear Biases (Preferences)
Linear biases represent the preferences each employee has for each shift. The lower the value, the more preferable the shift is for the employee.

```python
# Employee preferences for each shift
employee_preferences = {
    "Anna": [1, 2, 3, 4],
    "Bill": [3, 2, 1, 4],
    "Chris": [4, 2, 3, 1],
    "Diane": [4, 1, 2, 3]
}

# Add linear biases based on preferences
for name, prefs in employee_preferences.items():
    dqm.set_linear(name, prefs)
```

### Mathematical Expression
![](https://cdn.mathpix.com/snip/images/xDjTjm8bJqf5frX6vaHRWbrBJePkWxWiP_nTW2YlbfY.original.fullsize.png)

For adding the linear biases, the mathematical expression can be considered as:

\[
E(\text{shift}) = \sum_{i \in \text{Employees}} \text{Preference}_{i}(\text{shift})
\]

where \( \text{Preference}_{i}(\text{shift}) \) is the preference score for employee \( i \) for a particular shift. We try to minimize \( E \) to get the optimal schedule.

Combine these steps to create a full DQM model for solving your employee scheduling problem. After these steps, you would usually add the quadratic terms and then sample the DQM to find the optimal assignment.
