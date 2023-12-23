from qrng import QRNG

instance = QRNG(backend="qasm_simulator")

# OR instance = QRNG(backend="statevector_simulator") by default

# Example usage: generate a random integer between 5 and 10
random_number = instance.integer_between(0, 100, do_prints=True, do_plots=True)
print("Random number:", random_number)

# Example usage: generate a batch of 100 random integers between 5 and 100
batch = instance.integer_batch(5, 100, 100)
print("Batch:", batch)

# Example usage: generate a random float between 0.0 and 1.0 with 4 decimal places
random_float = instance.float_between(0.0, 1.0, 4)
print("Random float:", random_float)

# Example usage: generate a batch of 100 random floats between 0.0 and 1.0 with 4 decimal places
batch = instance.float_batch(0.0, 1.0, 4, 100)
print("Batch:", batch)

# Example usage: generate a random ASCII character
random_char = instance.ascii_random()
print("Random character:", random_char)

# Example usage: generate a batch of 100 random ASCII characters
batch = instance.ascii_random_batch(batch_size=100)
print("Batch:", batch)

# Example usage: generate a random string of length 3
random_string = instance.string_random(3, include_uppercase=True)
print("Random string:", random_string)

# Example usage: generate a batch of 10 random strings of length 16
batch = instance.string_random_batch(16, include_uppercase=True, batch_size=10)
print("Batch:", batch)
