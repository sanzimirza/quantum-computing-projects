from qiskit import QuantumCircuit
from qiskit_aer import Aer

qc = QuantumCircuit(2,2)
qc.h([0,1])
qc.cz(0,1)
#this will put a -1 phase on the 11 because that is the correct answer
#this a controlled Z operator. it does not use square brackets. control means Z gate only acts 
#if the control qubit is one. Z gate means phase will switch to -1 of the qubit ONLY IF the qubit is 1.

#Diffuser(inversion about the mean)
qc.h([0,1])
qc.x([0,1])
qc.cz(0,1)
qc.x([0,1])
qc.h([0,1])

qc.measure([0,1],[0,1])

backend = Aer.get_backend("aer_simulator")
job = backend.run(qc, shots = 100)

result = job.result()
print(result.get_counts())

print(qc)