from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt
import math


class QRNG:
    def __init__(self, backend="statevector_simulator", api_token=None):
        self.backend = backend
        self.api_token = api_token
        self.real_device = True if api_token is not None else False

    def integer_between(self, bottom, top, do_plots=False, do_prints=False):
        # Determine the number of qubits needed. The number of qubits (n_qubits) is calculated to ensure that the
        # largest number in the range can be represented. This is done by finding the smallest power of 2 that is
        # greater than or equal to the size of the range (top - bottom + 1). The formula log2(top - bottom + 1) gives
        # the exact number of bits needed, and math.ceil ensures it's rounded up to the nearest whole number if it's
        # not an integer.
        n_qubits = math.ceil(math.log2(top - bottom + 1))
        if do_prints:
            print(f"Number of qubits used: {n_qubits}")

        # Create a quantum circuit with n_qubits qubits and classical bits. n_qubits qubits are needed to store the
        # quantum state, and n_qubits classical bits are used to store the measurement results.
        circuit = QuantumCircuit(n_qubits, n_qubits)

        # Apply Hadamard gates (H-gates) to each qubit to create superposition. A Hadamard gate puts a qubit in a
        # state where it has equal probability of being measured as 0 or 1, creating a superposition of |0⟩ and |1⟩.
        # Applying it to all qubits results in a superposition of all possible states (i.e., all possible
        # combinations of 0s and 1s), which is essential for generating a random number.
        circuit.h(range(n_qubits))

        # Measure all the qubits. Measurement collapses each qubit's superposition to either 0 or 1 randomly,
        # resulting in a random bit string. This bit string is then stored in the classical bits of the circuit.
        circuit.measure(range(n_qubits), range(n_qubits))

        # Display the circuit
        if do_prints:
            print("\nQuantum Circuit:")
            print(circuit)
        if do_plots:
            circuit.draw(output='mpl')
            plt.show()

        if self.real_device:
            # Execute the circuit using the IBM Quantum Runtime Service. This service runs the circuit on a real
            # quantum computer. Enable your IBMQ account with the API token
            api_token = self.api_token or exit()
            IBMQ.enable_account(api_token)
            provider = IBMQ.get_provider(hub='ibm-q')

            # Choose a backend
            backend = provider.get_backend('ibm_brisbane')  # Example backend

            # Execute the circuit on the chosen backend
            job = execute(circuit, backend=backend, shots=1)
            result = job.result()
            counts = result.get_counts(circuit)

            IBMQ.disable_account()  # Disable your IBMQ account
        else:
            # Execute the circuit using the QASM (Quantum Assembly Language) simulator. This simulator mimics the
            # behavior of a real quantum computer. 'shots=1' means the experiment (i.e., the generation of a random
            # number) is performed only once.
            simulator = Aer.get_backend(self.backend)
            result = execute(circuit, simulator, shots=1).result()
            counts = result.get_counts(circuit)
            if self.backend == "statevector_simulator" and do_plots:
                state = result.get_statevector()
                plot_bloch_multivector(state)
                plt.show()

        # Plot the measurement results
        if do_plots:
            plot_histogram(counts)
            plt.show()

        # Convert the measured bit string to an integer. The bit string represents a binary number,
        # and 'int(measured_str, 2)' converts it from binary to decimal.
        measured_str = list(counts.keys())[0]
        measured_int = int(measured_str, 2)
        if do_prints:
            print(f"Measured Bit String: {measured_str}")
            print(f"Measured Integer (0 to {2 ** n_qubits - 1}): {measured_int}")

        # Adjust the measured integer to the desired range. The modulus operation ensures the integer fits within the
        # size of the range (top - bottom + 1), and adding 'bottom' shifts this range to start from 'bottom' instead
        # of 0.
        random_number = bottom + (measured_int % (top - bottom + 1))
        if do_prints:
            print(f"Random Number in the range [{bottom}, {top}]: {random_number}")

        return random_number

    def integer_batch(self, bottom, top, batch_size=1, do_plots=False, do_prints=False):
        batch = []
        for i in range(batch_size):
            batch.append(self.integer_between(bottom, top, do_plots, do_prints))

        return batch

    def float_between(self, bottom, top, precision=2, do_plots=False, do_prints=False):
        # Scale the float range to an integer range based on the precision
        scale = 10 ** precision
        int_bottom = int(bottom * scale)
        int_top = int(top * scale)

        # Generate a random integer in the scaled range
        random_int = self.integer_between(int_bottom, int_top, do_plots, do_prints)

        # Convert the integer back to a float
        random_float = random_int / scale
        return random_float

    def float_batch(self, bottom, top, precision=2, batch_size=1, do_plots=False, do_prints=False):
        batch = []
        for i in range(batch_size):
            batch.append(self.float_between(bottom, top, precision, do_plots, do_prints))

        return batch

    def ascii_random(self, include_uppercase=False, do_plots=False, do_prints=False):
        if include_uppercase:
            # Range for both uppercase and lowercase letters, skipping non-alphabetic characters
            bottom, top = 65, 122
        else:
            # Range for lowercase letters only
            bottom, top = 97, 122

        # Generate a random integer in the range
        ascii_val = self.integer_between(bottom, top, do_plots, do_prints)

        # Skip non-alphabetic characters if uppercase is included
        if include_uppercase and 90 < ascii_val < 97:
            ascii_val += 6

        # Convert the ASCII value to a character
        return chr(ascii_val)

    def ascii_random_batch(self, batch_size=1, include_uppercase=False, do_plots=False, do_prints=False):
        batch = []
        for i in range(batch_size):
            batch.append(self.ascii_random(include_uppercase, do_plots, do_prints))

        return batch

    def string_random(self, length, include_uppercase=False, do_plots=False, do_prints=False):
        string = ""
        for i in range(length):
            string += self.ascii_random(include_uppercase, do_plots, do_prints)

        return string

    def string_random_batch(self, length, include_uppercase=False, batch_size=1, do_plots=False, do_prints=False):
        batch = []
        for i in range(batch_size):
            batch.append(self.string_random(length, include_uppercase, do_plots, do_prints))

        return batch
