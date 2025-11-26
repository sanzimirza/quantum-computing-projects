from qiskit import QuantumCircuit
from qiskit_aer import Aer

qc = QuantumCircuit(3,3)
qc.h(0)
qc.cx(0,1)
qc.cx(0,2)

qc.measure(0,0)
qc.measure(1,1)
qc.measure(2,2)

backend = Aer.get_backend("aer_simulator")
job = backend.run(qc, shots=100)

result = job.result()
print(result.get_counts())

print(qc)