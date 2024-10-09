# Testing the ohms_law_jh Package

## Installation

1. Install the package using pip:
   ```
   pip install ohms-law-jh
   ```

## Running the Tests

1. Save the provided `test_ohms_law.py` script to your computer
2. Open a terminal or command prompt
3. Navigate to the directory containing the test script
4. Run:
   ```
   python test_ohms_law.py
   ```

## Expected Output

You should see output similar to:
```
Testing standalone functions:
Voltage: 2A × 5Ω = 10V
Current: 10V ÷ 2Ω = 5A
Resistance: 12V ÷ 3A = 4Ω

Testing Drive class methods:
Voltage: 2A × 5Ω = 10V
Current: 10V ÷ 2Ω = 5A
Resistance: 12V ÷ 3A = 4Ω
```

## Package Usage

The package provides both standalone functions and a `Drive` class:

### Standalone Functions
```python
from ohms_law_jh import calcVoltage, calcCurrent, calcResistance

voltage = calcVoltage(current, resistance)
current = calcCurrent(voltage, resistance)
resistance = calcResistance(voltage, current)
```

### Using the Drive Class
```python
from ohms_law_jh import Drive

ohm = Drive()
voltage = ohm.calcVoltage(current, resistance)
current = ohm.calcCurrent(voltage, resistance)
resistance = ohm.calcResistance(voltage, current)
```

# Example
![Example of the terminal](/example.png)