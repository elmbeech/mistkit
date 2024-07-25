# Mistkit {&#x25BE;&#x25B4;&#x2726;&#x25C7;&#x25AE;&#x25AD;&#x25A0;&#x25CF;}


## Abstract:

In the book "Q is for quantum" Terry Rudolph describes a formalismen with white balls (|0>) and black balls (|1>), termend [misty state](https://youtu.be/vqave0V5qAA) to teach quantum computing  and quantum theory to folks with only a basic knowledge of arithmetic.
The formalismen was for teaching adapted and further developed by Sophia Economou, Edwin Barnes, Adrian German, Marcelo Pias, and Qiao Xiang.

+ https://www.qisforquantum.org/
+ https://arxiv.org/abs/2005.07874  # Economou, Rudolph, Barnes 2020
+ https://arxiv.org/abs/2210.02868  # Economou, Barnes 2022
+ https://dl.acm.org/doi/10.1145/3626253.3633435  # German, Pias, Xiang 2024

Industrial Busines Machine developed a popular, Python based, open source software stack for quantum computing; qiskit.

+ https://en.wikipedia.org/wiki/Qiskit
+ https://docs.quantum.ibm.com/
+ https://github.com/Qiskit/qiskit
+ https://www.ibm.com/quantum/qiskit

Mistkit adds to the Qikit's state\_drawer function the possibility to output Statevectors in misty state formalism, along all it's other possibility to output Statevectors (text, latex, latex\_source, qsphere, hinton, bloch, city, paulivec).


## Header:
+ Language: python [>= 3.8](https://devguide.python.org/versions/)              
+ Library dependencies: numpy, qiskit
+ Date: 2024-07  
+ License: [Apache 2.0](https://en.wikipedia.org/wiki/Apache_License)           
+ Author: Elmar Bucher
+ User manual: this README.md file                                              
+ Source code: [https://github.com/elmbeech/mistkit](https://github.com/elmbeech/mistkit)
+ Inspiration: Dan Adrian German's CSCI A590 quantum computing class at [Indiana University](https://www.iu.edu/index.html).


## HowTo Guide:

1. Install or update to the latest mistkit version:
```bash
pip install -U mistkit
```

1. Load mistkit:
```python
import mistkit
```

1. Run minimal example:
```python
# load libraries
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import pylatex
import mistkit

# generate 8[qubit] quantum circuit
qc = QuantumCircuit(8)
qc.x([0,1,3,5,6,7])  # state 0b11101011
qc.draw()

# read out the quantum circuit state vector
sv = Statevector.from_instruction(qc)
print(sv.data)  # numpy state vector array.
print(sv.draw('mist'))  # state vector in Terry Rudolph's misty state notation.
sv.draw('latex')  # state vector in Paul Dirac's ket notation.
```

1. Uninstall mistkit:
```bash
pip uninstall mistkit
```


## Refernce Manual:

1. Read the [docstrings](https://en.wikipedia.org/wiki/Docstring):
```python
import mistkit
from qiskit import visualization

help(mistkit.state_to_mist)
help(visualization.state_visualization.state_drawer)
help(mistkit.mistify)
```


## Tutorial:

+  [man/misty_bell_states.ipynb](https://github.com/elmbeech/mistkit/man/misty_bell_states.ipynb)


## Discussion:
To be developed.


## About Documentation:                                                         
Within the mistkit library, we tried to stick to the documentation policy laid out by Daniele Procida in his "[what nobody tells you about documentation](https://www.youtube.com/watch?v=azf6yzuJt54)" talk at PyCon 2017 in Portland, Oregon.


## Cite:
+ ~


## Road Map:
+ ~


## Release Note:

+ version 0.0.0 miskit rises from the ashes.

All we know is falling.
