# Mistkit {&#x25BE;&#x25B4;&#x2726;&#x25C7;&#x25AE;&#x25AD;&#x25A0;&#x25CF;}


## Abstract:

In the book "[Q is for quantum](https://www.qisforquantum.org/)", Terry Rudolph describes a formalism with white balls <span style="white-space: nowrap;">(|0>)</span> and black balls <span style="white-space: nowrap;">(|1>)</span>, termed [misty state](https://youtu.be/vqave0V5qAA), to teach quantum theory and quantum computing to folks with only a basic knowledge of arithmetic.

This formalism was for teaching adapted and further developed, amongst others, by Adrian German, Edwin Barnes, Marcelo Pias, Qiao Xiang, and Sophia Economou.

+ https://arxiv.org/abs/2005.07874  # Economou, Rudolph, Barnes 2020
+ https://arxiv.org/abs/2210.02868  # Economou, Barnes 2022
+ https://dl.acm.org/doi/10.1145/3626253.3633435  # German, Pias, Xiang 2024

For quantum computing, International Business Machines developed [Qiskit](https://en.wikipedia.org/wiki/Qiskit), a popular, [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) based, free and open-source software stack.

+ https://docs.quantum.ibm.com/
+ https://github.com/Qiskit/qiskit
+ https://www.ibm.com/quantum/qiskit

All what **Mistkit** does is adding to Qiskit's state\_drawer function the possibility to output Statevectors in *misty state* formalism, alongside the already available Statevectors output formats (*text*, *latex*, *latex\_source*, *qsphere*, *hinton*, *bloch*, *city*, *paulivec*).


## Header:
+ Language: python [>= 3.8](https://devguide.python.org/versions/)
+ Library dependencies: [numpy](https://en.wikipedia.org/wiki/NumPy), qiskit
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

2. Load mistkit:
```python
import mistkit
```

3. Run minimal example:
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

4. Uninstall mistkit:
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
help(mistkit.mystify)
```


## Tutorial:

1. [man/misty_bell_states.ipynb](https://github.com/elmbeech/mistkit/blob/main/man/misty_bell_states.ipynb)


## Discussion:

To be developed.


## About Documentation:

Within the mistkit library, we tried to stick to the documentation policy laid out by Daniele Procida in his "[what nobody tells you about documentation](https://www.youtube.com/watch?v=azf6yzuJt54)" talk at PyCon 2017 in Portland, Oregon.


## Cite:
+ ~


## Road Map:
+ ~


## Release Note:

+ version 0.1.1 ok implementation.
+ version 0.0.0 miskit rises from the ashes.

All we know is falling.
