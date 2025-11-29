from qiskit import QuantumCircuit
from qiskit_aer import Aer

qc = QuantumCircuit(1,1)
qc.h(0) 
qc.s(0)
qc.h(0)

qc.measure(0,0)

backend = Aer.get_backend("aer_simulator")
job = backend.run(qc, shots = 100)

result = job.result()
print(result.get_counts())

print(qc)