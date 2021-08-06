from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
circuit=QuantumCircuit(2,2)
circuit.x(0)
simulator=Aer.get_backend('statevector_simulator')
result=execute(circuit,backend=simulator).result()
sv=result.get_statevector()
print(sv)
%matplotlib inline
circuit.draw(output='mpl')
