# QRNG - Quantum Random Number Generator

QRNG is a Python module that leverages quantum computing to generate random numbers. This module uses Qiskit to interface with quantum simulators or quantum computers, providing various functions to generate random integers, floats, ASCII characters, and strings.

Note, due to current limitations of quantum, running this module on a real quantum computer will be slower than a classical computer. However, this module is intended to be used for educational purposes, and to demonstrate the potential of quantum computing.
For reference, a single random integer between 0 and 100 takes approximately 36 minutes to generate on a real quantum computer due to queue times.

## Features

- Generate random integers within a specified range.
- Generate random floating-point numbers with specified precision.
- Generate random ASCII characters and strings.
- Batch generation for all types of random values.
- Option to choose between different quantum backends, including simulators and real quantum hardware.

## Installation

To install QRNG, ensure you have Python and pip installed on your system. Then run the following command:

```bash
pip install qrng
```

Make sure you also have Qiskit installed:
```bash
pip install qiskit
```

## Usage

Import the `QRNG` class from the `qrng` module and create an instance. You can specify the backend used for quantum computations.

### Basic Usage
```python
from qrng import QRNG

# Initialize the QRNG instance
instance = QRNG(backend="qasm_simulator")

# Generate a random integer between 0 and 100
random_number = instance.integer_between(0, 100, do_prints=True, do_plots=True)
print("Random number:", random_number)
```

### Batch Generation

```python
# Generate a batch of 100 random integers between 5 and 100
batch = instance.integer_batch(5, 100, 100)
print("Batch:", batch)
```

### Floating-Point Numbers

```python
# Generate a random float between 0.0 and 1.0 with 4 decimal places
random_float = instance.float_between(0.0, 1.0, 4)
print("Random float:", random_float)
```

### ASCII Characters
```python
# Generate a random ASCII character, including uppercase
random_char = instance.ascii_random(include_uppercase=True)
print("Random character:", random_char)
```

### Strings
```python
# Generate a random string of length 3, including uppercase
random_string = instance.string_random(3, include_uppercase=True)
print("Random string:", random_string)
```

## Documentation

For more information, please refer to the [documentation](documentation.md).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[//]: # (implement some sort of license that is open source requires attribution in derivative works)

## License  
[MIT License](license.md)