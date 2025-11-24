from qiskit import QuantumCircuit
from qiskit_aer import Aer

qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure(0,0)
qc.measure(1,1)
backend = Aer.get_backend("aer_simulator")
# run using .run(), not execute()
job = backend.run(qc, shots=1000)
result = job.result()
print(result.get_counts())
