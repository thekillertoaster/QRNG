# QRNG - Quantum Random Number Generator

## Documentation is a ***WIP*** and may not represent the correct state of the project

The `QRNG` class is a Python module for generating random numbers using quantum computing principles. It leverages Qiskit to interface with IBM's quantum simulators and real quantum computers. The class offers a variety of methods to generate random integers, floats, ASCII characters, and strings.

## Initialization

The class is initialized with the following parameters:

- `backend`: Specifies the quantum backend to use. Default is `"statevector_simulator"`.
- `api_token`: Optional. Required if using a real quantum device. (will use a real device if `api_token` is specified)

```python
instance = QRNG(backend="qasm_simulator", api_token="your_api_token")
```

## Methods

### integer_between

Generates a random integer between two specified values.

```python
random_number = instance.integer_between(0, 100, do_prints=False, do_plots=False)
```

- `bottom`: Lower bound of the range (inclusive).
- `top`: Upper bound of the range (inclusive).
- `do_plots`: If True, plots the quantum circuit and measurement results.
- `do_prints`: If True, prints details about the quantum circuit and random number.

### integer_batch

Generates a batch of random integers between two specified values.

```python
batch = instance.integer_batch(0, 10, batch_size=10, do_plots=False, do_prints=False)
```

- `batch_size`: Number of random integers to generate.

### float_between

Generates a random floating-point number between two specified values and with a specified precision.

```python
batch = instance.float_batch(0.0, 1.0, precision=4, batch_size=10, do_plots=False, do_prints=False)
